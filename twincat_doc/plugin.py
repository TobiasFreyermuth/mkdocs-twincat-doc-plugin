import os
import re
import sys
from timeit import default_timer as timer
from datetime import datetime, timedelta

import mkdocs.structure.pages
from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin
from mkdocs.utils import write_file
from pathlib import Path
import shutil

from TwinCAT3_plc_files_to_src import get_sources_of_project
from DocClasses.run import get_pou_doc


class TwinCatDoc(BasePlugin):

    config_scheme = (
        ('TwinCAT_proj_dir', config_options.Type(str, default=r'./')),
        ('TwinCAT_autodoc_folder_name', config_options.Type(str, default='autodoc')),
        ('verbose', config_options.Type(bool, default=False)),
        ('project_folder_name_black_lists', config_options.Type(dict, default={})),
        ('project_file_name_black_lists', config_options.Type(dict, default={})),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_pre_build(self, config):
        src_path = self.config.get('TwinCAT_proj_dir')
        autodoc_folder_path = f'./docs/{self.config.get("TwinCAT_autodoc_folder_name", "autodoc")}/'

        rtd_project_name = os.getenv('READTHEDOCS_PROJECT')
        print(f'Red The Docs project name: {rtd_project_name}')

        folder_name_black_list = self.config.get('project_folder_name_black_lists', {}).get(rtd_project_name, [])
        print(f'folder_name_black_list: \n{folder_name_black_list}')

        file_name_black_list = self.config.get('project_file_name_black_lists', {}).get(rtd_project_name, [])
        print(f'file_name_black_list: \n{file_name_black_list}')

        if os.path.exists(autodoc_folder_path):
            shutil.rmtree(autodoc_folder_path)
        os.mkdir(autodoc_folder_path)

        if os.path.exists(src_path):
            for name, folder, src in get_sources_of_project(src_path):
                if skip_item(folder_name_black_list, folder, 'folder'):
                    continue
                if skip_item(file_name_black_list, name, 'file'):
                    continue
                pou = get_pou_doc(src)
                if pou is not None:
                    folder = folder.replace(r'\\', '/')
                    dst_folder = f'{autodoc_folder_path}{folder}'
                    Path(dst_folder).mkdir(parents=True, exist_ok=True)
                    with open(f'{dst_folder}/{name}.md', 'w', encoding="utf-8") as file:
                        file.write(pou.get_MD_doc())

        return


def skip_item(regex_list, folder_name, item_type):
    for regex in regex_list:
        if re.match(regex, folder_name, re.IGNORECASE):
            print(f'skip {item_type}: {folder_name}')
            return True
    else:
        return False

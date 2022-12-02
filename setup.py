'''Package description'''
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    name='mkdocs-twincat-doc-plugin',
    # version='0.0.1',
    description='MkDocs plugin to import retrieve docstrings from TwinCAT project objects and add to docs',
    keywords='mkdocs twincat',
    url='https://github.com/TobiasFreyermuth/mkdocs-twincat-doc-plugin',
    author='Tobias Freyermuth',
    author_email='Tobias.Freyermuth@posteo.net',
    license='MIT',
    python_requires='>=3.7',
    install_requires=[
        'lxml>=4.0.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'twincat_doc = twincat_doc.plugin:TwinCatDoc'
        ]
    },

    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=long_description,

    extras_require={
        "dev": [
            "pytest>=3.7",
        ]
    },
)

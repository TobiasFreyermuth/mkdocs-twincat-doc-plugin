import os
from jinja2 import Environment, FileSystemLoader


class Pou(object):
    def __init__(self):
        self.name = ''
        self.methods = []
        self.properties = []
        self.doc_string = ''

    def add_method(self, method):
        self.methods.append(method)

    def add_property(self, property):
        self.properties.append(property)

    def get_MD_doc(self):
        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        j2_env = Environment(
            loader=FileSystemLoader(
                r'%s/templates/' % THIS_DIR),
            trim_blocks=True)
        return j2_env.get_template('pou_md_doc_template.txt').render(pou=self)

    def write_MD_doc(self, dst_path):
        print(f'write file: {dst_path}')

#        print(j2_env.get_template('pou_md_doc_template.txt').render(pou=self))
        with open(f'{dst_path}/{self.name}.md', 'w', encoding="utf-8") as file:
            file.write(self.get_MD_doc())


class MethodDoc(object):
    def __init__(self, node):
        self.name = node.method_Name().getText()
        if node.return_data_type() is not None:
            self.return_type = node.return_data_type().getText()
        else:
            self.return_type = ''
        if node.DOC_STRING() is not None:
            self.doc_string = node.DOC_STRING().getText()[3:-2]
        else:
            self.doc_string = ''
        self.inputs = [['Name', 'Date Type', 'Default Value']]
        self.outputs = [['Name', 'Date Type', 'Default Value']]
        self.inouts = [['Name', 'Date Type', 'Default Value']]
        for var_block in node.var_in_block() + node.var_in_retain_block() + node.var_in_non_retain_block():
            for stmt in var_block.declaration_stmt():
                self.inputs.append([str(stmt.IDENTIFIER()),
                                    stmt.data_type().getText(),
                                    stmt.constant_expression().getText() if stmt.constant_expression() else ""
                                    ])

        for var_block in node.var_out_block() + node.var_out_retain_block() + node.var_out_non_retain_block():
            for stmt in var_block.declaration_stmt():
                self.outputs.append([str(stmt.IDENTIFIER()),
                                    stmt.data_type().getText(),
                                    stmt.constant_expression().getText() if stmt.constant_expression() else ""
                                    ])

        for var_block in node.var_inout_block():
            for stmt in var_block.declaration_stmt():
                self.inouts.append([str(stmt.IDENTIFIER()),
                                    stmt.data_type().getText(),
                                    stmt.constant_expression().getText() if stmt.constant_expression() else ""
                                    ])

    def make_markdown_table(self, array):
        nl = "\n"
        markdown = nl
        markdown += f"| {' | '.join(array[0])} |"
        markdown += nl
        markdown += f"| {' | '.join(['---'] * len(array[0]))} |"
        markdown += nl
        for entry in array[1:]:
            markdown += f"| {' | '.join(entry)} |{nl}"

        return markdown

    def get_inputs_md_table(self):
        if len(self.inputs) > 1:
            return self.make_markdown_table(self.inputs)
        else:
            return None

    def get_outputs_md_table(self):
        if len(self.outputs) > 1:
            return self.make_markdown_table(self.outputs)
        else:
            return None

    def get_inouts_md_table(self):
        if len(self.inouts) > 1:
            return self.make_markdown_table(self.inouts)
        else:
            return None

    def __str__(self):
        return f'MethodDoc: {self.name}'


class PropertyDoc(object):
    def __init__(self, node):
        self.name = node.property_Name().getText()
        self.getter_doc_string = None
        self.setter_doc_string = None
        if node.return_data_type() is not None:
            self.return_type = node.return_data_type().getText()
        else:
            self.return_type = ''
        if node.DOC_STRING() is not None:
            self.doc_string = node.DOC_STRING().getText()[3:-2]
        else:
            self.doc_string = ''

        getter = node.property_getter_declaration()
        if getter:
            if getter.DOC_STRING() is not None:
                self.getter_doc_string = getter.DOC_STRING().getText()[3:-2]

        setter = node.property_setter_declaration()
        if setter:
            if setter.DOC_STRING() is not None:
                self.setter_doc_string = setter.DOC_STRING().getText()[3:-2]

    def __str__(self):
        return f'PropertyDoc: {self.name}'

import sys
from gen.StructuredTextLexer import StructuredTextLexer
from gen.StructuredTextParser import StructuredTextParser
from gen.StructuredTextListener import StructuredTextListener
from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from TwinCAT3_plc_files_to_src import get_sources_of_project

from DocClasses.ST_docs import Pou, MethodDoc, PropertyDoc


class DocGenerator(StructuredTextListener):
    def __init__(self):
        self.pou = None

    def enterFunction_block_declaration(self, ctx: StructuredTextParser.Function_block_declarationContext):
        pou = Pou()
        if ctx.DOC_STRING() is not None:
            pou.doc_string = ctx.DOC_STRING().getText()[3:-2]

        for x in ctx.getChildren():
            if isinstance(x, StructuredTextParser.Function_block_nameContext):
                pou.name = x.getText()
            elif isinstance(x, StructuredTextParser.Method_declarationContext):
                m = MethodDoc(x)
                pou.add_method(m)
            elif isinstance(x, StructuredTextParser.Parent_function_block_nameContext):
                pass
            elif isinstance(x, StructuredTextParser.Var_in_blockContext):
                pass
            elif isinstance(x, StructuredTextParser.Var_out_blockContext):
                pass
            elif isinstance(x, StructuredTextParser.Var_blockContext):
                pass
            elif isinstance(x, StructuredTextParser.Var_const_blockContext):
                pass
            elif isinstance(x, StructuredTextParser.Interface_Type_AccessContext):
                pass
                # print(x.getText())
            elif isinstance(x, StructuredTextParser.Function_bodyContext):
                pass
            elif isinstance(x, StructuredTextParser.Property_declarationContext):
                p = PropertyDoc(x)
                pou.add_property(p)
            else:
                pass

        self.pou = pou


def run_(src_folder, dst_folder):
    src = """
        FUNCTION_BLOCK InterfaceManager IMPLEMENTS I_InterfaceManager
        VAR
            registrations_in_cycle 	: UINT;
        END_VAR
        VAR CONSTANT 
            MAX_REGISTRATIONS_PER_CYCLE : UINT:=100;
        END_VAR
        registrations_in_cycle:=0;
        
        
        METHOD FB_init : BOOL
        VAR_INPUT
            bInitRetains : BOOL; // if TRUE, the retain variables are initialized (warm start / cold start)
        END_VAR
        test:=test;
        VAR
            tmp: UINT;
        END_VAR
        IF _internal.InterfaceManager_InstanceCounter > 0 THEN
            ;
        ELSE
            _internal.InterfaceManager_InstanceCounter := 1;
        END_IF
        END_METHOD

    """

    input = InputStream(src)
    lexer = StructuredTextLexer(input)
    stream = CommonTokenStream(lexer)
    parser = StructuredTextParser(stream)
    parser.removeErrorListeners()
    # parser._errHandler = MyErrorStrategy()
    tree = parser.pou_declaration()
    # print(tree.toStringTree(recog=parser))
    walker = ParseTreeWalker()
    a = DocGenerator(dst_folder)
    walker.walk(a, tree)


def run(src_folder, dst_folder):
    pous = []
    for pou_name, sub_folder, src in get_sources_of_project(src_folder):
        if src is None:
            print(f'Source string empty: {pou_name}')
            continue
#        print(f'\n==== {pou_name} =======================')
        input = InputStream(src)
        lexer = StructuredTextLexer(input)
        stream = CommonTokenStream(lexer)
        parser = StructuredTextParser(stream)
        parser.removeErrorListeners()
        # parser._errHandler = MyErrorStrategy()
        tree = parser.pou_declaration()
        # print(tree.toStringTree(recog=parser))
        walker = ParseTreeWalker()
        a = DocGenerator(pous)
        walker.walk(a, tree)


def get_pou_doc(src):
    input = InputStream(src)
    lexer = StructuredTextLexer(input)
    stream = CommonTokenStream(lexer)
    parser = StructuredTextParser(stream)
    parser.removeErrorListeners()
    # parser._errHandler = MyErrorStrategy()
    tree = parser.pou_declaration()
    # print(tree.toStringTree(recog=parser))
    walker = ParseTreeWalker()
    a = DocGenerator()
    walker.walk(a, tree)
    return a.pou


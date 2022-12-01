# Generated from .\StructuredText.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .StructuredTextParser import StructuredTextParser
else:
    from StructuredTextParser import StructuredTextParser

# This class defines a complete listener for a parse tree produced by StructuredTextParser.
class StructuredTextListener(ParseTreeListener):

    # Enter a parse tree produced by StructuredTextParser#number.
    def enterNumber(self, ctx:StructuredTextParser.NumberContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#number.
    def exitNumber(self, ctx:StructuredTextParser.NumberContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#typed_number.
    def enterTyped_number(self, ctx:StructuredTextParser.Typed_numberContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#typed_number.
    def exitTyped_number(self, ctx:StructuredTextParser.Typed_numberContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#row_number.
    def enterRow_number(self, ctx:StructuredTextParser.Row_numberContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#row_number.
    def exitRow_number(self, ctx:StructuredTextParser.Row_numberContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#pou_declaration.
    def enterPou_declaration(self, ctx:StructuredTextParser.Pou_declarationContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#pou_declaration.
    def exitPou_declaration(self, ctx:StructuredTextParser.Pou_declarationContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#namespace_Name.
    def enterNamespace_Name(self, ctx:StructuredTextParser.Namespace_NameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#namespace_Name.
    def exitNamespace_Name(self, ctx:StructuredTextParser.Namespace_NameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#function_name.
    def enterFunction_name(self, ctx:StructuredTextParser.Function_nameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#function_name.
    def exitFunction_name(self, ctx:StructuredTextParser.Function_nameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#func_Access.
    def enterFunc_Access(self, ctx:StructuredTextParser.Func_AccessContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#func_Access.
    def exitFunc_Access(self, ctx:StructuredTextParser.Func_AccessContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#derived_Func_Name.
    def enterDerived_Func_Name(self, ctx:StructuredTextParser.Derived_Func_NameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#derived_Func_Name.
    def exitDerived_Func_Name(self, ctx:StructuredTextParser.Derived_Func_NameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#function_declaration.
    def enterFunction_declaration(self, ctx:StructuredTextParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#function_declaration.
    def exitFunction_declaration(self, ctx:StructuredTextParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#elementary_data_types.
    def enterElementary_data_types(self, ctx:StructuredTextParser.Elementary_data_typesContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#elementary_data_types.
    def exitElementary_data_types(self, ctx:StructuredTextParser.Elementary_data_typesContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#array_data_type.
    def enterArray_data_type(self, ctx:StructuredTextParser.Array_data_typeContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#array_data_type.
    def exitArray_data_type(self, ctx:StructuredTextParser.Array_data_typeContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#fb_Type_Name.
    def enterFb_Type_Name(self, ctx:StructuredTextParser.Fb_Type_NameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#fb_Type_Name.
    def exitFb_Type_Name(self, ctx:StructuredTextParser.Fb_Type_NameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#fb_Type_Access.
    def enterFb_Type_Access(self, ctx:StructuredTextParser.Fb_Type_AccessContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#fb_Type_Access.
    def exitFb_Type_Access(self, ctx:StructuredTextParser.Fb_Type_AccessContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#function_block_name.
    def enterFunction_block_name(self, ctx:StructuredTextParser.Function_block_nameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#function_block_name.
    def exitFunction_block_name(self, ctx:StructuredTextParser.Function_block_nameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#parent_function_block_name.
    def enterParent_function_block_name(self, ctx:StructuredTextParser.Parent_function_block_nameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#parent_function_block_name.
    def exitParent_function_block_name(self, ctx:StructuredTextParser.Parent_function_block_nameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#function_block_declaration.
    def enterFunction_block_declaration(self, ctx:StructuredTextParser.Function_block_declarationContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#function_block_declaration.
    def exitFunction_block_declaration(self, ctx:StructuredTextParser.Function_block_declarationContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#return_data_type.
    def enterReturn_data_type(self, ctx:StructuredTextParser.Return_data_typeContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#return_data_type.
    def exitReturn_data_type(self, ctx:StructuredTextParser.Return_data_typeContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#data_type.
    def enterData_type(self, ctx:StructuredTextParser.Data_typeContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#data_type.
    def exitData_type(self, ctx:StructuredTextParser.Data_typeContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#method_Name.
    def enterMethod_Name(self, ctx:StructuredTextParser.Method_NameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#method_Name.
    def exitMethod_Name(self, ctx:StructuredTextParser.Method_NameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#property_Name.
    def enterProperty_Name(self, ctx:StructuredTextParser.Property_NameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#property_Name.
    def exitProperty_Name(self, ctx:StructuredTextParser.Property_NameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#fb_Instance_Name.
    def enterFb_Instance_Name(self, ctx:StructuredTextParser.Fb_Instance_NameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#fb_Instance_Name.
    def exitFb_Instance_Name(self, ctx:StructuredTextParser.Fb_Instance_NameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#interface_Decl.
    def enterInterface_Decl(self, ctx:StructuredTextParser.Interface_DeclContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#interface_Decl.
    def exitInterface_Decl(self, ctx:StructuredTextParser.Interface_DeclContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#method_Prototype.
    def enterMethod_Prototype(self, ctx:StructuredTextParser.Method_PrototypeContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#method_Prototype.
    def exitMethod_Prototype(self, ctx:StructuredTextParser.Method_PrototypeContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#method_declaration.
    def enterMethod_declaration(self, ctx:StructuredTextParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#method_declaration.
    def exitMethod_declaration(self, ctx:StructuredTextParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#property_getter_declaration.
    def enterProperty_getter_declaration(self, ctx:StructuredTextParser.Property_getter_declarationContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#property_getter_declaration.
    def exitProperty_getter_declaration(self, ctx:StructuredTextParser.Property_getter_declarationContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#property_setter_declaration.
    def enterProperty_setter_declaration(self, ctx:StructuredTextParser.Property_setter_declarationContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#property_setter_declaration.
    def exitProperty_setter_declaration(self, ctx:StructuredTextParser.Property_setter_declarationContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#property_declaration.
    def enterProperty_declaration(self, ctx:StructuredTextParser.Property_declarationContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#property_declaration.
    def exitProperty_declaration(self, ctx:StructuredTextParser.Property_declarationContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#interface_Value.
    def enterInterface_Value(self, ctx:StructuredTextParser.Interface_ValueContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#interface_Value.
    def exitInterface_Value(self, ctx:StructuredTextParser.Interface_ValueContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#interface_Name_List.
    def enterInterface_Name_List(self, ctx:StructuredTextParser.Interface_Name_ListContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#interface_Name_List.
    def exitInterface_Name_List(self, ctx:StructuredTextParser.Interface_Name_ListContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#interface_Type_Name.
    def enterInterface_Type_Name(self, ctx:StructuredTextParser.Interface_Type_NameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#interface_Type_Name.
    def exitInterface_Type_Name(self, ctx:StructuredTextParser.Interface_Type_NameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#interface_Type_Access.
    def enterInterface_Type_Access(self, ctx:StructuredTextParser.Interface_Type_AccessContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#interface_Type_Access.
    def exitInterface_Type_Access(self, ctx:StructuredTextParser.Interface_Type_AccessContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#interface_Name.
    def enterInterface_Name(self, ctx:StructuredTextParser.Interface_NameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#interface_Name.
    def exitInterface_Name(self, ctx:StructuredTextParser.Interface_NameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#access_Spec.
    def enterAccess_Spec(self, ctx:StructuredTextParser.Access_SpecContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#access_Spec.
    def exitAccess_Spec(self, ctx:StructuredTextParser.Access_SpecContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_block.
    def enterVar_block(self, ctx:StructuredTextParser.Var_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_block.
    def exitVar_block(self, ctx:StructuredTextParser.Var_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_const_block.
    def enterVar_const_block(self, ctx:StructuredTextParser.Var_const_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_const_block.
    def exitVar_const_block(self, ctx:StructuredTextParser.Var_const_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_retain_block.
    def enterVar_retain_block(self, ctx:StructuredTextParser.Var_retain_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_retain_block.
    def exitVar_retain_block(self, ctx:StructuredTextParser.Var_retain_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_non_retain_block.
    def enterVar_non_retain_block(self, ctx:StructuredTextParser.Var_non_retain_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_non_retain_block.
    def exitVar_non_retain_block(self, ctx:StructuredTextParser.Var_non_retain_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_in_block.
    def enterVar_in_block(self, ctx:StructuredTextParser.Var_in_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_in_block.
    def exitVar_in_block(self, ctx:StructuredTextParser.Var_in_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_in_retain_block.
    def enterVar_in_retain_block(self, ctx:StructuredTextParser.Var_in_retain_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_in_retain_block.
    def exitVar_in_retain_block(self, ctx:StructuredTextParser.Var_in_retain_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_in_non_retain_block.
    def enterVar_in_non_retain_block(self, ctx:StructuredTextParser.Var_in_non_retain_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_in_non_retain_block.
    def exitVar_in_non_retain_block(self, ctx:StructuredTextParser.Var_in_non_retain_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_out_block.
    def enterVar_out_block(self, ctx:StructuredTextParser.Var_out_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_out_block.
    def exitVar_out_block(self, ctx:StructuredTextParser.Var_out_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_out_retain_block.
    def enterVar_out_retain_block(self, ctx:StructuredTextParser.Var_out_retain_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_out_retain_block.
    def exitVar_out_retain_block(self, ctx:StructuredTextParser.Var_out_retain_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_out_non_retain_block.
    def enterVar_out_non_retain_block(self, ctx:StructuredTextParser.Var_out_non_retain_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_out_non_retain_block.
    def exitVar_out_non_retain_block(self, ctx:StructuredTextParser.Var_out_non_retain_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_inout_block.
    def enterVar_inout_block(self, ctx:StructuredTextParser.Var_inout_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_inout_block.
    def exitVar_inout_block(self, ctx:StructuredTextParser.Var_inout_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_temp_block.
    def enterVar_temp_block(self, ctx:StructuredTextParser.Var_temp_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_temp_block.
    def exitVar_temp_block(self, ctx:StructuredTextParser.Var_temp_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_external_block.
    def enterVar_external_block(self, ctx:StructuredTextParser.Var_external_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_external_block.
    def exitVar_external_block(self, ctx:StructuredTextParser.Var_external_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_external_const_block.
    def enterVar_external_const_block(self, ctx:StructuredTextParser.Var_external_const_blockContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_external_const_block.
    def exitVar_external_const_block(self, ctx:StructuredTextParser.Var_external_const_blockContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#declaration_stmt.
    def enterDeclaration_stmt(self, ctx:StructuredTextParser.Declaration_stmtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#declaration_stmt.
    def exitDeclaration_stmt(self, ctx:StructuredTextParser.Declaration_stmtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#constant_expression.
    def enterConstant_expression(self, ctx:StructuredTextParser.Constant_expressionContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#constant_expression.
    def exitConstant_expression(self, ctx:StructuredTextParser.Constant_expressionContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#expression.
    def enterExpression(self, ctx:StructuredTextParser.ExpressionContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#expression.
    def exitExpression(self, ctx:StructuredTextParser.ExpressionContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#primary_Expr.
    def enterPrimary_Expr(self, ctx:StructuredTextParser.Primary_ExprContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#primary_Expr.
    def exitPrimary_Expr(self, ctx:StructuredTextParser.Primary_ExprContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#term.
    def enterTerm(self, ctx:StructuredTextParser.TermContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#term.
    def exitTerm(self, ctx:StructuredTextParser.TermContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#comparator.
    def enterComparator(self, ctx:StructuredTextParser.ComparatorContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#comparator.
    def exitComparator(self, ctx:StructuredTextParser.ComparatorContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#add_sub.
    def enterAdd_sub(self, ctx:StructuredTextParser.Add_subContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#add_sub.
    def exitAdd_sub(self, ctx:StructuredTextParser.Add_subContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#unary.
    def enterUnary(self, ctx:StructuredTextParser.UnaryContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#unary.
    def exitUnary(self, ctx:StructuredTextParser.UnaryContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#multibit_Part_Access.
    def enterMultibit_Part_Access(self, ctx:StructuredTextParser.Multibit_Part_AccessContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#multibit_Part_Access.
    def exitMultibit_Part_Access(self, ctx:StructuredTextParser.Multibit_Part_AccessContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#variable.
    def enterVariable(self, ctx:StructuredTextParser.VariableContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#variable.
    def exitVariable(self, ctx:StructuredTextParser.VariableContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#symbolic_Variable.
    def enterSymbolic_Variable(self, ctx:StructuredTextParser.Symbolic_VariableContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#symbolic_Variable.
    def exitSymbolic_Variable(self, ctx:StructuredTextParser.Symbolic_VariableContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#var_Access.
    def enterVar_Access(self, ctx:StructuredTextParser.Var_AccessContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#var_Access.
    def exitVar_Access(self, ctx:StructuredTextParser.Var_AccessContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#variable_Name.
    def enterVariable_Name(self, ctx:StructuredTextParser.Variable_NameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#variable_Name.
    def exitVariable_Name(self, ctx:StructuredTextParser.Variable_NameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#multi_Elem_Var.
    def enterMulti_Elem_Var(self, ctx:StructuredTextParser.Multi_Elem_VarContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#multi_Elem_Var.
    def exitMulti_Elem_Var(self, ctx:StructuredTextParser.Multi_Elem_VarContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#subscript_List.
    def enterSubscript_List(self, ctx:StructuredTextParser.Subscript_ListContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#subscript_List.
    def exitSubscript_List(self, ctx:StructuredTextParser.Subscript_ListContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#subscript.
    def enterSubscript(self, ctx:StructuredTextParser.SubscriptContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#subscript.
    def exitSubscript(self, ctx:StructuredTextParser.SubscriptContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#global_Var_Name.
    def enterGlobal_Var_Name(self, ctx:StructuredTextParser.Global_Var_NameContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#global_Var_Name.
    def exitGlobal_Var_Name(self, ctx:StructuredTextParser.Global_Var_NameContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#global_Var_Decls.
    def enterGlobal_Var_Decls(self, ctx:StructuredTextParser.Global_Var_DeclsContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#global_Var_Decls.
    def exitGlobal_Var_Decls(self, ctx:StructuredTextParser.Global_Var_DeclsContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#global_Var_Decl.
    def enterGlobal_Var_Decl(self, ctx:StructuredTextParser.Global_Var_DeclContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#global_Var_Decl.
    def exitGlobal_Var_Decl(self, ctx:StructuredTextParser.Global_Var_DeclContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#global_Var_Spec.
    def enterGlobal_Var_Spec(self, ctx:StructuredTextParser.Global_Var_SpecContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#global_Var_Spec.
    def exitGlobal_Var_Spec(self, ctx:StructuredTextParser.Global_Var_SpecContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#located_At.
    def enterLocated_At(self, ctx:StructuredTextParser.Located_AtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#located_At.
    def exitLocated_At(self, ctx:StructuredTextParser.Located_AtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#direct_Variable.
    def enterDirect_Variable(self, ctx:StructuredTextParser.Direct_VariableContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#direct_Variable.
    def exitDirect_Variable(self, ctx:StructuredTextParser.Direct_VariableContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#constant_Expr.
    def enterConstant_Expr(self, ctx:StructuredTextParser.Constant_ExprContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#constant_Expr.
    def exitConstant_Expr(self, ctx:StructuredTextParser.Constant_ExprContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#variable_Access.
    def enterVariable_Access(self, ctx:StructuredTextParser.Variable_AccessContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#variable_Access.
    def exitVariable_Access(self, ctx:StructuredTextParser.Variable_AccessContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#func_Call.
    def enterFunc_Call(self, ctx:StructuredTextParser.Func_CallContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#func_Call.
    def exitFunc_Call(self, ctx:StructuredTextParser.Func_CallContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#stmt_List.
    def enterStmt_List(self, ctx:StructuredTextParser.Stmt_ListContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#stmt_List.
    def exitStmt_List(self, ctx:StructuredTextParser.Stmt_ListContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#stmt.
    def enterStmt(self, ctx:StructuredTextParser.StmtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#stmt.
    def exitStmt(self, ctx:StructuredTextParser.StmtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#assign_Stmt.
    def enterAssign_Stmt(self, ctx:StructuredTextParser.Assign_StmtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#assign_Stmt.
    def exitAssign_Stmt(self, ctx:StructuredTextParser.Assign_StmtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#subprog_Ctrl_Stmt.
    def enterSubprog_Ctrl_Stmt(self, ctx:StructuredTextParser.Subprog_Ctrl_StmtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#subprog_Ctrl_Stmt.
    def exitSubprog_Ctrl_Stmt(self, ctx:StructuredTextParser.Subprog_Ctrl_StmtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#param_Assign.
    def enterParam_Assign(self, ctx:StructuredTextParser.Param_AssignContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#param_Assign.
    def exitParam_Assign(self, ctx:StructuredTextParser.Param_AssignContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#selection_Stmt.
    def enterSelection_Stmt(self, ctx:StructuredTextParser.Selection_StmtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#selection_Stmt.
    def exitSelection_Stmt(self, ctx:StructuredTextParser.Selection_StmtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#if_Stmt.
    def enterIf_Stmt(self, ctx:StructuredTextParser.If_StmtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#if_Stmt.
    def exitIf_Stmt(self, ctx:StructuredTextParser.If_StmtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#case_Stmt.
    def enterCase_Stmt(self, ctx:StructuredTextParser.Case_StmtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#case_Stmt.
    def exitCase_Stmt(self, ctx:StructuredTextParser.Case_StmtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#case_Selection.
    def enterCase_Selection(self, ctx:StructuredTextParser.Case_SelectionContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#case_Selection.
    def exitCase_Selection(self, ctx:StructuredTextParser.Case_SelectionContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#case_List.
    def enterCase_List(self, ctx:StructuredTextParser.Case_ListContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#case_List.
    def exitCase_List(self, ctx:StructuredTextParser.Case_ListContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#case_List_Elem.
    def enterCase_List_Elem(self, ctx:StructuredTextParser.Case_List_ElemContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#case_List_Elem.
    def exitCase_List_Elem(self, ctx:StructuredTextParser.Case_List_ElemContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#iteration_Stmt.
    def enterIteration_Stmt(self, ctx:StructuredTextParser.Iteration_StmtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#iteration_Stmt.
    def exitIteration_Stmt(self, ctx:StructuredTextParser.Iteration_StmtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#for_Stmt.
    def enterFor_Stmt(self, ctx:StructuredTextParser.For_StmtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#for_Stmt.
    def exitFor_Stmt(self, ctx:StructuredTextParser.For_StmtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#control_Variable.
    def enterControl_Variable(self, ctx:StructuredTextParser.Control_VariableContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#control_Variable.
    def exitControl_Variable(self, ctx:StructuredTextParser.Control_VariableContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#for_List.
    def enterFor_List(self, ctx:StructuredTextParser.For_ListContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#for_List.
    def exitFor_List(self, ctx:StructuredTextParser.For_ListContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#while_Stmt.
    def enterWhile_Stmt(self, ctx:StructuredTextParser.While_StmtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#while_Stmt.
    def exitWhile_Stmt(self, ctx:StructuredTextParser.While_StmtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#repeat_Stmt.
    def enterRepeat_Stmt(self, ctx:StructuredTextParser.Repeat_StmtContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#repeat_Stmt.
    def exitRepeat_Stmt(self, ctx:StructuredTextParser.Repeat_StmtContext):
        pass


    # Enter a parse tree produced by StructuredTextParser#function_body.
    def enterFunction_body(self, ctx:StructuredTextParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by StructuredTextParser#function_body.
    def exitFunction_body(self, ctx:StructuredTextParser.Function_bodyContext):
        pass



del StructuredTextParser
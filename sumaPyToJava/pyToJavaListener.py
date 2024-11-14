# Generated from pyToJava.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pyToJavaParser import pyToJavaParser
else:
    from pyToJavaParser import pyToJavaParser

# This class defines a complete listener for a parse tree produced by pyToJavaParser.
class pyToJavaListener(ParseTreeListener):

    # Enter a parse tree produced by pyToJavaParser#program.
    def enterProgram(self, ctx:pyToJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#program.
    def exitProgram(self, ctx:pyToJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#statement.
    def enterStatement(self, ctx:pyToJavaParser.StatementContext):
        pass


    # Exit a parse tree produced by pyToJavaParser#statement.
    def exitStatement(self, ctx:pyToJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#function.
    def enterFunction(self, ctx:pyToJavaParser.FunctionContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#function.
    def exitFunction(self, ctx:pyToJavaParser.FunctionContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#parameters.
    def enterParameters(self, ctx:pyToJavaParser.ParametersContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#parameters.
    def exitParameters(self, ctx:pyToJavaParser.ParametersContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#block.
    def enterBlock(self, ctx:pyToJavaParser.BlockContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#block.
    def exitBlock(self, ctx:pyToJavaParser.BlockContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#returnStatement.
    def enterReturnStatement(self, ctx:pyToJavaParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#returnStatement.
    def exitReturnStatement(self, ctx:pyToJavaParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#printStatement.
    def enterPrintStatement(self, ctx:pyToJavaParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#printStatement.
    def exitPrintStatement(self, ctx:pyToJavaParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#expression.
    def enterExpression(self, ctx:pyToJavaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#expression.
    def exitExpression(self, ctx:pyToJavaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#functionCall.
    def enterFunctionCall(self, ctx:pyToJavaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#functionCall.
    def exitFunctionCall(self, ctx:pyToJavaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#operator.
    def enterOperator(self, ctx:pyToJavaParser.OperatorContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#operator.
    def exitOperator(self, ctx:pyToJavaParser.OperatorContext):
        pass



del pyToJavaParser
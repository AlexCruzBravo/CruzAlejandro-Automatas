# Generated from pyToJava.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,100,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,3,2,38,8,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,5,3,47,8,3,10,3,12,3,50,9,3,1,4,4,4,53,8,4,11,4,
        12,4,54,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,73,8,7,1,7,1,7,1,7,1,7,5,7,79,8,7,10,7,12,7,82,9,7,1,
        8,1,8,1,8,1,8,1,8,5,8,89,8,8,10,8,12,8,92,9,8,3,8,94,8,8,1,8,1,8,
        1,9,1,9,1,9,0,1,14,10,0,2,4,6,8,10,12,14,16,18,0,1,1,0,8,11,102,
        0,21,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,43,1,0,0,0,8,52,1,0,0,0,
        10,56,1,0,0,0,12,59,1,0,0,0,14,72,1,0,0,0,16,83,1,0,0,0,18,97,1,
        0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,
        24,1,0,0,0,24,25,1,0,0,0,25,26,5,0,0,1,26,1,1,0,0,0,27,32,3,4,2,
        0,28,32,3,10,5,0,29,32,3,12,6,0,30,32,3,14,7,0,31,27,1,0,0,0,31,
        28,1,0,0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,34,5,1,0,
        0,34,35,5,12,0,0,35,37,5,6,0,0,36,38,3,6,3,0,37,36,1,0,0,0,37,38,
        1,0,0,0,38,39,1,0,0,0,39,40,5,7,0,0,40,41,5,4,0,0,41,42,3,8,4,0,
        42,5,1,0,0,0,43,48,5,12,0,0,44,45,5,5,0,0,45,47,5,12,0,0,46,44,1,
        0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,7,1,0,0,0,50,
        48,1,0,0,0,51,53,3,2,1,0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,
        0,54,55,1,0,0,0,55,9,1,0,0,0,56,57,5,2,0,0,57,58,3,14,7,0,58,11,
        1,0,0,0,59,60,5,3,0,0,60,61,5,6,0,0,61,62,3,14,7,0,62,63,5,7,0,0,
        63,13,1,0,0,0,64,65,6,7,-1,0,65,73,5,12,0,0,66,73,5,13,0,0,67,73,
        3,16,8,0,68,69,5,6,0,0,69,70,3,14,7,0,70,71,5,7,0,0,71,73,1,0,0,
        0,72,64,1,0,0,0,72,66,1,0,0,0,72,67,1,0,0,0,72,68,1,0,0,0,73,80,
        1,0,0,0,74,75,10,2,0,0,75,76,3,18,9,0,76,77,3,14,7,3,77,79,1,0,0,
        0,78,74,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,15,
        1,0,0,0,82,80,1,0,0,0,83,84,5,12,0,0,84,93,5,6,0,0,85,90,3,14,7,
        0,86,87,5,5,0,0,87,89,3,14,7,0,88,86,1,0,0,0,89,92,1,0,0,0,90,88,
        1,0,0,0,90,91,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,93,85,1,0,0,0,
        93,94,1,0,0,0,94,95,1,0,0,0,95,96,5,7,0,0,96,17,1,0,0,0,97,98,7,
        0,0,0,98,19,1,0,0,0,9,23,31,37,48,54,72,80,90,93
    ]

class pyToJavaParser ( Parser ):

    grammarFileName = "pyToJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'print'", "':'", 
                     "','", "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "PRINT", "COLON", "COMMA", 
                      "LPAREN", "RPAREN", "PLUS", "MINUS", "MULT", "DIV", 
                      "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_function = 2
    RULE_parameters = 3
    RULE_block = 4
    RULE_returnStatement = 5
    RULE_printStatement = 6
    RULE_expression = 7
    RULE_functionCall = 8
    RULE_operator = 9

    ruleNames =  [ "program", "statement", "function", "parameters", "block", 
                   "returnStatement", "printStatement", "expression", "functionCall", 
                   "operator" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    PRINT=3
    COLON=4
    COMMA=5
    LPAREN=6
    RPAREN=7
    PLUS=8
    MINUS=9
    MULT=10
    DIV=11
    ID=12
    NUMBER=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(pyToJavaParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyToJavaParser.StatementContext)
            else:
                return self.getTypedRuleContext(pyToJavaParser.StatementContext,i)


        def getRuleIndex(self):
            return pyToJavaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = pyToJavaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 12366) != 0)):
                    break

            self.state = 25
            self.match(pyToJavaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(pyToJavaParser.FunctionContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(pyToJavaParser.ReturnStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(pyToJavaParser.PrintStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(pyToJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return pyToJavaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = pyToJavaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.function()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.returnStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.printStatement()
                pass
            elif token in [6, 12, 13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(pyToJavaParser.DEF, 0)

        def ID(self):
            return self.getToken(pyToJavaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(pyToJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(pyToJavaParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(pyToJavaParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(pyToJavaParser.BlockContext,0)


        def parameters(self):
            return self.getTypedRuleContext(pyToJavaParser.ParametersContext,0)


        def getRuleIndex(self):
            return pyToJavaParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = pyToJavaParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(pyToJavaParser.DEF)
            self.state = 34
            self.match(pyToJavaParser.ID)
            self.state = 35
            self.match(pyToJavaParser.LPAREN)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 36
                self.parameters()


            self.state = 39
            self.match(pyToJavaParser.RPAREN)
            self.state = 40
            self.match(pyToJavaParser.COLON)
            self.state = 41
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(pyToJavaParser.ID)
            else:
                return self.getToken(pyToJavaParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(pyToJavaParser.COMMA)
            else:
                return self.getToken(pyToJavaParser.COMMA, i)

        def getRuleIndex(self):
            return pyToJavaParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = pyToJavaParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(pyToJavaParser.ID)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 44
                self.match(pyToJavaParser.COMMA)
                self.state = 45
                self.match(pyToJavaParser.ID)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyToJavaParser.StatementContext)
            else:
                return self.getTypedRuleContext(pyToJavaParser.StatementContext,i)


        def getRuleIndex(self):
            return pyToJavaParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = pyToJavaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 51
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 54 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(pyToJavaParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(pyToJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return pyToJavaParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = pyToJavaParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(pyToJavaParser.RETURN)
            self.state = 57
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(pyToJavaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(pyToJavaParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(pyToJavaParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(pyToJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return pyToJavaParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = pyToJavaParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(pyToJavaParser.PRINT)
            self.state = 60
            self.match(pyToJavaParser.LPAREN)
            self.state = 61
            self.expression(0)
            self.state = 62
            self.match(pyToJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(pyToJavaParser.ID, 0)

        def NUMBER(self):
            return self.getToken(pyToJavaParser.NUMBER, 0)

        def functionCall(self):
            return self.getTypedRuleContext(pyToJavaParser.FunctionCallContext,0)


        def LPAREN(self):
            return self.getToken(pyToJavaParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyToJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pyToJavaParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(pyToJavaParser.RPAREN, 0)

        def operator(self):
            return self.getTypedRuleContext(pyToJavaParser.OperatorContext,0)


        def getRuleIndex(self):
            return pyToJavaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pyToJavaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 65
                self.match(pyToJavaParser.ID)
                pass

            elif la_ == 2:
                self.state = 66
                self.match(pyToJavaParser.NUMBER)
                pass

            elif la_ == 3:
                self.state = 67
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 68
                self.match(pyToJavaParser.LPAREN)
                self.state = 69
                self.expression(0)
                self.state = 70
                self.match(pyToJavaParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = pyToJavaParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 74
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 75
                    self.operator()
                    self.state = 76
                    self.expression(3) 
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(pyToJavaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(pyToJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(pyToJavaParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyToJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pyToJavaParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(pyToJavaParser.COMMA)
            else:
                return self.getToken(pyToJavaParser.COMMA, i)

        def getRuleIndex(self):
            return pyToJavaParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = pyToJavaParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(pyToJavaParser.ID)
            self.state = 84
            self.match(pyToJavaParser.LPAREN)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 12352) != 0):
                self.state = 85
                self.expression(0)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 86
                    self.match(pyToJavaParser.COMMA)
                    self.state = 87
                    self.expression(0)
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 95
            self.match(pyToJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(pyToJavaParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(pyToJavaParser.MINUS, 0)

        def MULT(self):
            return self.getToken(pyToJavaParser.MULT, 0)

        def DIV(self):
            return self.getToken(pyToJavaParser.DIV, 0)

        def getRuleIndex(self):
            return pyToJavaParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = pyToJavaParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         





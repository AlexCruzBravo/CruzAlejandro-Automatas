from pyToJavaListener import pyToJavaListener
from pyToJavaParser import pyToJavaParser


class ListenerSuma(pyToJavaListener):
    def __init__(self):
        self.java_file=open("Main.java","w")
    
    # Enter a parse tree produced by pyToJavaParser#program.
    def enterProgram(self, ctx:pyToJavaParser.ProgramContext): 
        self.java_file.write("public class Main {\n")
        print("\npublic class Main{")

    # Exit a parse tree produced by pyToJavaParser#program.
    def exitProgram(self, ctx:pyToJavaParser.ProgramContext):
        self.java_file.write("\n}")  # Cierra la clase Main
        self.java_file.close()
        print("}")
        print("\nArchivo JAVA generado exitosamente (Main.java)")
        pass


    # Enter a parse tree produced by pyToJavaParser#function.
    def enterFunction(self, ctx:pyToJavaParser.FunctionContext):
        self.java_file.write(f"\tpublic static int {ctx.ID().getText()}(")  # Escribe la declaración de la función

        print("\tpublic static int",ctx.ID().getText(),"(", end='')
    

    # Enter a parse tree produced by pyToJavaParser#parameters.
    def enterParameters(self, ctx:pyToJavaParser.ParametersContext):
        parametros =[f"int {param.getText()}" for param in ctx.ID()]
        
        self.java_file.write(", ".join(parametros))
        print(", ".join(parametros), end='')
        
    # Exit a parse tree produced by pyToJavaParser#parameters.
    def exitParameters(self, ctx:pyToJavaParser.ParametersContext):
        self.java_file.write(") {\n")
        print(")",end='')
        pass


    # Enter a parse tree produced by pyToJavaParser#block.
    def enterBlock(self, ctx:pyToJavaParser.BlockContext):
        print("{")


    # Enter a parse tree produced by pyToJavaParser#returnStatement.
    def enterReturnStatement(self, ctx:pyToJavaParser.ReturnStatementContext):
        self.java_file.write("\t\t" + ctx.RETURN().getText() + " " + ctx.expression().getText() + ";\n")
        self.java_file.write("\t}\n") # Escribe la sentencia return
        
        print("\t\t",ctx.RETURN().getText(),end=' ')
        print(ctx.expression().getText(),";\n")
        pass


    # Enter a parse tree produced by pyToJavaParser#printStatement.
    def enterPrintStatement(self, ctx:pyToJavaParser.PrintStatementContext):
        self.java_file.write("\tpublic static void main(String[] args) {\n")
        print("\tpublic static void main(String[] args) {")
        pass

    # Exit a parse tree produced by pyToJavaParser#printStatement.
    def exitPrintStatement(self, ctx:pyToJavaParser.PrintStatementContext):
        self.java_file.write("\t}")
        print("\t}")
        pass


    # Enter a parse tree produced by pyToJavaParser#functionCall.
    def enterFunctionCall(self, ctx:pyToJavaParser.FunctionCallContext):
        
        print("\t\tSystem.out.println(",ctx.ID().getText(),"(",end='')
        if ctx.expression():
            args = [exp.getText() for exp in ctx.expression()]
            self.java_file.write(f"\t\tSystem.out.println({ctx.ID().getText()}({",".join(args)}")
            print(", ".join(args), end='')

    # Exit a parse tree produced by pyToJavaParser#functionCall.
    def exitFunctionCall(self, ctx:pyToJavaParser.FunctionCallContext):
        self.java_file.write("));\n")
        print("));")
        pass

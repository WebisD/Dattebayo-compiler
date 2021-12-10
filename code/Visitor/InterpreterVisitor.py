from .NodeVisitor import NodeVisitor
from Tokens.TokenEnum import TokenEnum as te
import re


class InterpreterVisitor(NodeVisitor):
    def __init__(self, all_ast, file_name):
        """ Performs the creation of an object of type InterpreterVisitor

        :param all_ast: All ASTs
        :param file_name: the file name
        """
        self.asts = all_ast
        self.file_name = re.split('[./]', file_name)[1]

    def run_visitor(self):
        """ Run the visitor

        """
        f = open(f"TestCases/GeneratedCases/{self.file_name}.py", "w")
        for ast in self.asts:
            code = self.visit(ast)
            f.write(code + '\n')
        f.close()

        print(f"Your code is in: TestCases/GeneratedCases/{self.file_name}.py")

    def visit_BinOp(self, node, indentation=None):
        """ Execute the visit of binOp

        """
        final_code = ""
        if node.op.type == te.FUUMASHURIKEN:
            final_code += self.visit(node.left) + ' + ' + self.visit(node.right)
        elif node.op.type == te.KUNAI:
            final_code += self.visit(node.left) + ' - ' + self.visit(node.right)
        elif node.op.type == te.SHURIKEN:
            final_code += self.visit(node.left) + ' * ' + self.visit(node.right)
        elif node.op.type == te.KATANA:
            final_code += self.visit(node.left) + ' + ' + self.visit(node.right)
        elif node.op.type == te.GENNIN:
            final_code += self.visit(node.left) + ' < ' + self.visit(node.right)
        elif node.op.type == te.JUNNIN:
            final_code += self.visit(node.left) + ' > ' + self.visit(node.right)
        elif node.op.type == te.KIRIGAKURE:
            final_code += self.visit(node.left) + ' == ' + self.visit(node.right)
        elif node.op.type == te.KUMOGAKURE:
            final_code += self.visit(node.left) + ' and ' + self.visit(node.right)
        elif node.op.type == te.AMEGAKURE:
            final_code += self.visit(node.left) + ' or ' + self.visit(node.right)
        return final_code

    def visit_Num(self, node, indentation=None):
        """ Visit a number

        """
        return str(node.value)

    def visit_VariableAST(self, node, indentation=None):
        """ Visit a Variable AST

        """
        final_code = ""
        if node.value is not None:
            final_code += node.name + ' = ' + self.visit(node.value)
        else:
            final_code += node.name

        return final_code

    def visit_Str(self, node, indentation=None):
        """ Visit a String

        """
        return node.value

    def visit_Bool(self, node, indentation=None):
        """ Visit a boolean

        """
        return str(node.value)

    def visit_PrintAST(self, node, indentation=None):
        """ Visit a Print AST

        """
        final_code = f"print({self.visit(node.value)})"
        return final_code

    def visit_WhileAST(self, node, indentation=None):
        """ Visit a While AST

        """
        final_code = f"while ( {self.visit(node.condition)} ):"

        for scope in node.scope:
            final_code += "\n"
            final_code += f"{4*' '}{self.visit(scope)}"

        return final_code

    def visit_IfAST(self, node, indentation=4*' '):
        """ Visit a If AST

        """
        if not indentation:
            indentation = 4*' '

        final_code = f"if ( {self.visit(node.condition)} ):"

        for scope in node.scope:
            final_code += "\n"
            final_code += f"{indentation}{self.visit(scope, indentation*2)}"

        return final_code

    def visit_ElseAST(self, node, indentation=4*' '):
        """ Visit a Else AST

        """
        if not indentation:
            indentation = 4*' '

        final_code = f"else:"
        for scope in node.scope:
            final_code += "\n"
            final_code += f"{indentation}{self.visit(scope, indentation*2)}"

        return final_code

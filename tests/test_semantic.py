
import unittest
from lexer import Lexer
from parser import Parser
from semantic_analyzer import SemanticAnalyzer


def analyze_code(code):
    tokens = Lexer(code).tokenize()
    ast = Parser(tokens).parse()
    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)


class TestSemanticAnalyzer(unittest.TestCase):

    def test_valid_program(self):
        code = "int main() { int x = 5; x = x + 2; return x; }"
        analyze_code(code)

    def test_undeclared_variable_usage(self):
        code = "int main() { return y; }"
        with self.assertRaisesRegex(Exception, "used before declaration"):
            analyze_code(code)

    def test_undeclared_variable_in_initializer(self):
        code = "int main() { int x = y; return x; }"
        with self.assertRaisesRegex(Exception, "used before declaration"):
            analyze_code(code)

    def test_assignment_to_undeclared_variable(self):
        code = "int main() { x = 5; return 0; }"
        with self.assertRaisesRegex(Exception, "not declared before assignment"):
            analyze_code(code)

    def test_duplicate_declaration(self):
        code = "int main() { int x; int x; return 0; }"
        with self.assertRaisesRegex(Exception, "already declared"):
            analyze_code(code)


if __name__ == "__main__":
    unittest.main()

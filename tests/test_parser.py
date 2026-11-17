import unittest
from lexer import Lexer
from parser import Parser


def parse_code(code):
    tokens = Lexer(code).tokenize()
    parser = Parser(tokens)
    return parser.parse()


class TestParser(unittest.TestCase):

    def test_valid_function(self):
        ast = parse_code("int main() { return 10; }")
        self.assertEqual(ast.label, "Program")
        self.assertEqual(ast.children[0].label, "Function(main)")

    def test_variable_declaration(self):
        ast = parse_code("int main() { int x; return x; }")
        self.assertEqual(ast.children[0].children[0].label, "VarDecl")

    def test_assignment(self):
        ast = parse_code("int main() { int x; x = 5; return x; }")
        self.assertEqual(ast.children[0].children[1].label, "Assign")

    def test_if_else_statement(self):
        ast = parse_code(
            "int main() { int x; if (x > 0) { return 1; } else { return 0; } }"
        )
        self.assertEqual(ast.children[0].children[1].label, "If")

    def test_invalid_function(self):
        with self.assertRaises(SyntaxError):
            parse_code("int main( { return 10; }")


if __name__ == "__main__":
    unittest.main()

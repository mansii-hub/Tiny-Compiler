import unittest
from lexer import Lexer


class TestLexer(unittest.TestCase):

    def test_keywords(self):
        tokens = Lexer("int return if else").tokenize()
        self.assertEqual(
            [(t.type, t.value) for t in tokens],
            [
                ("KEYWORD", "int"),
                ("KEYWORD", "return"),
                ("KEYWORD", "if"),
                ("KEYWORD", "else")
            ]
        )

    def test_identifiers(self):
        tokens = Lexer("main my_variable count1").tokenize()
        self.assertEqual(
            [(t.type, t.value) for t in tokens],
            [
                ("ID", "main"),
                ("ID", "my_variable"),
                ("ID", "count1")
            ]
        )

    def test_numbers(self):
        tokens = Lexer("123 45.67").tokenize()
        self.assertEqual(
            [(t.type, t.value) for t in tokens],
            [
                ("NUMBER", "123"),
                ("NUMBER", "45.67")
            ]
        )

    def test_operators(self):
        tokens = Lexer("+ - * / == != >= <= && ||").tokenize()
        self.assertEqual(
            [t.value for t in tokens],
            ["+", "-", "*", "/", "==", "!=", ">=", "<=", "&&", "||"]
        )

    def test_invalid_character(self):
        with self.assertRaises(SyntaxError):
            Lexer("int @ value;").tokenize()


if __name__ == "__main__":
    unittest.main()

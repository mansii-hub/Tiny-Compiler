
import unittest
from codegen import CodeGenerator


class TestCodeGenerator(unittest.TestCase):

    def test_assignment(self):
        tac = ["x = 10"]
        expected = ["MOV x, 10"]
        self.assertEqual(CodeGenerator(tac).generate(), expected)

    def test_addition(self):
        tac = ["t1 = a + b"]
        expected = [
            "MOV R1, a",
            "ADD R1, b",
            "MOV t1, R1"
        ]
        self.assertEqual(CodeGenerator(tac).generate(), expected)

    def test_comparison(self):
        tac = ["t1 = a > b"]
        expected = [
            "MOV R1, a",
            "CMP R1, b",
            "SETG t1"
        ]
        self.assertEqual(CodeGenerator(tac).generate(), expected)

    def test_conditional_jump(self):
        tac = ["IF NOT t1 GOTO L1"]
        expected = [
            "MOV R1, t1",
            "CMP R1, 0",
            "JE L1"
        ]
        self.assertEqual(CodeGenerator(tac).generate(), expected)

    def test_return(self):
        tac = ["RETURN x"]
        expected = [
            "MOV R0, x",
            "RET"
        ]
        self.assertEqual(CodeGenerator(tac).generate(), expected)


if __name__ == "__main__":
    unittest.main()


import unittest
from intermediate import TACGenerator
from parser import ASTNode


class TestTACGenerator(unittest.TestCase):

    def test_new_temp(self):
        generator = TACGenerator()
        self.assertEqual(generator.new_temp(), "t1")
        self.assertEqual(generator.new_temp(), "t2")

    def test_new_label(self):
        generator = TACGenerator()
        self.assertEqual(generator.new_label(), "L1")
        self.assertEqual(generator.new_label(), "L2")

    def test_arithmetic_expression(self):
        generator = TACGenerator()

        expression = ASTNode(
            "Op(+)",
            [ASTNode("Number(5)"), ASTNode("Number(3)")]
        )

        result = generator.generate(expression)

        self.assertEqual(result, "t1")
        self.assertEqual(generator.code, ["t1 = 5 + 3"])

    def test_variable_assignment(self):
        generator = TACGenerator()

        assignment = ASTNode(
            "Assign",
            [ASTNode("x"), ASTNode("Number(10)")]
        )

        generator.generate(assignment)

        self.assertEqual(generator.code, ["x = 10"])

    def test_return_statement(self):
        generator = TACGenerator()

        return_node = ASTNode(
            "Return",
            [ASTNode("Number(5)")]
        )

        generator.generate(return_node)

        self.assertEqual(generator.code, ["RETURN 5"])


if __name__ == "__main__":
    unittest.main()

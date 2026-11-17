
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

    def test_if_else_statement(self):
        generator = TACGenerator()

        condition = ASTNode("Condition", [ASTNode("Number(1)")])
        then_body = ASTNode("Then", [
            ASTNode("Assign", [ASTNode("x"), ASTNode("Number(10)")])
        ])
        else_body = ASTNode("Else", [
            ASTNode("Assign", [ASTNode("x"), ASTNode("Number(20)")])
        ])

        if_node = ASTNode("If", [condition, then_body, else_body])

        generator.generate(if_node)

        self.assertIn("IF NOT 1 GOTO L1", generator.code)
        self.assertIn("GOTO L2", generator.code)
        self.assertIn("L1:", generator.code)
        self.assertIn("x = 10", generator.code)
        self.assertIn("x = 20", generator.code)
        self.assertIn("L2:", generator.code)

    def test_while_loop(self):
        generator = TACGenerator()

        condition = ASTNode(
            "Condition",
            [ASTNode("Op(<)", [
                ASTNode("Var(x)"),
                ASTNode("Number(5)")
            ])]
        )

        body = ASTNode("Body", [
            ASTNode("Assign", [
                ASTNode("x"),
                ASTNode("Number(10)")
            ])
        ])

        while_node = ASTNode("While", [condition, body])

        generator.generate(while_node)

        self.assertIn("L1:", generator.code)
        self.assertIn("t1 = x < 5", generator.code)
        self.assertIn("IF NOT t1 GOTO L2", generator.code)
        self.assertIn("x = 10", generator.code)
        self.assertIn("GOTO L1", generator.code)
        self.assertIn("L2:", generator.code)

    def test_for_loop(self):
        generator = TACGenerator()

        init = ASTNode(
            "Assign",
            [ASTNode("i"), ASTNode("Number(0)")]
        )

        condition = ASTNode(
            "Condition",
            [ASTNode("Op(<)", [
                ASTNode("Var(i)"),
                ASTNode("Number(3)")
            ])]
        )

        update = ASTNode(
            "Assign",
            [ASTNode("i"), ASTNode("Op(+)", [
                ASTNode("Var(i)"),
                ASTNode("Number(1)")
            ])]
        )

        body = ASTNode("Body", [
            ASTNode("Assign", [
                ASTNode("x"),
                ASTNode("Number(1)")
            ])
        ])

        for_node = ASTNode(
            "For",
            [init, condition, update, body]
        )

        generator.generate(for_node)

        self.assertIn("i = 0", generator.code)
        self.assertIn("L1:", generator.code)
        self.assertIn("t1 = i < 3", generator.code)
        self.assertIn("IF NOT t1 GOTO L2", generator.code)
        self.assertIn("x = 1", generator.code)
        self.assertIn("L3:", generator.code)
        self.assertIn("t2 = i + 1", generator.code)
        self.assertIn("i = t2", generator.code)
        self.assertIn("GOTO L1", generator.code)
        self.assertIn("L2:", generator.code)

    def test_break_statement(self):
        generator = TACGenerator()

        break_node = ASTNode("Break")
        generator.break_stack.append("L1")

        generator.generate(break_node)

        self.assertEqual(generator.code, ["GOTO L1"])

    def test_continue_statement(self):
        generator = TACGenerator()

        continue_node = ASTNode("Continue")
        generator.continue_stack.append("L2")

        generator.generate(continue_node)

        self.assertEqual(generator.code, ["GOTO L2"])


if __name__ == "__main__":
    unittest.main()

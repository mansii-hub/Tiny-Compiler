
import unittest
from optimizer import Optimizer


class TestOptimizer(unittest.TestCase):

    def test_constant_folding_addition(self):
        code = ["t1 = 5 + 3", "RETURN t1"]
        expected = ["t1 = 8  # constant folded", "RETURN t1"]
        self.assertEqual(Optimizer(code).optimize(), expected)

    def test_constant_folding_subtraction(self):
        optimizer = Optimizer([])
        result = optimizer.constant_folding("t1 = 10 - 4")
        self.assertEqual(result, "t1 = 6  # constant folded")

    def test_constant_folding_multiplication(self):
        optimizer = Optimizer([])
        result = optimizer.constant_folding("t1 = 5 * 4")
        self.assertEqual(result, "t1 = 20  # constant folded")

    def test_division_by_zero(self):
        optimizer = Optimizer([])
        result = optimizer.constant_folding("t1 = 10 / 0")
        self.assertEqual(result, "t1 = 10 / 0")

    def test_dead_code_elimination(self):
        code = [
            "t1 = 5 + 3",
            "t2 = 10 + 2",
            "RETURN t1"
        ]
        expected = [
            "t1 = 8  # constant folded",
            "RETURN t1"
        ]
        self.assertEqual(Optimizer(code).optimize(), expected)


if __name__ == "__main__":
    unittest.main()

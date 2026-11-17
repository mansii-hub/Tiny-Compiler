import re
import operator

class Optimizer:
    def __init__(self, code_lines):
        self.code = code_lines
        self.optimized_code = []

    def constant_folding(self, line):
        match = re.match(r"\s*(t\d+)\s*=\s*(-?\d+)\s*([+\-*/])\s*(-?\d+)\s*$", line)
        if not match:
            return line
        target, lhs, op, rhs = match.groups()
        lhs, rhs = int(lhs), int(rhs)
        operations = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
        if op == "/" and rhs == 0:
            return line
        return f"{target} = {operations[op](lhs, rhs)}  # constant folded"

    def dead_code_elimination(self):
        used_vars = set()
        for line in self.code:
            line = line.strip()
            if not line or line.startswith("#") or line.endswith(":"):
                continue
            assignment = re.match(r"(\w+)\s*=\s*(.*)$", line)
            if assignment:
                expression = assignment.group(2)
                used_vars.update(re.findall(r"\bt\d+\b", expression))
            elif line.startswith(("RETURN", "IF", "GOTO")):
                used_vars.update(re.findall(r"\bt\d+\b", line))
        new_code = []
        for line in self.code:
            assignment = re.match(r"\s*(t\d+)\s*=", line)
            if assignment and assignment.group(1) not in used_vars:
                continue
            new_code.append(line)
        self.code = new_code

    def optimize(self):
        self.code = [self.constant_folding(line) for line in self.code]
        self.dead_code_elimination()
        self.optimized_code = self.code
        return self.optimized_code

if __name__ == "__main__":
    print("Run the compiler using: python main.py")

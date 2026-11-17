import re

class CodeGenerator:
    def __init__(self, tac_lines):
        self.tac = tac_lines
        self.asm = []

    def generate(self):
        self.asm = []

        for line in self.tac:
            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                self.asm.append(f"; {line[1:].strip()}")
                continue

            if line.endswith(":"):
                self.asm.append(line)
                continue

            match = re.fullmatch(r"IF NOT (\w+) GOTO (L\d+)", line)
            if match:
                cond, label = match.groups()
                self.asm.extend([f"MOV R1, {cond}", "CMP R1, 0", f"JE {label}"])
                continue

            match = re.fullmatch(r"GOTO (L\d+)", line)
            if match:
                self.asm.append(f"JMP {match.group(1)}")
                continue

            match = re.fullmatch(r"RETURN (\w+)", line)
            if match:
                self.asm.extend([f"MOV R0, {match.group(1)}", "RET"])
                continue

            match = re.fullmatch(r"(\w+)\s*=\s*(\w+)\s*(==|!=|>=|<=|>|<|[+*/%\-])\s*(\w+)", line)
            if match:
                dest, left, op, right = match.groups()
                self.asm.append(f"MOV R1, {left}")

                if op in {"+", "-", "*", "/", "%"}:
                    instruction = {
                        "+": "ADD", "-": "SUB", "*": "MUL",
                        "/": "DIV", "%": "MOD"
                    }[op]
                    self.asm.extend([
                        f"{instruction} R1, {right}",
                        f"MOV {dest}, R1"
                    ])
                else:
                    condition = {
                        "==": "E", "!=": "NE", ">": "G",
                        "<": "L", ">=": "GE", "<=": "LE"
                    }[op]
                    self.asm.extend([
                        f"CMP R1, {right}",
                        f"SET{condition} {dest}"
                    ])
                continue

            match = re.fullmatch(r"(\w+)\s*=\s*(\w+)", line)
            if match:
                dest, src = match.groups()
                self.asm.append(f"MOV {dest}, {src}")
                continue

            self.asm.append(f"; Unrecognized TAC: {line}")

        return self.asm

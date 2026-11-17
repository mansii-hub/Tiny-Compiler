
# Tiny Compiler

A Python-based mini compiler that demonstrates the major phases of compilation using a simplified C-like language.

## Overview

The project processes source code through lexical analysis, syntax analysis, semantic analysis, intermediate code generation, optimization, and pseudo-assembly generation.

## Compilation Workflow

1. Lexical Analysis – Converts source code into tokens.
2. Syntax Analysis – Builds an Abstract Syntax Tree (AST).
3. Semantic Analysis – Performs semantic checks.
4. Intermediate Code Generation – Generates Three Address Code (TAC).
5. Code Optimization – Applies constant folding and basic dead-code elimination.
6. Target Code Generation – Generates illustrative pseudo-assembly.
7. Simulation – Simulates the return value using the original TAC.

## Features

- Tokenization of keywords, identifiers, numbers and operators.
- AST construction.
- Variable declarations and assignments.
- Conditional statements (`if` and `else`).
- `while` and `for` loops.
- `break` and `continue`.
- Arithmetic and comparison expressions.
- Three Address Code generation.
- Basic code optimization.
- Pseudo-assembly generation.
- TAC return-value simulation.

## Technologies Used

- Python
- Regular Expressions
- Flask
- Flask-CORS
- Streamlit

## Project Structure

```text
Tiny-Compiler/
├── api.py
├── app.py
├── codegen.py
├── intermediate.py
├── lexer.py
├── main.py
├── optimizer.py
├── parser.py
├── semantic_analyzer.py
├── simulator.py
├── test.c
├── test1.c
├── ast_tree
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/mansii-hub/Tiny-Compiler.git
cd Tiny-Compiler
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Compiler

```bash
python main.py
```

The compiler reads the source program from `test.c` and displays the output of each compilation phase.

## Sample Tests

- `test.c` – Nested conditional statements. The simulator produced a return value of `2`.
- `test1.c` – A loop using conditions, `break`, and `continue`. The simulator produced a return value of `16`.

## Limitations

- Supports a subset of C-like syntax, not the complete C language.
- Generated target instructions are illustrative pseudo-assembly, not verified machine code.
- Generated pseudo-assembly is not executed by a real processor or assembler.
- The simulator evaluates original TAC rather than generated pseudo-assembly.
- Optimization and language support are basic and need further testing.

## Future Improvements

- Add automated unit tests.
- Improve semantic analysis and error handling.
- Expand optimization techniques.
- Improve target-code generation and execution support.

## Project Team

This project was developed as a group project for the **Compiler Design** subject.

- Ritin Gusain
- Ankita Negi
- Saloni Rawat
- Mansi Gusain



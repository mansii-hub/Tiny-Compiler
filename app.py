import streamlit as st
import io
import sys
import traceback

from lexer import Lexer
from parser import Parser, print_ast_tree
from semantic_analyzer import SemanticAnalyzer
from intermediate import TACGenerator
from optimizer import Optimizer
from codegen import CodeGenerator
from simulator import simulate_return

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="Tiny Compiler",
    layout="wide"
)

st.title("🧠 Tiny Compiler – Streamlit GUI")
st.write("Lexical → Syntax → Semantic → TAC → Optimization → CodeGen → Simulation")

# -----------------------------
# Source Code Input
# -----------------------------
source_code = st.text_area(
    "✍️ Enter Tiny/C-like Source Code",
    height=300,
    placeholder="int main() {\n  int x;\n  x = 2 + 3;\n  return x;\n}"
)

compile_btn = st.button("🚀 Compile")

# -----------------------------
# Compile Logic
# -----------------------------
if compile_btn:
    if not source_code.strip():
        st.warning("Please enter some source code.")
    else:
        try:
            output = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = output

            # -------- PHASE 1 --------
            print("PHASE 1: Lexical Analysis")
            lexer = Lexer(source_code)
            tokens = lexer.tokenize()
            for token in tokens:
                print(f"{token.type}: {token.value}")

            # -------- PHASE 2 --------
            print("\nPHASE 2: Syntax Analysis / AST")
            parser = Parser(tokens)
            ast = parser.parse()
            print_ast_tree(ast)

            # -------- PHASE 3 --------
            print("\nPHASE 3: Semantic Analysis")
            analyzer = SemanticAnalyzer()
            analyzer.analyze(ast)
            print("Semantic Analysis: PASSED")

            # -------- PHASE 4 --------
            print("\nPHASE 4: Intermediate Code (TAC)")
            tacgen = TACGenerator()
            tac_code = tacgen.generate(ast)
            for line in tac_code:
                print(line)

            # -------- PHASE 5 --------
            print("\nPHASE 5: Optimization")
            optimizer = Optimizer(tac_code)
            optimized_code = optimizer.optimize()
            for line in optimized_code:
                print(line)

            # -------- PHASE 6 --------
            print("\nPHASE 6: Code Generation (Assembly)")
            codegen = CodeGenerator(optimized_code)
            asm_code = codegen.generate()
            for line in asm_code:
                print(line)

            # -------- PHASE 7 --------
            print("\nPHASE 7: Simulation")
            simulate_return(tac_code)

            sys.stdout = old_stdout
            full_output = output.getvalue()

            # -----------------------------
            # Output UI
            # -----------------------------
            st.success("Compilation Successful ✅")

            tabs = st.tabs([
                "🔤 Lexer",
                "🌳 AST",
                "🧠 Semantic",
                "⚙️ TAC",
                "✨ Optimized TAC",
                "🧾 Assembly",
                "▶️ Full Output"
            ])

            with tabs[0]:
                st.code(
                    "\n".join([f"{t.type}: {t.value}" for t in tokens]),
                    language="text"
                )

            with tabs[1]:
                ast_out = io.StringIO()
                sys.stdout = ast_out
                print_ast_tree(ast)
                sys.stdout = old_stdout
                st.code(ast_out.getvalue(), language="text")

            with tabs[2]:
                st.write("Semantic Analysis: ✅ PASSED")

            with tabs[3]:
                st.code("\n".join(tac_code), language="text")

            with tabs[4]:
                st.code("\n".join(optimized_code), language="text")

            with tabs[5]:
                st.code("\n".join(asm_code), language="asm")

            with tabs[6]:
                st.code(full_output, language="text")

        except Exception as e:
            sys.stdout = old_stdout
            st.error("❌ Compilation Failed")
            st.code(traceback.format_exc())

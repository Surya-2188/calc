import streamlit as st
import numpy as np
import math

# Title and description
st.title("Scientific Calculator - Casio FX-991EX Equivalent")
st.markdown("A fully functional scientific calculator with features inspired by the Casio FX-991EX ClassWiz.")

# Input area
expression = st.text_input("Enter your expression (e.g., sin(45), log10(100), 5^2 + 3*4):")

# Buttons for predefined operations
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Trigonometry"):
        st.markdown("- `sin(x)`: Sine of x (degrees)")
        st.markdown("- `cos(x)`: Cosine of x (degrees)")
        st.markdown("- `tan(x)`: Tangent of x (degrees)")
with col2:
    if st.button("Logarithms"):
        st.markdown("- `log10(x)`: Base 10 logarithm of x")
        st.markdown("- `ln(x)`: Natural logarithm of x")
        st.markdown("- `e^x`: Exponential of x")
with col3:
    if st.button("Matrices"):
        st.markdown("Perform matrix calculations under the **Matrix Operations** section below.")

# Evaluate the expression
if expression:
    try:
        # Convert to degrees for trigonometry by default
        expression = expression.replace("sin", "np.sin(np.radians")
        expression = expression.replace("cos", "np.cos(np.radians")
        expression = expression.replace("tan", "np.tan(np.radians")
        expression = expression.replace("log10", "np.log10")
        expression = expression.replace("ln", "np.log")
        result = eval(expression)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

# Advanced options: Factorial, combinations, permutations
st.markdown("### Advanced Operations")
n = st.number_input("Enter a number (for factorial, permutations, combinations):", min_value=0, step=1)
r = st.number_input("Enter r (for combinations/permutations):", min_value=0, step=1)

adv_col1, adv_col2, adv_col3 = st.columns(3)
with adv_col1:
    if st.button("Factorial"):
        try:
            st.write(f"Factorial of {n}: {math.factorial(int(n))}")
        except Exception as e:
            st.error(f"Error: {e}")
with adv_col2:
    if st.button("Permutation"):
        try:
            st.write(f"Permutation P({n}, {r}): {math.perm(int(n), int(r))}")
        except Exception as e:
            st.error(f"Error: {e}")
with adv_col3:
    if st.button("Combination"):
        try:
            st.write(f"Combination C({n}, {r}): {math.comb(int(n), int(r))}")
        except Exception as e:
            st.error(f"Error: {e}")

# Matrix operations
st.markdown("### Matrix Operations")
matrix_ops = st.selectbox("Choose a matrix operation:", ["None", "Addition", "Multiplication", "Determinant", "Inverse"])

if matrix_ops != "None":
    matrix_a = st.text_area("Enter Matrix A (comma-separated rows, e.g., '1,2;3,4'):")
    matrix_b = st.text_area("Enter Matrix B (if applicable):")

    try:
        if matrix_a:
            mat_a = np.array([list(map(float, row.strip().split(','))) for row in matrix_a.strip().split(';')])
        if matrix_b:
            mat_b = np.array([list(map(float, row.strip().split(','))) for row in matrix_b.strip().split(';')])

        if matrix_ops == "Addition":
            st.write("Result (A + B):")
            st.write(mat_a + mat_b)
        elif matrix_ops == "Multiplication":
            st.write("Result (A * B):")
            st.write(np.dot(mat_a, mat_b))
        elif matrix_ops == "Determinant":
            st.write("Determinant of A:")
            st.write(np.linalg.det(mat_a))
        elif matrix_ops == "Inverse":
            st.write("Inverse of A:")
            st.write(np.linalg.inv(mat_a))
    except Exception as e:
        st.error(f"Matrix error: {e}")

# Footer
st.markdown("---")
st.markdown("**Note:** This app is for educational purposes and may have limitations compared to a physical Casio FX-991EX calculator.")

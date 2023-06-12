import streamlit as st
import numpy as np

def gauss_jordan_elimination(matrix):
    row, col = matrix.shape
    for i in range(row):
        if matrix[i, i] == 0:
            st.warning("Pivot element is zero. Matrix is not invertible.")
            return None
        matrix[i, :] /= matrix[i, i]
        for j in range(row):
            if i != j:
                matrix[j, :] -= matrix[j, i] * matrix[i, :]
    return matrix

def create_matrix(order):
    matrix = []
    for i in range(order):
        row = []
        for j in range(order):
            row.append(st.number_input(f"Enter element at position ({i}, {j}):"))
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix):
    for row in matrix:
        st.write(row)

def main():
    st.title("Gauss-Jordan Matrix Elimination")
    order = st.selectbox("Select matrix order:", (2, 3))

    st.write("Matrix A:")
    matrix_a = create_matrix(order)
    display_matrix(matrix_a)

    if st.button("Eliminate"):
        result = gauss_jordan_elimination(matrix_a)
        if result is not None:
            st.write("Resultant Matrix:")
            display_matrix(result)

if __name__ == '__main__':
    main()

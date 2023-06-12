import streamlit as st
import numpy as np

def matrix_normalization(matrix):
    max_value = np.max(matrix)
    min_value = np.min(matrix)
    normalized_matrix = (matrix - min_value) / (max_value - min_value)
    return normalized_matrix

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
    st.title("Matrix Normalization")
    order = st.selectbox("Select matrix order:", (2, 3))

    st.write("Matrix A:")
    matrix_a = create_matrix(order)
    display_matrix(matrix_a)

    if st.button("Normalize"):
        result = matrix_normalization(matrix_a)
        st.write("Normalized Matrix:")
        display_matrix(result)

if __name__ == '__main__':
    main()

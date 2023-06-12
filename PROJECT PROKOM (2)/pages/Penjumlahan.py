import streamlit as st
import numpy as np

def matrix_addition(a, b):
    return np.add(a, b)

def create_matrix(order):
    matrix = []
    for i in range(order):
        row = []
        for j in range(order):
            key = f"element_{i}_{j}"
            row.append(st.number_input(f"Enter element at position ({i}, {j}):", key=key))
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix):
    for row in matrix:
        st.write(row)

def main():
    st.title("Matrix Addition")
    order = st.selectbox("Select matrix order:", (2, 3))

    st.write("Matrix A:")
    matrix_a = create_matrix(order)
    display_matrix(matrix_a)

    st.write("Matrix B:")
    matrix_b = create_matrix(order)
    display_matrix(matrix_b)

    if st.button("Add"):
        result = matrix_addition(matrix_a, matrix_b)
        st.write("Resultant Matrix:")
        display_matrix(result)

if __name__ == '__main__':
    main()

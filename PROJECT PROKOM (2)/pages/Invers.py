import streamlit as st
import numpy as np

def matrix_inverse(matrix):
    try:
        inverse = np.linalg.inv(matrix)
        return inverse
    except np.linalg.LinAlgError:
        st.error("Matrix is not invertible.")

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
    st.title("Matrix Inverse")
    order = st.selectbox("Select matrix order:", (2, 3))

    st.write("Matrix A:")
    matrix_a = create_matrix(order)
    display_matrix(matrix_a)

    if st.button("Calculate Inverse"):
        result = matrix_inverse(matrix_a)
        if result is not None:
            st.write("Inverse Matrix:")
            display_matrix(result)

if __name__ == '__main__':
    main()

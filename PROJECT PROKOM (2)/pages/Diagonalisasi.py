import streamlit as st
import numpy as np

def matrix_diagonalization(matrix):
    try:
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        diagonal_matrix = np.diag(eigenvalues)
        diagonal_matrix = np.round(diagonal_matrix, decimals=2)
        return eigenvectors, diagonal_matrix
    except np.linalg.LinAlgError:
        st.error("Matrix is not diagonalizable.")

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
    st.title("Matrix Diagonalization")
    order = st.selectbox("Select matrix order:", (2, 3))

    st.write("Matrix A:")
    matrix_a = create_matrix(order)
    display_matrix(matrix_a)

    if st.button("Diagonalize"):
        eigenvectors, diagonal_matrix = matrix_diagonalization(matrix_a)
        if eigenvectors is not None and diagonal_matrix is not None:
            st.write("Eigenvalues:")
            st.write(np.round(eigenvectors, decimals=2))
            st.write("Diagonal Matrix:")
            display_matrix(diagonal_matrix)

if __name__ == '__main__':
    main()

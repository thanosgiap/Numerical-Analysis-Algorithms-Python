from math import sqrt
import numpy as np


def luDecomposition():
    # Function multiplying two matrices
    def matrixMultiplication(A, B):
        res = np.dot(A, B)
        return res

    # Function that creates the right pivoting matrix based on the argument
    def pivotize(m):
        n = len(m)
        identityMatrix = [[float(i == j) for i in range(n)] for j in range(n)]
        for j in range(n):
            row = m.index(max(m))
            if j != row:
                temp = identityMatrix[j]
                identityMatrix[j] = identityMatrix[row]
                identityMatrix[row] = temp
        return identityMatrix

    def gauss(A, b):
        rows, columns = np.shape(A)

        # Initialization with zero's
        L = np.zeros((rows, columns))
        U = np.zeros((rows, columns))

        if rows != columns:
            print("Matrix needs to be squared")
            return

        P = pivotize(A)
        A2 = matrixMultiplication(P, A)

        # Creating the two matrices L and U
        for j in range(columns):
            L[j][j] = 1.0
            for i in range(j + 1):
                s1 = sum(U[k][j] * L[i][k] for k in range(i))
                U[i][j] = A2[i][j] - s1

            for i in range(j, columns):
                s2 = sum(U[k][j] * L[i][k] for k in range(j))
                L[i][j] = (A2[i][j] - s2) / U[j][j]

        n = len(L)
        y = np.zeros(n)
        # Multiplying matrix b with the pivoting matrix P
        b1 = matrixMultiplication(P, b)

        # Forward substitution, solving Ly = b.
        for i in range(0, n, 1):
            temp = b1[i]
            for k in range(0, i, 1):
                temp -= y[k] * L[i][k]
            y[i] = temp / L[i][i]

        # Backward substitution, solving Ux = y
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            temp = y[i]
            for k in range(n - 1, i, -1):
                temp -= x[k] * U[i][k]
            x[i] = temp / U[i][i]

        return x

    # Manual insertion of the two matrices A, b
    A = [[-1, 0, 1], [2, 2, 1], [-1, 2, 0]]
    b = [-2, 17, 0]
    x = gauss(A, b)
    print("x: ")
    print(x)


def choleskyDecomposition():
    def cholesky(A):
        n = len(A)
        rows, columns = np.shape(A)
        L = np.zeros((rows, columns))

        for i in range(n):
            for k in range(i + 1):
                tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))

                if (i == k):
                    L[i][k] = sqrt(A[i][i] - tmp_sum)
                else:
                    L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
        return L

    A = [[3, 4, 3], [4, 8, 6], [3, 6, 9]]
    L = cholesky(A)

    print("L:")
    print(L)


def gaussSeidelMethod(n):
    iterator = 0
    np.set_printoptions(precision=5)
    A = np.zeros((n, n))
    b = np.zeros(n)
    x = np.zeros(n)

    # Filling the matrix according to n argument.
    def matrixFill():
        for i in range(n):
            for j in range(n):
                if (i == j):
                    A[i][j] = 5
                elif (i + 1 == j or i == j + 1):
                    A[i][j] = -2
                else:
                    A[i][j] = 0
            if i == 0 or i == n - 1:
                b[i] = 3
            else:
                b[i] = 1

    matrixFill()
    # Creating a temporary copy of the previous solution
    temp = x.copy()
    while (True):
        for i in range(n):
            s1 = 0
            temp = x.copy()
            for j in range(n):
                if i != j:
                    s1 += x[j] * A[i][j]
            x[i] = (b[i] - s1) / A[i][i]

        iterator += 1
        # Calculating the infinite norm of matrices x and temp.
        # Checking if the solution found is acceptable based on the infinite norm
        if (abs(np.amax(x, axis=0)) - abs(np.amax(temp, axis=0)) < 0.000005):
            print("x:")
            print(np.array([x]).T)
            break


def main():
    print("System solution using PA=LU.")
    luDecomposition()
    print()
    print("System decomposition using Cholesky method.")
    choleskyDecomposition()
    print()
    print("System solution using the iterative method Gauss-Seidel.")
    gaussSeidelMethod(10)


if __name__ == "__main__":
    main()

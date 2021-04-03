import numpy as np


def googleMatrixCreation():
    q = 0.15
    n = 15
    G = np.zeros((n, n))
    np.set_printoptions(precision=5)

    A = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
                  ])

    columnSum = A.sum(axis=1)
    for i in range(n):
        for j in range(n):
            G[i][j] = q / n + (A[j][i] * (1 - q)) / columnSum[j]

    return G, n


def powerMethod():
    G, n = googleMatrixCreation()
    x0 = np.empty(n)
    x0.fill(1)
    for i in range(50):
        # Matrix Multiplication
        x1 = np.dot(G, x0)
        x1Norm = abs(max(x1))
        x0 = x1 / x1Norm

    # Normalization of the vector x0.
    p = x0 / abs(sum(x0))
    print("Eigenvector p:")
    print(np.array([p]).T)


def main():
    googleMatrixCreation()
    powerMethod()


if __name__ == "__main__":
    main()

def mat_mul (A, B):
    nlinhasA, ncolA = len(A), len(A[0])
    nlinhasB, ncolB = len(B), len(B[0])
    assert ncolA == nlinhasB

    C = []
    for linha in range(nlinhasA):
        C.append([])
        for coluna in range(ncolB):
            C[linha].append(0)
            for k in range(ncolA):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C
            
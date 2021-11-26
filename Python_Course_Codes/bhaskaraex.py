import math
valorA = float(input("Insira o valor do a da sua equação: "))
valorB = float(input("Insira o valor do b da sua equação: "))
valorC = float(input("Insira o valor do c da sua equação: "))

Delta = (valorB ** 2) - (4 * valorA * valorC)

if Delta < 0:
    print("esta equação não possui raízes reais")
else:
    if Delta == 0:
        raizunica = (- valorB) / (2 * valorA)
        print("a raiz desta equação é",raizunica)
    else:
        raizum = ((- valorB) - (math.sqrt(Delta))) / (2 * valorA)
        raizdois = ((- valorB) + (math.sqrt(Delta))) / (2 * valorA)
        if raizum < raizdois:
            print("as raízes da equação são",raizum,"e",raizdois)
        else:
            print("as raízes da equação são",raizdois,"e",raizum)


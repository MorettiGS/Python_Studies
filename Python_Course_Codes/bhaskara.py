import math
print("Encontrarei as raízes reais de uma equação de segundo grau.")
valorA = float(input("Insira o valor do a da sua equação: "))
valorB = float(input("Insira o valor do b da sua equação: "))
valorC = float(input("Insira o valor do c da sua equação: "))

Delta = (valorB ** 2) - (4 * valorA * valorC)

if Delta < 0:
    print("Essa equação não possui raízes reais.")
    print("Obrigado pela preferência! :)")
else:
    if Delta == 0:
        raizunica = (- valorB) / (2 * valorA)
        print("A raiz dessa equação é:",raizunica,".")
        print("Obrigado pela preferência! :)")
    else:
        raizum = ((- valorB) - (math.sqrt(Delta))) / (2 * valorA)
        raizdois = ((- valorB) + (math.sqrt(Delta))) / (2 * valorA)
        print("As raízes dessa equação são",raizum,"e",raizdois,".")
        print("Obrigado pela preferência! :)")


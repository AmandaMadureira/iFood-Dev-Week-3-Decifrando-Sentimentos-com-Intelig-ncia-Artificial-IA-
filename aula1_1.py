import pandas as pd

def calcular_nps(notas):
    detratores = 0
    promotores = 0

    for nota in notas:
        if nota >= 9:
            promotores += 1
    
        elif nota <= 6:
            detratores += 1

    nps = (promotores - detratores) / len(notas) * 100
    return nps


dados = pd.read_csv("dados.csv", delimiter=";")

notas = dados["nota"]

print(calcular_nps(notas))

#print(f"Promotores: {promotores}")
#print(f"Detratores: {detratores}")
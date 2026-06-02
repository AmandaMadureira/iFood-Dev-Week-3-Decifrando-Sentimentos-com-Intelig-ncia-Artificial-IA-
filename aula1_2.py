import pandas as pd

class Feedback:
    def __init__(self, nota, comentario):
        self.nota = nota
        self.comentario = comentario

class AnalisadorFeedback:
    def __init__(self, feedbacks):
        self.feedbacks = feedbacks

    def calcular_nps(self):
        detratores = sum ([1 for feedback in self.feedbacks if feedback.nota <= 6])
        promotores = sum ([1 for feedback in self.feedbacks if feedback.nota >= 9])

        return (promotores - detratores) / len(self.feedbacks) * 100

dados = pd.read_csv("dados.csv", delimiter=";")

feedbacks = [Feedback(linha["nota"], linha["comentario"]) for indice, linha in dados.iterrows()]


analisador = AnalisadorFeedback(feedbacks)
nps = analisador.calcular_nps()

print(nps)

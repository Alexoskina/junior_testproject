import numpy as np

def check(envelop_x, envelop_y, paper_x, paper_y):

    envelop = np.array([envelop_x, envelop_y])
    paper = np.array([paper_x, paper_y])
    return all(np.sort(envelop) >= np.sort(paper))

# Пример использования функции
envelop_x = float(input("Введи ширину конверта: "))
envelop_y = float(input("Введи высоту конверта: "))
paper_x = float(input("Введи ширину листа бумаги: "))
paper_y = float(input("Введи высоту листа бумаги: "))

result = check(envelop_x, envelop_y, paper_x, paper_y)
print(result)
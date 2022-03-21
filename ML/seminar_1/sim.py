import numpy as np
import re
import scipy
from scipy.spatial import distance


# Задание: Дан набор предложений, каждое из которых содержит слово "lead" в разных значениях.
# Необходимо с помощью косинусной близости найти 3 предложения, которые ближе всего к первому в корпусе и вывести их


def main():
    sents = open('sentences.txt').readlines()
    # 1) Привести строки к нижнему регистру
    low = []
    for sent in sents:
        low.append(sent.lower())

    # 2) Произведите токенизацию (например, с помощью регулярного выражения re.split('[^a-z]', t))
    tokens = []
    for sent in low:
        tokens.append(re.split('[^a-z]', sent))

    # 3) Составьте словарь всех уникальных слов, встречающихся в предложениях: каждому слову должен соответствовать
    #    индекс от нуля до (d - 1), где d - размер словаря.
    dict = {}
    for sent in tokens:
        for token in sent:
            dict[token] = 0

    new_dict = {}
    d = 0
    for word in dict:
        new_dict[d] = word
        d += 1

    # 4) Создайте пустую матрицу размера n x d, где n — число предложений.
    matrix = np.zeros((len(sents), len(dict)))
    shape = np.shape(matrix)

    # 5) Заполните ее: элемент с индексом (i, j) в этой матрице должен быть равен
    #    количеству вхождений j-го слова в i-е предложение.
    for i in range(len(sents)):
        for j in range(d):
            matrix[i][j] = low[i].count(new_dict[j])

    # 6) Найдите косинусное расстояние от предложения в самой первой строке до всех остальных с помощью функции scipy.spatial.distance.cosine.
    dists = {}
    for sent in range(len(low)):
        dist = scipy.spatial.distance.cosine(matrix[0], matrix[sent])
        dists[sent] = dist

    results = sorted(dists, key=dists.get, reverse=True)[:3]
    # <-- здесь необходимо вывести 3 ближайших предложения: каждое на своей строчке
    for result in results:
        print(sents[result])


if __name__ == '__main__':
    main()

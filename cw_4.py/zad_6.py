import numpy as np

def foo6():
    first_word = "malina"
    second_word = "lizak"
    third_word = "jagoda"
    third_word_3 = third_word[::-1]
    print(third_word_3)
    matrix = np.zeros((6, 6), dtype=str)
    matrix[:, 0] = np.fromiter(first_word, dtype="S1")
    matrix[5:, ::-1] = np.fromiter(third_word, dtype="S2")
    np.fill_diagonal(matrix, list(second_word))
    print(matrix)

foo6()

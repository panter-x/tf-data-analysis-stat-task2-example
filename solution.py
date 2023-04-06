import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 46951859 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    alpha = 1 - p
    loc = x.mean()
    sumq = 0
    for i in range(n):
        sumq += x[i]**2
    left = sumq / chi2.ppf((1-alpha / 2), df = 2*n)
    right = sumq / chi2.ppf((alpha / 2), df = 2*n)
    return np.sqrt(left/5) , \
           np.sqrt(right/5)

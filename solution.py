import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 257689856 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, p_value = ks_2samp(x, y)
    alpha = 0.03
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return p_value < alpha # Ваш ответ, True или False

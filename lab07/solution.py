import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    """Преобразует плоский список измерений в таблицу по width значений в строке."""
    if not values or width <= 0 or len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype=float)
    reshaped = arr.reshape((-1, width))
    return [[round(float(val), 6) for val in row] for row in reshaped]


def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    """Выбирает участок таблицы по заданным индексам строк и столбцов в нужном порядке."""
    if not matrix or not rows or not columns:
        return []
    arr = np.asarray(matrix, dtype=float)
    sub = arr[np.ix_(rows, columns)]
    return [[round(float(val), 6) for val in row] for row in sub]


def column_means(matrix: list[list[float]]) -> list[float]:
    """Вычисляет среднее арифметическое по каждому столбцу."""
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    means = np.mean(arr, axis=0)
    return [round(float(m), 6) for m in means]


def column_range(matrix: list[list[float]], column: int) -> float:
    """Вычисляет размах значений в указанном столбце (максимум минус минимум)."""
    if not matrix:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    col_data = arr[:, column]
    rng = np.ptp(col_data)  # ptp (peak-to-peak) считает разницу между max и min
    return round(float(rng), 6)
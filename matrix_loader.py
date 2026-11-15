from typing import List
import httpx

class MatrixParseError(ValueError):
    pass

def parse_matrix_text(text: str) -> List[List[int]]:
    """парсинг текстовой матрицы в двумерный список чисел """

    lines = text.strip().splitlines()
    matrix_rows: List[List[int]] = []
    
    for line in lines:
        stripped = line.strip()

        if not stripped or all(c in "+-" for c in stripped):
            continue

        if not stripped.startswith("|") or not stripped.endswith("|"):
            raise MatrixParseError(f"Некорректная строка: {line}")

        cells = [cell.strip() for cell in stripped.split("|")[1:-1]]
        try:
            row_ints = [int(cell) for cell in cells]
        except ValueError as e:
            raise MatrixParseError(f"Ошибка конвертации в число в строке: {line}")

        matrix_rows.append(row_ints)

    if not matrix_rows:
        raise MatrixParseError("Пустая матрица")

    #проверка на квадратность
    n = len(matrix_rows)
    for row in matrix_rows:
        if len(row) != n:
            raise MatrixParseError(f"Матрица не квадратная.")

    return matrix_rows

def traverse_counter_clockwise(matrix: List[List[int]]) -> List[int]:
    """Обход квадратной матрицы по спирали против часовой стрелки, начиная с левого верхнего угла (0, 0)"""

    if not matrix or not matrix[0]:
        return []

    n = len(matrix)
    top, bottom = 0, n-1
    left, right = 0, n -1
    result: List[int] = []

    while top <= bottom and left <= right:
        for row in range(top,bottom + 1):
            result.append(matrix[row][left])
        left += 1

        if left > right:
            break

        for col in range(left, right+1):
            result.append(matrix[bottom][col])
        bottom -= 1

        if top> bottom:
            break

        for row in range(bottom, top -1, -1):
            result.append(matrix[row][right])
        right -= 1

        if left > right:
            break

        for col in range(right, left -1, -1 ):
            result.append(matrix[top][col])
        top += 1

    return result
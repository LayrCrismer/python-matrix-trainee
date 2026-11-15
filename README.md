# Matrix Spiral Loader

Python-библиотека для асинхронной загрузки квадратной матрицы ($N \times N$) с удалённого сервера и обхода её элементов по спирали против часовой стрелки, начиная с левого верхнего угла.

## Исходное задание
Тестовое задание для стажёра Python-разработчика от компании **Avito Tech**:  
[avito-tech/python-trainee-assignment](https://github.com/avito-tech/python-trainee-assignment)

---

## Объём выполненных работ

### Что сделано
* Реализована асинхронная функция `get_matrix(url: str) -> List[int]` с использованием библиотеки `httpx`.
* Написан парсер текстового представления таблицы (`parse_matrix_text`), преобразующий входной текст в двумерный список целых чисел с проверкой на квадратность и корректность формата.
* Реализован алгоритм спирального обхода против часовой стрелки (`traverse_counter_clockwise`) методом послойного сужения границ матрицы.
* Добавлена обработка сетевых и серверных ошибок (`HTTPStatusError`, `TimeoutException`, `RequestError`).
* Написан автотест (`test_matrix.py`), проверяющий официальный тест-кейс из ТЗ.
* Настроена автоматическая проверка тестов при каждом коммите через **GitHub Actions**.

### Что не сделано (и почему)
* **Кеширование ответов сервера и CLI-интерфейс:** не требовались по условиям задания и выходят за рамки основного сценария в рамках отведённого времени (6–8 часов).
* **Поддержка неквадратных матриц:** по условиям ТЗ гарантируется, что исходная матрица всегда имеет размерность $N \times N$.

---

## Структура проекта

* `matrix_loader.py` — основной модуль библиотеки с логикой загрузки, парсинга и спирального обхода.
* `test_matrix.py` — юнит-тест для проверки основного сценария.
* `.github/workflows/tests.yml` — конфигурация CI/CD для автоматического прогона тестов в GitHub Actions.

---

## Как запустить и проверить

### 1. Клонирование репозитория
```bash
git clone https://github.com/LayrCrismer/python-matrix-trainee.git
cd python-matrix-trainee
```

### 2. Установка зависимостей
Рекомендуется использовать виртуальное окружение (Python 3.10+):
```bash
python -m venv .venv
# Активация в Windows:
.venv\Scripts\activate
# Активация в Linux/macOS:
source .venv/bin/activate

python -m pip install httpx pytest pytest-asyncio
```

### 3. Запуск тестов
Для проверки работоспособности выполните команду:
```bash
python -m pytest
```

### Пример использования в коде
```python
import asyncio
from matrix_loader import get_matrix

url = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
result = asyncio.run(get_matrix(url))
print(result)
# Вывод: [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]
```
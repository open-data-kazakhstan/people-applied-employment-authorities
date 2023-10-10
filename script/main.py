# Импорт библиотек
import pandas as pd
import bar_chart_race as bcr

# Загрузка данных из CSV-файла
df = pd.read_csv('data/data.csv')

# Установка столбца 'year' в качестве индекса DataFrame
df = df.set_index('year')

# Путь к файлу для сохранения видео
output_file_path = 'video/video.mp4'

# Создание bar chart race с определенными параметрами
bcr.bar_chart_race(
    df=df,  # DataFrame с данными
    title='Number of people who applied to employment authorities',  # Заголовок видео
    orientation='h',  # Ориентация: горизонтальная
    sort='desc',  # Сортировка данных в нисходящем порядке
    n_bars=10,  # Количество столбцов, отображаемых в каждый момент времени
    steps_per_period=40,  # Количество шагов (кадров) на каждый период данных
    period_length=2000,  # Длительность каждого периода в миллисекундах
    filename=output_file_path,  # Путь и имя файла для сохранения видео
    figsize=(9, 16),  # Размер фигуры
    cmap='dark12',  # Цветовая карта
    bar_kwargs={'alpha': 0.7},  # Прозрачность столбцов
    filter_column_colors=True,  # Разрешить изменение цвета столбцов в процессе анимации
    title_size=20,  # Размер шрифта заголовка
    bar_label_size=15,  # Размер шрифта для названий регионов
    tick_label_size=15  # Размер шрифта для числа населения
)
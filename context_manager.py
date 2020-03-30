# Генерация списка из 50 млн элементов и применение к нему фукнции set

from contextlib import contextmanager
from random import randint
from datetime import datetime


@contextmanager
def time_logger():
    date_start = datetime.now()
    print(f"Время начала работы: {date_start}")
    yield # тут будет подставлен блок из конструции with
    date_end = datetime.now()
    print(f"Время окончания работы: {date_end}")
    print(f"Время работы: {date_end - date_start}")


if __name__ == '__main__':
    with time_logger():
        nums = set([randint(1, 100) for i in range(50_000_000)])

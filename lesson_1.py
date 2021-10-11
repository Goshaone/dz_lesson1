def duration(n):
    day = n // (24 * 3600)
    n = n % (24 * 3600)
    hour = n // 3600
    n = n % 3600
    minutes = n // 60
    n = n % 60
    seconds = n
    print(day, "дн.", hour, "час", minutes, "мин", seconds, "сек")

n = int(input('Введите количество секунд: '))
duration(n)


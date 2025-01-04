import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.day = 0 # день
        self.warrior = 100 # воин

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.warrior > 0:
            self.day += 1
            self.warrior -= self.power
            time.sleep(1)
            print(f'{self.name} сражается {self.day} день(дня)..., осталось {self.warrior} воинов.')
        if self.warrior <= 0:
            print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')
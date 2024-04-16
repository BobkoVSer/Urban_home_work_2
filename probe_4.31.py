
import time
from threading import Thread



class Knight(Thread):
    def __init__ (self, name, skills, *args, **kwargs):
        super(Knight, self). __init__(*args, **kwargs)
        self.attack = 100
        self.name = name
        self.skills = skills
    def run (self):
            day = 0
            while self.attack > 0:
                self.attack -= self.skills
                day += 1
                print(f'{self.name} сражается {day} день(дня)..., осталось {self.attack} воинов', flush= True)
                print(f'{self.name} одержал победу спустя {day} дней!')
time.sleep(1)

Lanselot = Knight(name='Sir_Lanselot', skills=10)
Galahat = Knight(name='Sir_Galahat', skills=20)

print(f'{Lanselot.name}, на нас напали!')
print(f'{Galahat.name}, на нас напали!')

Lanselot.start()
time.sleep(0.5)
Galahat.start()

Lanselot.join()
Galahat.join()
print('Все битвы закончились!')
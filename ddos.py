import time
import random
from colorama import *

url = input("Введіть юрл російського сайту: ")
i = int(input("Введіть кількість пакетів (аттак на сайт): "))   
print("Слава Україні!")
time.sleep(2)
while i > 0:
    print(f"Спроба надсилання пакету з текстом <Слава Україні> на сайт {url}")
    time.sleep(0.2)
    isatacked = random.randint(0, 1)
    if isatacked == 0:
        print(Back.RED + "Спроба провалена(")
    elif isatacked == 1:
        print(Back.GREEN + "Пакет надісланий успішно!")


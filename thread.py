#! /usr/bin/env python3

import time
import random
from threading import Thread

class MyThread(Thread):
    """
    A threading example
    """

    def __init__(self, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name

    def run(self):
        """Запуск потока"""
        amount = random.randint(3, 15)
        time.sleep(amount)
        msg = "%s is running" % self.name
        print(msg)

def main():
    """
    Запускаем программу
    """
    print("Begin")

    """
    Создаем группу потоков
    """
    for i in range(5):
        name = f"Thread №{i}"
        my_thread = MyThread(name)
        my_thread.setDaemon(True)
        my_thread.start()

    print("End")


if __name__ == "__main__":
    try:
        main()
    except:
        raise

from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.stop_deposit = False

    def deposit(self):
        for i in range(100):
            if self.stop_deposit:
                break
            amount = randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")

            sleep(0.001)

    def take(self):
        for x in range(100):
            amount = randint(50, 500)
            print(f"Запрос на {amount}")
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print(f"Запрос отклонён, недостаточно средств")
                    self.stop_deposit = True
                    break
            sleep(0.001)


bk = Bank()

th1 = Thread(target=bk.deposit)
th2 = Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

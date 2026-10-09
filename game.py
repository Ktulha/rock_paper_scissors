from datetime import datetime
import random
import json


class Game:
    """
    Базовый класс игры
    """

    def __init__(self):
        self.score = 0
        self.user_choise = None
        self.computer_choise = None

    def start(self):
        """
        Старт 1 раунда игры
        """
        print('\033c\033[3J', end='')
        print(
            "\n\033[1;36m>>>>>>>>>> ИГРА КАМЕНЬ-НОЖНИЦЫ-БУМАГА <<<<<<<<<<\n\033[0m")
        print(
            f'\n\033[1;34mВаш выбор:\033[0m {self._get_user_choice()}\n\033[1;34mКомпьютер выбрал:\033[0m {self._generate_computer_choice()}\n')
        winner = self._check_winner()
        if self.score == 0:
            print(f"{winner}\n")
        else:
            print(
                f'\033[1;34mВыиграл:\033[0m \033[1m{winner}\n\033[1;34mСчет:\033[0m {self.score}\n ')

    def _generate_computer_choice(self):
        self.computer_choice = random.choice(
            ['камень', 'бумага', 'ножницы'])
        return self.computer_choice

    def _get_user_choice(self):
        choises = {"1": 'камень', '2': 'бумага', '3': 'ножницы'}
        choise = input(1
                       "\033[1;34mВыберите ваш вариант:\033[0m \n\n1 - камень\n2 - бумага\n3 - ножницы\n\n>>>>>>> : ")
        if choise in choises:
            self.user_choise = choises[choise]
            return self.user_choise
        if choise not in choises:
            print("Wrong choise")
            return self._get_user_choice()

    def _check_winner(self):
        if self.user_choise == self.computer_choice:
            self.score = 0
            return "НИЧЬЯ"
        if self.user_choise == 'камень' and self.computer_choice == 'ножницы':
            self.score = 1
            return "user"
        if self.user_choise == 'бумага' and self.computer_choice == 'камень':
            self.score = 1
            return "user"
        if self.user_choise == 'ножницы' and self.computer_choice == 'бумага':
            self.score = 1
            return "user"
        self.score = -1
        return "computer"

    def to_dict(self):
        return {"user_choise": self.user_choise, "computer_choice": self.computer_choice, "score": self.score}


class ScoreBoard:
    """
    Класс для вывода таблицы результатов
    """


if __name__ == '__main__':
    game = Game()
    game.start()

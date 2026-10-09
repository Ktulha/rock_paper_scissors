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
        choise = input(
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

    def __init__(self):
        self.games = {}
        self.user_wins = 0
        self.computer_wins = 0
        self.draws = 0
        self.date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def start_game(self):
        """
        Запускаем игру в цикле
            - запускаем игру
            - обновляем результаты игры
            - показываем результаты игры
            - сохраняем результаты игры
            - выход из цикла
        """
        while True:
            game = Game()
            game.start()
            self.update(game)
            if input("\nСыграем еще раз? (y/n): ") == 'n':
                break

        if input("\nПоказать результат? (y/n): ") == 'y':
            self.show()
        if input("\nСохранить результат? (y/n): ") == 'y':
            self.save()

        return game

    def update(self, game):
        """
        Обновляем результаты игры
        """
        if game.score == 1:
            self.user_wins += 1
        if game.score == -1:
            self.computer_wins += 1
        if game.score == 0:
            self.draws += 1
        self.games[len(self.games)+1] = game.to_dict()

    def show(self):
        """
        Показываем результаты игры
        """
        print(
            f"\n\033[1;34mСыграно игр:\033[0m {len(self.games)}\n\033[1;34mВыиграл:\033[0m \033[1m{self.user_wins}\n\033[1;34mПроиграл:\033[0m {self.computer_wins}\n\033[1;34mНичья:\033[0m {self.draws}\n\033[1;34mСчет:\033[0m {self.user_wins} \\ {self.computer_wins}\n")

    def show_games(self):
        print(f"\n\033[1;34mИгры:\033[0m {self.games}\n")

    def to_dict(self):
        """
        выводим результаты игры в формате json
        """
        return {'score': {
            'user_wins': self.user_wins,
            'computer_wins': self.computer_wins,
            'draws': self.draws,
            'date': self.date,
        },
            'games': self.games}

    def save(self):
        """
        Сохраняем результаты игры
        """
        try:
            with open('score.json', 'r', encoding="utf-8") as f:
                file_data = json.load(f)
        except FileNotFoundError:
            file_data = {'saved_results': []}
            with open('score.json', 'w', encoding="utf-8") as f:
                f.seek(0)
                json.dump(file_data, f, indent=4)

        file_data['saved_results'].append(self.to_dict())

        with open('score.json', 'w', encoding="utf-8") as f:
            f.seek(0)
            json.dump(file_data, f, indent=4, ensure_ascii=False)
        print("\n\033[1;34mРезультаты сохранены\033[0m")


if __name__ == '__main__':
    ScoreBoard().start_game()

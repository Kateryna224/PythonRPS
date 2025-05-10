import random
from schemas.game import Choice, Winner

WINNING_COMBINATIONS = {
    Choice.КАМЕНЬ: Choice.НОЖНИЦЫ,
    Choice.БУМАГА: Choice.КАМЕНЬ,
    Choice.НОЖНИЦЫ: Choice.БУМАГА
}

def get_random_choice(choices: list[Choiceка]) -> Choice:
    return random.choice(choices)

def determine_winner(player_choice: Choice, computer_choice: Choice) -> Winner:
    if player_choice == computer_choice:
        return "Ничья"
    elif WINNING_COMBINATIONS[player_choice] == computer_choice:
        return "Игрок"
    else:
        return 'Компьютер'

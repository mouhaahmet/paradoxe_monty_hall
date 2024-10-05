import random
from typing import List

class MontyHallGame:
    def __init__(self):
        self.doors: List[str] = ["goat", "goat", "car"]
        self.player_choice: int = -1
        self.revealed_door: int = -1

    def reset_game(self):
        """Réinitialise le jeu avec une nouvelle configuration des portes."""
        random.shuffle(self.doors)
        self.player_choice = -1
        self.revealed_door = -1

    def player_select_door(self, choice: int):
        """Le joueur sélectionne une porte (de 0 à 2)."""
        if 0 <= choice < 3:
            self.player_choice = choice
        else:
            raise ValueError("Le choix de la porte doit être 0, 1 ou 2.")

    def reveal_goat(self):
        """Montre une porte avec une chèvre que le joueur n'a pas choisie."""
        available_doors = [i for i in range(3) if i != self.player_choice and self.doors[i] == "goat"]
        self.revealed_door = random.choice(available_doors)

    def change_choice(self):
        """Permet au joueur de changer de porte après avoir révélé une chèvre."""
        remaining_doors = [i for i in range(3) if i != self.player_choice and i != self.revealed_door]
        self.player_choice = remaining_doors[0]

    def is_winner(self) -> bool:
        """Retourne True si le joueur a gagné la voiture, sinon False."""
        return self.doors[self.player_choice] == "car"


def simulate_games(n_games: int, change: bool) -> float:
    """Simule n parties de Monty Hall et retourne le pourcentage de victoires."""
    wins = 0
    game = MontyHallGame()

    for _ in range(n_games):
        game.reset_game()
        initial_choice = random.randint(0, 2)
        game.player_select_door(initial_choice)
        game.reveal_goat()

        if change:
            game.change_choice()

        if game.is_winner():
            wins += 1

    return (wins / n_games) * 100

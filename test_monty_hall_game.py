import unittest
from monty_hall_game import MontyHallGame, simulate_games

class TestMontyHallGame(unittest.TestCase):

    def setUp(self):
        """Initialise un objet MontyHallGame avant chaque test."""
        self.game = MontyHallGame()

    def test_initialization(self):
        """Test que le jeu est bien initialisé avec 2 chèvres et 1 voiture."""
        self.assertEqual(self.game.doors.count("goat"), 2)
        self.assertEqual(self.game.doors.count("car"), 1)

    def test_player_select_door(self):
        """Test que le joueur peut sélectionner une porte valide."""
        self.game.player_select_door(1)
        self.assertEqual(self.game.player_choice, 1)

    def test_player_select_invalid_door(self):
        """Test que la sélection d'une porte invalide génère une erreur."""
        with self.assertRaises(ValueError):
            self.game.player_select_door(3)  # Porte invalide

    def test_reveal_goat(self):
        """Test que la méthode reveal_goat révèle toujours une porte avec une chèvre."""
        self.game.player_select_door(0)
        self.game.reveal_goat()
        self.assertIn(self.game.revealed_door, [1, 2])
        self.assertEqual(self.game.doors[self.game.revealed_door], "goat")

    def test_change_choice(self):
        """Test que la méthode change_choice permet de changer de porte correctement."""
        self.game.player_select_door(0)
        self.game.reveal_goat()
        old_choice = self.game.player_choice
        self.game.change_choice()
        self.assertNotEqual(self.game.player_choice, old_choice)

    def test_is_winner(self):
        """Test que is_winner retourne True si le joueur a gagné (choisi la voiture)."""
        # Simuler un cas où le joueur gagne
        self.game.doors = ["car", "goat", "goat"]
        self.game.player_select_door(0)
        self.assertTrue(self.game.is_winner())

        # Simuler un cas où le joueur perd
        self.game.doors = ["car", "goat", "goat"]
        self.game.player_select_door(1)
        self.assertFalse(self.game.is_winner())

    def test_simulate_games_without_change(self):
        """Test que la simulation sans changement de porte retourne un pourcentage entre 0 et 100."""
        result = simulate_games(100, change=False)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 100)

    def test_simulate_games_with_change(self):
        """Test que la simulation avec changement de porte retourne un pourcentage entre 0 et 100."""
        result = simulate_games(100, change=True)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 100)


if __name__ == '__main__':
    unittest.main()

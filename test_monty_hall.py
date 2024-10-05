from monty_hall_game import simulate_games

def test_monty_hall():
    n_games = 10000

    # Simulation sans changement de porte
    win_percentage_without_change = simulate_games(n_games, change=False)
    print(f"Sans changement : {win_percentage_without_change:.2f}% de victoires sur {n_games} parties.")

    # Simulation avec changement de porte
    win_percentage_with_change = simulate_games(n_games, change=True)
    print(f"Avec changement : {win_percentage_with_change:.2f}% de victoires sur {n_games} parties.")


if __name__ == "__main__":
    test_monty_hall()

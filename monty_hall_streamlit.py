import logging
import streamlit as st
from monty_hall_game import simulate_games

# Configurer le fichier de log
logging.basicConfig(filename='/app/logs/monty_hall_app.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Exemple de log pour indiquer que l'application a démarré
logging.info('Application Monty Hall démarrée')

# Titre de l'application
st.title("Simulation du paradoxe de Monty Hall")

# Explication du jeu
st.write("""
Bienvenue dans la simulation du paradoxe de Monty Hall !
Vous êtes dans un jeu où vous devez choisir une porte parmi trois :
derrière l'une d'elles se cache une voiture, et derrière les deux autres se trouvent des chèvres.

Après votre choix initial, une des portes avec une chèvre sera révélée, et vous aurez la possibilité de changer votre choix.
L'objectif de cette simulation est de voir si changer de porte ou rester sur votre choix initial vous donne une meilleure chance de gagner.
""")

# Input pour le nombre de simulations
n_games = st.slider("Combien de parties voulez-vous simuler ?", min_value=100, max_value=10000, step=100, value=1000)

# Input pour la stratégie de jeu : changer ou non de porte
change = st.radio("Voulez-vous changer de porte après la révélation ?", ("Oui", "Non"))

# Lancer la simulation lorsque l'utilisateur appuie sur le bouton
if st.button("Lancer la simulation"):
    change_choice = change == "Oui"  # Convertir en booléen
    win_percentage = simulate_games(n_games, change=change_choice)

    # Afficher les résultats
    st.write(
        f"Sur {n_games} parties simulées, vous avez gagné **{win_percentage:.2f}%** des parties en choisissant de {'changer' if change_choice else 'ne pas changer'} de porte.")

    # Interprétation des résultats
    if change_choice:
        st.write("Changer de porte augmente vos chances de gagner car les probabilités sont en votre faveur.")
    else:
        st.write("Garder votre choix initial vous donne moins de chances de gagner, en moyenne.")

    # Ajouter des logs pour chaque simulation
    logging.info(
         f"Simulation lancée avec {n_games} parties - {'Changer' if change_choice else 'Ne pas changer'} de porte.")
    logging.info(f"Résultat : {win_percentage:.2f}% de victoires")

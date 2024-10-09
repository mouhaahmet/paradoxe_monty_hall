import logging
import streamlit as st
from monty_hall_game import simulate_games

log_dir = './logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=os.path.join(log_dir, 'monty_hall_app.log'),
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


logging.info('Application Monty Hall démarrée')


st.title("Simulation du paradoxe de Monty Hall")

st.write("""
Bienvenue dans la simulation du paradoxe de Monty Hall !
Vous êtes dans un jeu où vous devez choisir une porte parmi trois :
derrière l'une d'elles se cache une voiture, et derrière les deux autres se trouvent des chèvres.

Après votre choix initial, une des portes avec une chèvre sera révélée, et vous aurez la possibilité de changer votre choix.
L'objectif de cette simulation est de voir si changer de porte ou rester sur votre choix initial vous donne une meilleure chance de gagner.
""")

n_games = st.slider("Combien de parties voulez-vous simuler ?", min_value=100, max_value=10000, step=100, value=1000)


change = st.radio("Voulez-vous changer de porte après la révélation ?", ("Oui", "Non"))


if st.button("Lancer la simulation"):
    change_choice = change == "Oui"  
    win_percentage = simulate_games(n_games, change=change_choice)


    st.write(
        f"Sur {n_games} parties simulées, vous avez gagné **{win_percentage:.2f}%** des parties en choisissant de {'changer' if change_choice else 'ne pas changer'} de porte.")

    if change_choice:
        st.write("Changer de porte augmente vos chances de gagner car les probabilités sont en votre faveur.")
    else:
        st.write("Garder votre choix initial vous donne moins de chances de gagner, en moyenne.")

    
    logging.info(
         f"Simulation lancée avec {n_games} parties - {'Changer' if change_choice else 'Ne pas changer'} de porte.")
    logging.info(f"Résultat : {win_percentage:.2f}% de victoires")

from ui.ui import GUI
from repository.highscore_repository import HighscoreRepository
from database_connection import get_database_connection
from initialize_database import initialize_database
"""
Metodi sovelluksen käynnistämiseen.
"""
def main():
    guivariable = GUI()
    guivariable.main()
if __name__ == "__main__":
    h = HighscoreRepository(get_database_connection())
    h.add_name("Pelaaja 1")
    h.add_name("Pelaaja 2")
    h.add_name("Pelaaja 3")
    h.add_name("Pelaaja 4")
    game_objects = []
    game_objects.append([1, 1, 52])
    game_objects.append([2, 1, 6])
    game_objects.append([3, 1, 29])
    game_objects.append([4, 1, 22])
    h.add_game(game_objects)
    names = h.get_names()
    h.get_points(1)
    print("ok")
    main()

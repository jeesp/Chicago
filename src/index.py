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
    initialize_database()
    main()

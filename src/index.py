from repository.highscore_repository import HighscoreRepository
from database_connection import get_database_connection
from initialize_database import initialize_database
from game_logic.game_actions import App
"""
Metodi sovelluksen käynnistämiseen.
"""
def main():
    app = App()
    app.gui.main(app)

if __name__ == "__main__":
    main()

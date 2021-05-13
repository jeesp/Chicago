from game_logic.game_actions import App

def main():
    """
    Metodi sovelluksen käynnistämiseen.
    """
    app = App()
    app.gui.main(app)

if __name__ == "__main__":
    main()

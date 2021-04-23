from game_logic import play
from ui.ui import GUI


def main():
    play()


if __name__ == "__main__":
    while True:
        print ("Tekstikäyttöliittymä vai GUI ? 1/2")
        syote = input()
        if syote == "1":
            main()
        elif syote == "2":
            guivariable = GUI()
            guivariable.main()
        else:
            print("")
            print("virheellinen syöte. Kirjoita joko 1 tai 2.")
            print("")
            continue
        break

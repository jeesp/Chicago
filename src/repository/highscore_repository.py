from database_connection import get_database_connection
class HighscoreRepository:
    """
    Tietokantaluokka. Tämän luokan avulla haetaan/tallennetaan/poistetaan tietoa tietokannasta.
    """
    def __init__(self, connection):
        self.connection = connection
    def get_players(self):
        """
        Metodi hakee pelaajat tietokannasta.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM players")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(row[1])
        return result
    def get_latest_game(self):
        """
        Metodi hakee tietokannasta viimeisimmän pelin id:n ja palauttaa siitä seuraavan.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT max(game_id) FROM games")
        game_id = cursor.fetchone()[0]
        return game_id + 1
    def get_player_id(self, player):
        """
        Metodi hakee pelaajan id:n tietokannasta.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id FROM players WHERE name = (?)", (player,))
        player_id = cursor.fetchone()[0]
        return player_id
    def get_points(self, player):
        """
        Metodi hakee pelaajan kokonaispisteet tietokannasta.
        """
        cursor = self.connection.cursor()
        player_id = self.get_player_id(player)
        points = 0
        if player_id in [1, 2, 3, 4]:
            cursor.execute("SELECT SUM(points) FROM games WHERE player_id = (?)", (player_id,))
            row = cursor.fetchone()
            points = row[0]
        return points
    def add_name(self, name):
        """
        Metodi lisää pelaajan tietokantaan.
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT OR IGNORE INTO players(name) VALUES (?)", (name,))
        self.connection.commit()
    def create_game_object(self, app):
        """
        Metodi luo peliobjektin, jonka avulla voi luoda uuden pelin.
        """
        game_id = self.get_latest_game()
        game_objects = []
        for player in app.players:
            player_id = self.get_player_id(player.name)
            game_objects.append([player_id, game_id, app.scoreboard[player]])
        self.add_new_game(game_objects)
    def add_new_game(self, game_object):
        """
        Metodi lisää uuden pelin tietokantaan.
        """
        cursor = self.connection.cursor()
        for player in game_object:
            cursor.execute("INSERT INTO games (player_id, game_id, points) VALUES (?,?,?)",
                           (player[0], player[1], player[2]))
        self.connection.commit()
    def delete_all(self):
        """
        Metodi tyhjentää tietokannan taulut.
        """
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM players")
        cursor.execute("DELETE FROM games")
highscore_repository = HighscoreRepository(get_database_connection)

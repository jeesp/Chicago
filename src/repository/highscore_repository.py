from database_connection import get_database_connection
class HighscoreRepository:

    def __init__(self, connection):
        self.connection = connection
    def get_players(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM players")
        rows = cursor.fetchall()
        return rows
    def get_latest_game(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT max(game_id) FROM games")
        game_id = cursor.fetchone()[0]
        return game_id + 1
    def get_player_id(self, player):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id FROM players WHERE name = (?)", (player,))
        player_id = cursor.fetchone()[0]
        return player_id
    def get_points(self, player):
        cursor = self.connection.cursor()
        player_id = self.get_player_id(player)
        if player_id in [1,2,3,4]:
            cursor.execute("SELECT SUM(points) FROM games WHERE player_id = (?)", (player_id,))
            rows = cursor.fetchall()
            return rows
        else:
            return 0
    def add_name(self, name):
        cursor = self.connection.cursor()
        cursor.execute("INSERT OR IGNORE INTO players(name) VALUES (?)", (name,))
        self.connection.commit()
    def create_game_object(self, app):
        game_id = self.get_latest_game()
        game_objects = []
        for player in app.players:
            player_id = self.get_player_id(player.name)
            game_objects.append([player_id, game_id, app.scoreboard[player]])
        self.add_new_game(game_objects)
    def add_new_game(self, game_object):
        cursor = self.connection.cursor()
        for player in game_object:
            cursor.execute("INSERT INTO games (player_id, game_id, points) VALUES (?,?,?)", (player[0], player[1], player[2]))
        self.connection.commit()
    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM players")
        cursor.execute("DELETE FROM games")
highscore_repository = HighscoreRepository(get_database_connection)

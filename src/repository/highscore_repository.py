from database_connection import get_database_connection
class HighscoreRepository:

    def __init__(self, connection):
        self.connection = connection
    def get_names(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM players")
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], row[1])
        
        return rows
    def get_points(self, player):
        cursor = self.connection.cursor()
        cursor.execute("SELECT SUM(points) FROM games WHERE player_id = (?)", (player,))
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])
        
        return rows
    def add_name(self, name):
        cursor = self.connection.cursor()
        cursor.execute("INSERT OR IGNORE INTO players(name) VALUES (?)", (name,))
        self.connection.commit()
    def add_game(self, game_object):
        cursor = self.connection.cursor()
        for player in game_object:
            cursor.execute("INSERT INTO games (player_id, game_id, points) VALUES (?,?,?)", (player[0], player[1], player[2]))
        self.connection.commit()
    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE * FROM players")
        cursor.execute("DELETE * FROM games")
highscore_repository = HighscoreRepository(get_database_connection)

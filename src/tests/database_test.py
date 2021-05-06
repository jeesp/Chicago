from repository.highscore_repository import delete_all
class TestDatabase(unittest.TestCase):
    def setUp(self):
        delete_all()
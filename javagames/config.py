import os

GAMES_PATH = os.environ.get('GAMES_PATH', '../games')
PORT = int(os.environ.get('GAMES_PORT', '8080'))
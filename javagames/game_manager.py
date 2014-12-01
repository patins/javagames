import config
import os

def get_valid_game_ids():
    game_ids = []
    directories = [ f for f in os.listdir(config.GAMES_PATH) if os.path.isdir(os.path.join(config.GAMES_PATH,f)) ]
    for directory in directories:
        if directory.isdigit() and len([ f for f in os.listdir(os.path.join(config.GAMES_PATH, directory)) if os.path.isfile(os.path.join(os.path.join(config.GAMES_PATH, directory),f)) and f.endswith('.class')]) == 1:
            game_ids += [int(directory)]
    return game_ids

def get_class_path(game_id):
    return os.path.join(config.GAMES_PATH, game_id)

def get_class_name(game_id):
    return [ f for f in os.listdir(os.path.join(config.GAMES_PATH, game_id)) if os.path.isfile(os.path.join(os.path.join(config.GAMES_PATH, game_id),f)) and f.endswith('.class')][0].replace('.class', '')

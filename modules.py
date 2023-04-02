import os

def home_directory():
    return os.path.expanduser( '~' )

def dir_list(path):
    return os.listdir(path)
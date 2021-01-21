import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from core import src

if __name__ == '__main__':
    src.run()

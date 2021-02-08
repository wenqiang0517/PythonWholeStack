import os
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

register = os.path.join(BASE_PATH, 'db', 'user.txt')

article = os.path.join(BASE_PATH, 'db', 'article')

user_status = os.path.join(BASE_PATH, 'db', 'user_status.json')

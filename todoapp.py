from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://root:jjbVaAgNrBNV7kD0@172.17.42.1:49153/todoapp'

from views import *

if __name__ == '__main__':
    app.run()


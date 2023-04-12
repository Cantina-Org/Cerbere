from json import load
from os import path, getcwd
from flask import Flask, request
from Cogs.auth import auth_cogs
from Cogs.home import home_cogs
from Cogs.my_account import my_account_cogs
from Utils.Database import DataBase

app = Flask(__name__)
conf_file = open(path.abspath(getcwd()) + "/config.json", 'r')
config_data = load(conf_file)

# Connection aux bases de données
database = DataBase(user=config_data['database'][0]['database_username'],
                    password=config_data['database'][0]['database_password'], host="localhost", port=3306)
database.connection()


@app.route('/')
def home():
    return home_cogs()


@app.route('/auth/<url_to_redirect>', methods=['GET', 'POST'])
@app.route('/auth/', methods=['GET', 'POST'])
def auth(url_to_redirect=None):
    return auth_cogs(request, database, url_to_redirect)


@app.route('/account/my', methods=['GET', 'POST'])
def my_account():
    return my_account_cogs(request, database)


if __name__ == '__main__':
    app.run()

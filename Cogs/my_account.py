from datetime import datetime
from Utils.Utils import verify_hash_password, make_log
from flask import render_template, redirect, url_for, make_response
from argon2 import PasswordHasher

ph = PasswordHasher()


def auth_cogs(ctx, database):
    database.select('''SELECT * FROM ''')

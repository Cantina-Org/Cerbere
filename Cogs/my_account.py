from datetime import datetime
from Utils.Utils import verify_hash_password, make_log
from flask import render_template, redirect, url_for, make_response
from argon2 import PasswordHasher

ph = PasswordHasher()


def my_account_cogs(ctx, database):
    data = database.select('''SELECT * FROM cantina_administration.user WHERE token=%s''', (ctx.cookies.get('userID')), 1)
    return data

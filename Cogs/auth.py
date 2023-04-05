from datetime import datetime
from Utils.Utils import hash_password, verify_hash_password, make_log
from flask import render_template, redirect, url_for, make_response
from argon2 import PasswordHasher

ph = PasswordHasher()


def auth_cogs(ctx, database):
    if ctx.method == 'POST':
        user = ctx.form['nm']
        try:
            passwd = ctx.form['passwd']
            print(passwd)
            row = database.select(f'''SELECT password, token FROM cantina_administration.user WHERE user_name = %s''', (user), 1)
            print(row[0])
            login = verify_hash_password(row[0], passwd)
        except Exception as e:
            return 'userNotFound: ' + str(e)

        try:
            if login:
                make_log(action_name='login', user_ip=ctx.remote_addr, user_token=row[2], log_level=1, database=database())
                resp = make_response(redirect(url_for('home')))
                resp.set_cookie('userID', row[1])
                database.insert('''UPDATE cantina_administration.user SET last_online=%s WHERE token=%s''',
                                (datetime.now(), row[1]))
                return resp
            else:
                return 'userNotFound'
        except Exception as error:
            make_log('Error', ctx.remote_addr, ctx.cookies.get('userID'), 2, str(error))
            return redirect(url_for("home"))

    elif ctx.method == 'GET':
        return render_template('login.html')

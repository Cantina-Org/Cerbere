from datetime import datetime
from Utils.Utils import hash_password, make_log
from flask import render_template, redirect, url_for, make_response


def auth_cogs(ctx, database):
    if ctx.method == 'POST':
        user = ctx.form['nm']
        try:
            passwd = hash_password(ctx.form['passwd'])
            row = database.select(f'''SELECT user_name, password, token FROM cantina_administration.user WHERE password = %s AND user_name = %s''', (passwd, user), 1)
        except Exception as e:
            return 'userNotFound: ' + str(e)

        try:
            make_log('login', ctx.remote_addr, row[2], 1, database)
            resp = make_response(redirect(url_for('home')))
            resp.set_cookie('userID', row[2])
            database.insert('''UPDATE cantina_administration.user SET last_online=%s WHERE token=%s''',
                            (datetime.now(), row[2]))
            return resp
        except Exception as error:
            make_log('Error', ctx.remote_addr, ctx.cookies.get('userID'), 2, str(error))
            return redirect(url_for("home"))

    elif ctx.method == 'GET':
        return render_template('login.html')

from datetime import datetime
from Utils.Utils import verify_hash_password, make_log
from flask import render_template, redirect, url_for, make_response
from argon2 import PasswordHasher

ph = PasswordHasher()


def auth_cogs(ctx, database, url_to_redirect):
    if ctx.method == 'POST':
        user = ctx.form['nm']
        try:
            passwd = ctx.form['passwd']
            row = database.select(f'''SELECT password, token FROM cantina_administration.user WHERE user_name = %s''',
                                  (user), 1)
            login = verify_hash_password(row[0], passwd)
        except Exception as e:
            return 'userNotFound: ' + str(e)

        try:
            if login:
                make_log(action_name='login', user_ip=ctx.remote_addr, user_token=row[1], log_level=1,
                         database=database)
                if not url_to_redirect:
                    data = database.select('SELECT fqdn FROM cantina_administration.domain WHERE name="olympie"',
                                           number_of_data=1)
                    resp = make_response(redirect('https://' + data[0] + '/', code=302))
                else:
                    data = database.select('SELECT fqdn FROM cantina_administration.domain WHERE name=%s',
                                           (url_to_redirect,), 1)
                    resp = make_response(redirect('https://' + data[0] + '/', code=302))

                domain = database.select("SELECT fqdn FROM cantina_administration.domain WHERE name='main'")
                resp.set_cookie('token', row[1], domain=domain[0][0])
                database.insert('''UPDATE cantina_administration.user SET last_online=%s WHERE token=%s''',
                                (datetime.now(), row[1]))
                return resp
            else:
                return 'userNotFound'
        except Exception as error:
            make_log('Error', ctx.remote_addr, ctx.cookies.get('userID'), 2, str(error))
            return redirect(url_for("home"))

    elif ctx.method == 'GET':
        if ctx.cookies.get('token'):
            if not url_to_redirect:
                resp = make_response(redirect(url_for('my_account')))
            else:
                data = database.select('SELECT fqdn FROM cantina_administration.domain WHERE name=%s',
                                       (url_to_redirect,), 1)
                resp = make_response(redirect(data))

        return render_template('login.html', url_to_redirect=url_to_redirect)

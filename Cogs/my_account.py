from flask import redirect, url_for


def my_account_cogs(ctx, database):
    if not ctx.cookies.get('userID'):
        return redirect(url_for('auth'))

    data = database.select('''SELECT * FROM cantina_administration.user WHERE token=%s''', (ctx.cookies.get('userID')), 1)
    return str(data)

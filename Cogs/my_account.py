from subprocess import check_output, CalledProcessError
from flask import redirect, url_for, render_template


def my_account_cogs(ctx, database):
    if not ctx.cookies.get('userID'):
        return redirect(url_for('auth'))

    user_data = database.select('''SELECT * FROM cantina_administration.user WHERE token=%s''',
                                (ctx.cookies.get('token')), 1)
    messsage_data = database.select('''SELECT * FROM cantina_hermes.data WHERE token=%s''', (ctx.cookies.get('userID'))
                                    , 1)
    try:
        folder_size = check_output(['du', '-sh', user_data[6]]).split()[0].decode('utf-8')
    except CalledProcessError:
        folder_size = 'error'
    return render_template('my_account.html', user_data=user_data, messsage_data=messsage_data, folder_size=folder_size)

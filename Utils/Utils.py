from hashlib import sha256
from argon2 import argon2_hash


def salt_password(passwordtohash, user_name, database, ctx, new_account=False):
    try:
        if not new_account:
            try:
                data = database.select('''SELECT salt FROM cantina_administration.user WHERE user_name=%s''',
                                       (user_name,), 1)
                passw = sha256(argon2_hash(passwordtohash, data[0])).hexdigest().encode()
                return passw
            except Exception as e:
                return 'User Not Found, ' + str(e)
        else:
            passw = sha256(argon2_hash(passwordtohash, user_name)).hexdigest().encode()
            return passw

    except AttributeError as error:
        make_log('Error', ctx.remote_addr, ctx.cookies.get('userID'), 2, str(error))
        return None


def make_log(action_name, user_ip, user_token, log_level, database, argument=None, content=None,):
    if content:
        database.insert('''INSERT INTO cantina_administration.log(name, user_ip, user_token, argument, log_level) 
        VALUES (%s, %s, %s,%s,%s)''', (str(action_name), str(user_ip), str(content), argument, log_level))
    else:
        database.insert('''INSERT INTO cantina_administration.log(name, user_ip, user_token, argument, log_level) 
        VALUES (%s, %s, %s,%s,%s)''', (str(action_name), str(user_ip), str(user_token), argument, log_level))


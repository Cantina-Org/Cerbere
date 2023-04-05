from argon2 import PasswordHasher

ph = PasswordHasher()


def hash_password(passwordtohash: str):
    return ph.hash(passwordtohash)


def make_log(action_name, user_ip, user_token, log_level, database, argument=None, content=None, ):
    if content:
        database.insert('''INSERT INTO cantina_administration.log(name, user_ip, user_token, argument, log_level) 
        VALUES (%s, %s, %s,%s,%s)''', (str(action_name), str(user_ip), str(content), argument, log_level))
    else:
        database.insert('''INSERT INTO cantina_administration.log(name, user_ip, user_token, argument, log_level) 
        VALUES (%s, %s, %s,%s,%s)''', (str(action_name), str(user_ip), str(user_token), argument, log_level))

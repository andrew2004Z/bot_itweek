import sqlite3


class WorkDB:
    def __init__(self, path_db):
        self.connection = sqlite3.connect(path_db)
        self.cursor = self.connection.cursor()

    def create_user(self, user_id, username, score):
        with self.connection:
            return self.cursor.execute('''INSERT INTO 'users' (id, username, score)  VALUES  (?,?,?)''', (user_id, username, score))

    def check_user(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('''SELECT * FROM `users` WHERE `id` = ?''', (user_id,)).fetchall()
            return bool(len(result))

    def create_answer(self, user_id, answer):
        with self.connection:
            return self.cursor.execute('''INSERT INTO 'answer' (id, answer)  VALUES  (?,?)''', (user_id, answer))

    def get_score(self, id):
        get_q = f'SELECT score FROM users WHERE id = {id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            return int(res)

    def update_score(self, user_id):
        with self.connection:
            score = self.get_score(user_id) + 1
            return self.cursor.execute('''UPDATE `users` SET `score` = ? WHERE `id` = ?''', (score, user_id))

    def get_username(self, user_id):
        get_q = f'SELECT username FROM users WHERE user_id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            return str(res)
    

    def get_users_train(self, user_id):
        get_q = f'SELECT answer FROM answer WHERE id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            return str(res)


    def update_answer(self, user_id, answer):
        with self.connection:
            return self.cursor.execute('''UPDATE `answer` SET `answer` = ? WHERE `id` = ?''',
                                       (str(answer), user_id))


    def get_top_rating(self):
        get_q = f'SELECT * FROM users;'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            all_users = []
            for item in result:
                all_users.append([item[0], item[1], item[2]])
            print(all_users)
            return all_users
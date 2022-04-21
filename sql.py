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

    def update_score(self, user_id, score):
        with self.connection:
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







    def get_username(self, user_id):
        get_q = f'SELECT username FROM users WHERE user_id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            print(res)
            return str(res)


    def update_tasks_id(self, user_id, tasks_id):
        with self.connection:
            return self.cursor.execute('''UPDATE `user_train` SET `tasks_id` = ? WHERE `user_id` = ?''',
                                       (str(tasks_id), user_id))

    

    def update_date_use(self, user_id, date_use):
        with self.connection:
            return self.cursor.execute('''UPDATE `users` SET `date_last_use` = ? WHERE `user_id` = ?''',
                                       (date_use, user_id))

    def update_task_id(self, user_id, task_id):
        with self.connection:
            return self.cursor.execute('''UPDATE `user_task` SET `task_id` = ? WHERE `user_id` = ?''',
                                       (task_id, user_id))

    def add_user_in_user_task(self, user_id, task_id):
        with self.connection:
            return self.cursor.execute('''INSERT INTO 'user_task' (user_id, task_id)  VALUES  (?,?)''',
                                       (user_id, task_id))

    def create_static(self, user_id, col_true, col_false, staicstic, rating):
        with self.connection:
            return self.cursor.execute('''INSERT INTO 'user_statistic' (user_id,сol_true_answer,col_false_answer,col_resh, rating)  VALUES  (?,?,?,?,?)''',
                                       (user_id, col_true, col_false, staicstic, rating))

    def get_rating_diapason(self, min_d, max_d):
        with self.connection:
            result = self.cursor.execute(f'SELECT * FROM tasks WHERE rating BETWEEN {min_d} AND {max_d}').fetchall()
            return result

    def update_col_true(self, user_id, col_true):
        with self.connection:
            return self.cursor.execute('''UPDATE `user_statistic` SET `сol_true_answer` = ? WHERE `user_id` = ?''',
                                       (col_true, user_id))

    def update_col_false(self, user_id, col_false):
        with self.connection:
            return self.cursor.execute('''UPDATE `user_statistic` SET `сol_false_answer` = ? WHERE `user_id` = ?''',
                                       (col_false, user_id))

    def update_col_resh(self, user_id, stat):
        with self.connection:
            return self.cursor.execute('''UPDATE `user_statistic` SET `col_resh` = ? WHERE `user_id` = ?''',
                                       (stat, user_id))

    def close_connection(self):
        self.sqlite_connection.close()
        return True

    def get_task_id_user(self, user_id):
        get_q = f'SELECT task_id FROM user_task WHERE user_id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            print(res)
            return str(res)

    def get_statistic(self, user_id):
        get_q = f'SELECT * FROM user_statistic WHERE user_id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            return result

    def get_task(self, id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchall()
            return result
    
    def get_task_answer(self, id):
        with self.connection:
            result = self.cursor.execute('SELECT answer FROM tasks WHERE id = ?', (id,)).fetchall()
            return result
        
    def get_all_task(self, number_task):
        get_q = f'SELECT * FROM tasks WHERE number_task = {number_task};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            return result

    def update_col_quetions(self, user_id, count_quetions):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute('''UPDATE `user_info` SET `count_quetions` = ? WHERE `user_id` = ?''',
                                       (count_quetions, user_id))

    def update_date_use(self, user_id, date_use):
        with self.connection:
            return self.cursor.execute('''UPDATE `users` SET `date_last_use` = ? WHERE `user_id` = ?''',
                                       (date_use, user_id))

    def get_top_rating(self):
        get_q = f'SELECT * FROM users;'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            all_users = []
            for item in result:
                all_users.append([item[0], item[1], item[2]])
            return all_users




    def update_task_num_attempts(self, id):
        with self.connection:
            num_attempts = self.get_task_num_attempts(id) + 1
            return self.cursor.execute('''UPDATE `tasks` SET `num_attempts` = ? WHERE `id` = ?''',
                                       (num_attempts, id))

    def get_task_num_attempts(self, id):
        get_q = f'SELECT num_attempts FROM tasks WHERE id = {id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            print(res)
            return int(res)
    
    def update_task_rating(self, id):
        with self.connection:
            rating = (self.get_task_rights_solves(id) / self.get_task_num_attempts(id) * 100)
            return self.cursor.execute('''UPDATE `tasks` SET `rating` = ? WHERE `id` = ?''',
                                       (rating, id))

    def update_task_rights_solves(self, id):
        with self.connection:
            num_attempts = self.get_task_rights_solves(id) + 1
            return self.cursor.execute('''UPDATE `tasks` SET `rights_solves` = ? WHERE `id` = ?''',
                                       (num_attempts, id))

    def get_task_rights_solves(self, id):
        get_q = f'SELECT rights_solves FROM tasks WHERE id = {id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            print(res)
            return int(res)

    def get_task_сol_true_answer(self, user_id):
        get_q = f'SELECT сol_true_answer FROM user_statistic WHERE user_id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            print(res)
            return int(res)

    def get_user_rating(self, user_id):
        get_q = f'SELECT rating FROM user_statistic WHERE user_id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            print(res)
            return int(res)

    def get_task_col_false_answer(self, user_id):
        get_q = f'SELECT col_false_answer FROM user_statistic WHERE user_id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            print(res)
            return int(res)

    def update_task_сol_true_answer(self, user_id):
        with self.connection:
            сol_true_answer = self.get_task_сol_true_answer(user_id) + 1
            return self.cursor.execute('''UPDATE `user_statistic` SET `сol_true_answer` = ? WHERE `user_id` = ?''',
                                       (сol_true_answer, user_id))

    def update_user_rating(self, user_id, rating_Add):
        with self.connection:
            rating = self.get_user_rating(user_id) + (101 - rating_Add)
            return self.cursor.execute('''UPDATE `user_statistic` SET `rating` = ? WHERE `user_id` = ?''',
                                       (rating, user_id))
    
    def update_task_col_false_answer(self, user_id):
        with self.connection:
            col_false_answer = self.get_task_col_false_answer(user_id) + 1
            return self.cursor.execute('''UPDATE `user_statistic` SET `col_false_answer` = ? WHERE `user_id` = ?''',
                                       (col_false_answer, user_id))

    def update_task_col_resh(self, user_id, col_resh):
        with self.connection:
            return self.cursor.execute('''UPDATE `user_statistic` SET `col_resh` = ? WHERE `user_id` = ?''',
                                       (col_resh, user_id))

    def get_task_rating(self, id):
        get_q = f'SELECT rating FROM tasks WHERE id = {id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            print(res)
            return int(res)

    

    def get_task_col_resh(self, user_id):
        get_q = f'SELECT col_resh FROM user_statistic WHERE user_id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            print(res)
            return res

    def get_task_number_id(self, id):
        get_q = f'SELECT number_task FROM tasks WHERE id = {id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            res = str(result[0])[1:]
            res = res[:-2]
            print(res)
            return int(res)

import sqlite3

class Database:
    def __int__(self):
        self.connection = sqlite3.connect("reg\\database.db")
        self.cursor = self.connection.cursor()
        print("Succsesed")

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))

    def users_exists(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM `users` WHERE `user_id`= ?", (user_id,)).fetchall()
            return bool(len(res))

    def set_name(self, user_id, name):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `name` = ? WHERE `user_id`= ?", (name, user_id))

    def get_signup(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT `signup` FROM `users` WHERE `user_id` = ?", (user_id)).fetchall()
            for row in res:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `signup` = ? WHERE `user_id`= ?", (signup, user_id))


































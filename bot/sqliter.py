import sqlite3

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status = True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `subscriptions` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status = True):
        with self.connection:
            return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES(?,?)", (user_id,status))

    def update_subscription(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def set_UTC(self,user_id, UTC):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `UTC` = ? WHERE `user_id` = ?", (UTC, user_id))

    def set_latest_place(self,user_id, latest_place):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `latest_place` = ? WHERE `user_id` = ?", (latest_place, user_id))

    def set_place(self,user_id, place):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `place` = ? WHERE `user_id` = ?", (place, user_id))

    def set_time(self,user_id, time):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `time` = ? WHERE `user_id` = ?", (time, user_id))

    def close(self):
        self.connection.close()

class SQLreader:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def read_informarion(self, user_id):
        with self.connection:
            temp = self.cursor.execute("SELECT * FROM subscriptions").fetchall()
            result = []        
            for i in temp:
                if str(user_id) in i:
                    result = i
                    break
            return result

import pymysql


class ColumbiaStudentResource:

    def __init__(self):
        pass

    @staticmethod
    def _get_connection():

        conn = pymysql.connect(
            user="admin",
            password="llqOFFER2020!",
            host="ll3466-coms6156.cbmcnoqggtt1.us-east-2.rds.amazonaws.com",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result


import pymysql

class Sql():
    def sql_data(self,sql1):
        db = pymysql.connect(host='47.119.123.226', port=3306, user='dbtest02', passwd='dbtest02', db='mm_test',
                             charset='utf8')
        cursor = db.cursor()
        sql =sql1
        cursor.execute(sql)
        data = cursor.fetchall()
        return data



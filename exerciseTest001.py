import pymysql

class MysqlUtil:
    def query(self, query):
        connection = pymysql.connect(
            host='localhost',
            user='root',
            passwd='Wntjdgh1!',
            db='datalab',
            charset='utf8mb4',
            port=3306
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()  # 변경 사항 커밋
                print("삭제 성공")

        except Exception as e:
            print("삭제 실패:", e)

        finally:
            connection.close()

# 사용 예시 코드
mysql_util = MysqlUtil()
QUERY = "DELETE FROM datalab.t_mart_sales_new"
mysql_util.query(QUERY)
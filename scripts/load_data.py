import pymysql
from parse_log import parse_line

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="mengxiang606",
    database="log_db"
)

cursor = conn.cursor()

sql = """
INSERT INTO access_log
(ip, request_time, method, url, status, response_size)
VALUES (%s, %s, %s, %s, %s, %s)
"""

data_list = []

with open("data/access.log", "r") as f:
    for line in f:
        parsed = parse_line(line.strip())
        if parsed:
            data_list.append(parsed)

cursor.executemany(sql, data_list)

conn.commit()

print("插入完成:", len(data_list))

cursor.close()
conn.close()
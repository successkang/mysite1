import pymysql
import pymysql.cursors

_db = pymysql.connect(
    host =  'successkang.mysql.pythonanywhere-services.com',
    user = 'successkang',
    port = 3306,
    password = 'qwer1234!',
    db = 'successkang$ubion'
    )

cursor = _db.cursor(pymysql.cursors.DictCursor)

create_user = """
    create table
    if not exists
    user(
    id varchar(32) primary key,
    password varchar(64) not null,
    name varchar(32) not null
    )
"""

cursor.execute(create_user)
_db.commit()
_db.close()
print('table 생성 완료')
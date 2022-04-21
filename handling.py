import psycopg2
import csv

# 클라우드 데이터베이스와 연결
conn = psycopg2.connect(
    host = 'rajje.db.elephantsql.com',
    database = 'esfjcgha',
    user = 'esfjcgha',
    password = 'TmHxm1cMLpre0SbR3dy4gulsGo7RHiht')
cur = conn.cursor()

# 테이블 생성
cur.execute("DROP TABLE IF EXISTS cafe")
cur.execute("DROP TABLE IF EXISTS card_sales")

crawling_data = """CREATE TABLE cafe (
                name VARCHAR(64), 
                score VARCHAR(64),
                visitor VARCHAR(64),
                blog VARCHAR(64)
                );"""

card_sales = """CREATE TABLE card_sales (
                년월 VARCHAR(64),
                시도명 VARCHAR(64),
                지역구분 VARCHAR(64),
                읍면동명 VARCHAR(64),
                이용자구분 VARCHAR(64),
                관광구분 VARCHAR(64),
                연령대 VARCHAR(64),
                성별 VARCHAR(64),
                이용금액 VARCHAR(64),
                매장수 VARCHAR(64)
                );
            """
cur.execute(crawling_data)
conn.commit()
cur.execute(card_sales)
conn.commit()

# 크롤링 데이터 입력
csv_file = open("/Users/rjsgk/section3/web_workspace/crawling/navermap_제주 카페",'r',encoding='utf-8',errors="",newline="")
f = csv.reader(csv_file, delimiter=",", doublequote =True, lineterminator="\r\n",quotechar='"', skipinitialspace=True)
header = next(f)

for row in f:
    row = tuple(row)
    sqlString = 'INSERT INTO cafe(name,score,visitor,blog) VALUES (%s,%s,%s,%s);'  #psycopg2 는 format 구문이 안된다?
    cur.execute(sqlString,row) 

conn.commit()


# DB 연결 종료
cur.close()
conn.close()
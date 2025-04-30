# [1단계] 필요 라이브러리 불러오기
from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import pooling
import pandas as pd

# [2단계] .env 파일 로드
load_dotenv(dotenv_path='.env', override=True)

# [3단계] DB 설정값 환경변수에서 불러오기
db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'port': int(os.getenv('MYSQL_PORT')),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE'),
    'charset': os.getenv('MYSQL_CHARSET')
}

# [4단계] 커넥션 풀 생성 (애플리케이션 전체에서 1회만 실행)
connection_pool = pooling.MySQLConnectionPool(
    pool_name=os.getenv('MYSQL_POOL_NAME'),           # 예: mypool
    pool_size=int(os.getenv('MYSQL_POOL_SIZE')),      # 예: 5
    pool_reset_session=True,                          # 세션 초기화 여부
    **db_config
)

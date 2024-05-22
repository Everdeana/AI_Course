# 라이브러리 불러오기
import pymysql
import requests
import datetime

def MemDbDel(idx):
    
    if idx == '': # 인덱스값 존재 여부
        return False
    
    # 데이터 존재 여부 검사 필요

    # DB Setting
    conn = pymysql.connect(
        host     = '127.0.0.1', # == host = 'localhost' --> 자기 자신 의미
        user     = 'mem',
        password = '@ai1234@',
        port     = 3306,
        db       = 'memdb',
        charset  = 'utf8' # 기본 변수들
    )

    try:
               
        cursor = conn.cursor()

        sql = "DELETE FROM member WHERE id = %s"
        val = idx
        cursor.execute(sql, val)
        conn.commit()

    except:
        print("삭제 에러입니다.")
        return False

    finally:
        conn.close()
        return True
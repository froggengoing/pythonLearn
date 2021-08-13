#!/usr/bin/python3

import pymysql
import tushare as ts
import time
import json


#

# # 对于每一行，通过列名name访问对应的元素
# df = pro.stock_basic(offset=0, limit=5, fields='ts_code,symbol,name,area,industry,fullname,enname,cnspell,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
# with connection:
#     with connection.cursor() as cursor:
#         for row in df.iterrows():
#             print(row[1]['ts_code'])
#             sql = "INSERT INTO stock_basic (ts_code,symbol,name,area,industry,fullname,enname,cnspell,market,exchange,curr_type,list_status,list_date,delist_date,is_hs)VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)"
#             cursor.execute(sql, (row[1]['ts_code'],row[1]['symbol'],row[1]['name'],row[1]['area'],row[1]['industry'],row[1]['fullname'],row[1]['enname'],row[1]['cnspell'],row[1]['market'],row[1]['exchange'],row[1]['curr_type'],row[1]['list_status'],row[1]['list_date'],row[1]['delist_date'],row[1]['is_hs']))
#             # connection is not autocommit by default. So you must commit to save
#             # your changes.
#         connection.commit()
#
# connection.close()


def request_commany(offset: int, limit: int):
    ts.set_token("b15cf9fd60dff0d0b1bd08dea0b8c4349d7caae9dad87b1a39568f25")
    pro = ts.pro_api("b15cf9fd60dff0d0b1bd08dea0b8c4349d7caae9dad87b1a39568f25")
    df = pro.stock_basic(offset=offset, limit=limit,
                         fields='ts_code,symbol,name,area,industry,fullname,enname,\
                         cnspell,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
    return df


def get_connection(host: str, user: str, password: str, db: str, ):
    return pymysql.connect(host=host,
                           user=user,
                           password=password,
                           database=db,
                           cursorclass=pymysql.cursors.DictCursor)


def insert_company(conn, companyArray):
    # pysql默认auto commit 为false
    try:
        sql = """INSERT INTO stock_basic (ts_code,symbol,name,area,industry,fullname,enname,cnspell,market,exchange,
        curr_type,list_status,list_date,delist_date,is_hs)
        VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)"""
        with conn.cursor() as cursor:
            for row in companyArray.iterrows():
                print(row[1]['ts_code'])
                sql = "INSERT INTO stock_basic (ts_code,symbol,name,area,industry,fullname,enname,cnspell,market,exchange,curr_type,list_status,list_date,delist_date,is_hs)VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)"
                cursor.execute(sql, (
                row[1]['ts_code'], row[1]['symbol'], row[1]['name'], row[1]['area'], row[1]['industry'],
                row[1]['fullname'], row[1]['enname'], row[1]['cnspell'], row[1]['market'], row[1]['exchange'],
                row[1]['curr_type'], row[1]['list_status'], row[1]['list_date'], row[1]['delist_date'],
                row[1]['is_hs']))
                # connection is not autocommit by default. So you must commit to save
        conn.commit()
    except BaseException as ex:
        print("异常:%s" % ex)
        conn.rollback()

    # finally:
    #     if(curor!=None):
    #         curor.close()


#
def main():
    limit = 200
    leng = 200
    offset = 0

    while (leng == limit):
        print(offset)
        df = request_commany(offset, limit)
        dataFrameArray = df.to_json(orient='table', force_ascii=False)
        datajsonArray = json.loads(dataFrameArray)['data']
        conn = get_connection('localhost', 'root', '123456', 'fgo_stock')
        insert_company(conn, df)
        leng = len(datajsonArray)
        offset += leng
        time.sleep(1)
    conn.close()

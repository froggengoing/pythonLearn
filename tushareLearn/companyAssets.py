#!/usr/bin/python3

import requests
import json
import tushareLearn.company as company
import time


def parseToFloat(rawsStr: str) -> str:
    value = rawsStr.replace('元', '').replace(',', '')
    if (value == ''):
        return '0'
    return value


def generateSql(jsonArray, symbol) -> str:
    if (len(jsonArray) > 0):
        sql = 'insert into company_financial_summary( symbol,'
        for key, value in jsonArray[0].items():
            sql += key + ','
        sql = sql[0:-1] + ') values'
        subSql = ''
        for asset in jsonArray:
            subSql += '('
            subSql += "'" + symbol + "',"
            subSql += "str_to_date('" + asset['date'] + "','%Y-%m-%d'),"
            subSql += parseToFloat(asset['sasset']) + ','
            subSql += parseToFloat(asset['mflow']) + ','
            subSql += parseToFloat(asset['fund']) + ','
            subSql += parseToFloat(asset['fasset']) + ','
            subSql += parseToFloat(asset['flasset']) + ','
            subSql += parseToFloat(asset['total']) + ','
            subSql += parseToFloat(asset['debt']) + ','
            subSql += parseToFloat(asset['mainin']) + ','
            subSql += parseToFloat(asset['fee']) + ','
            subSql += parseToFloat(asset['profits'])
            subSql += '),'
        subSql = subSql[0:-1]
        sql = sql + subSql
    return sql


def getCompany() -> list:
    conn = company.get_connection('localhost', 'root', '123456', 'fgo_stock')
    #market ='主板' and
    sql="""SELECT * FROM stock_basic sb WHERE 
     not exists(select 1 from company_financial_summary where company_financial_summary.symbol = sb.symbol)  
    """
    with conn.cursor() as cursor:
        cursor.execute(sql)
    datalist = cursor.fetchall()
    conn.close()
    return datalist


def insert(sql):
    conn = company.get_connection('localhost', 'root', '123456', 'fgo_stock')
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()
    except BaseException as ex:
        print("异常:%s" % ex)
        conn.rollback()
    conn.close()


def request_company_asset(symbol):
    url = 'http://ig507.com/data/time/f10/fs/{}?licence=3CB63E38-891C-C570-7AE9-54987A400664'
    companyUrl = url.format(symbol)
    res = requests.get(companyUrl)
    if (res.status_code == 200):
        try:
            return json.loads(res.content)
        except Exception as ex:
            print(res.content)
            print(ex)
        return None
    else:
        print(res.content)
        return []


def main():
    company_list = getCompany()
    count = 0
    for cp in company_list:
        sy = cp['symbol']
        print(str(count) + "=>" + sy)
        cpData = request_company_asset(sy)
        if (cpData != None):
            sql = generateSql(cpData, sy)
            insert(sql)
        time.sleep(2)
        count += 1


main()

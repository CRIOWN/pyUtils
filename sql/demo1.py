import pymysql

if __name__ == '__main__':
    try:
        db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
        print("connect success")
    except:
        print("connect error")
    cursor = db.cursor()
    # insert into test.swaggerdata(tags, summary, url, xorder)
    # values ('第三方接口','支付宝支付','/third/alipay/pay','2147483647')
    tags = 'tags'
    summary = 'summary'
    xorder = 'x-order'
    url = "url:8080"
    sql = "Insert into test.swaggerdata(tags, summary, url, xorder) " \
          "values ('{tags}','{summary}','{url}','{xorder}')".format(tags=tags, summary=summary, url=url, xorder=xorder)
    try:
        cursor.execute(sql)
        db.commit()
        print("success")
    except:
        db.rollback()
        print("Error")
    db.close()

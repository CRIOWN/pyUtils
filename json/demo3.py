if __name__ == '__main__':
    url = "url00"
    tags = 'tags0'
    summary = 'summary00'
    xorder = 'x-order00'
    sql = "Insert into test.swaggerdata(tags, summary, url, xorder) " \
          "values ({tags},{summary},{url},{xorder})".format(tags= tags, summary= summary, url= url,xorder= xorder)
    print(sql)
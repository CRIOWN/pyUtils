import json
import pymysql

if __name__ == '__main__':
    # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    filename = "../data/code2Session.json"
    mutifilename = "../data/wanfang-service-third_OpenAPI.json"
    try:
        db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
        print("connect success")
    except:
        print("connect error")
    cursor = db.cursor()

    with open(mutifilename, encoding='utf-8') as f:
        data = json.load(f)
        paths = data['paths']
        for url in paths:
            print("url路径::", url)  # url路径
            for method in paths[url]:
                # get/post 内容
                # print(paths[key][method])
                tags = ''.join(paths[url][method]['tags'])  # 分组标签
                summary = paths[url][method]['summary']  # 描述
                xorder = paths[url][method]['x-order']  #排序依据 越小越靠前
                print("tags:", tags)
                print("summary:", summary)
                print("x-order", xorder)
                sql = "Insert into test.swaggerdata(tags, summary, url, xorder) " \
                      "values ('{tags}','{summary}','{url}','{xorder}')".format(tags=tags, summary=summary, url=url,
                                                                                xorder=xorder)
                cursor.execute(sql)
            print("=="*5)
    db.commit()
    db.close()





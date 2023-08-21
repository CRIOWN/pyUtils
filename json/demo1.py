import json

if __name__ == '__main__':
    filename = '../data/test1.json'
    with open(filename) as f:
        jsdata = json.load(f)  # 装载json

    for msg in jsdata:
        cName = msg['Country Name']
        cCode = msg['Country Code']
        Year = msg['Year']
        Value = msg['Value']
        print(cName, ":", cCode, ":", Year, ":", Value)

import pymysql
db = pymysql.connect(host="192.168.192.21",user="root",password="beimai2014",db="test")
cursor = db.cursor()
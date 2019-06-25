import csv

with open('cike.csv','a')as f:
    #初始化写入对象
    writer = csv.writer(f)
    #把列表写入文件中
    writer.writerow(['荆轲','李白'])
    writer.writerow(['孙悟空', '兰陵王'])
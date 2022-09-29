# f = open("hello.txt",'a+')
# item = f.read()

# print(item)
# for c in item:
#     print(c)
# print(f.readline())
# print(f.readlines())

# f.write("\n\"eeeeee\"")

# f.close()

# import pandas as pd

# x = [[1,2,3],[4,5,6],[7,8,9]]

# from xml.etree.ElementTree import TreeBuilder
# import pandas as pd
   
# # 三个字段 name, site, age
# nme = ["Google", "Runoob", "Taobao", "Wiki"]
# st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
# ag = [90, 40, 80, 98]
   
# # 字典
# dict = {'name': nme, 'site': st, 'age': ag}
     
# df = pd.DataFrame(dict)
 
# # 保存 dataframe
# df.to_csv('site.csv')


def func():
    while True:
        try:
          x = int(input("enter:"))
          y = int(input("enter:"))
          return x/y
        except:
            print("error") 

            
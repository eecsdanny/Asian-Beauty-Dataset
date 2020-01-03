import urllib.parse
import urllib.request
import os
import pandas as pd
import ast

record = pd.read_csv('img_url_history.csv')

information = list()
for info in record['0']:
    information.append(ast.literal_eval(info))

links = list()
for link in record['1']:
    links.append(eval(link))

os.mkdir('ABD')
def save_pics(information,links):
    num = len(information)
    for index in range(num):
        info = information[index]
        urls = links[index]
        dirname = 'ABD/'+info['author']+info['date']
        try:
            os.mkdir(dirname)
        except:
            print('dir exists')
        local_count = 0
        for url in urls:
            try:
                urllib.request.urlretrieve(url, dirname+"/"+str(local_count)+".jpg")
                local_count = local_count + 1
            except:
                print("flie not found or not a jpg file")
        print(info['title']+' done, count: ',index)
save_pics(information,links)



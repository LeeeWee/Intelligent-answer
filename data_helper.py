import os
import math
import pandas as pd
import csv

def save_all_questions(input, output):
    d = dict()
    train_df = pd.read_csv(input)
    
    for i in range(len(train_df['id'])):
        if i % 10000 == 0:
            print(str(i) + ' lines handled.')
        orId = int(train_df['orId'][i])
        dqId = int(train_df['dqId'][i])
        orTitle = train_df['orTitle'][i]
        dqTitle = train_df['dqTitle'][i]
        orBody = train_df['orBody'][i]
        dqBody = train_df['dqBody'][i]
        if not d.get(orId):
            d[orId] = [orTitle, orBody]
        if not d.get(dqId):
            d[dqId] = [dqTitle, dqBody]
    print("total " + str(len(d)) + " questions.")
    with open(output, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id','qid','title','body'])
        id = 0
        for key in d:
            id += 1
            if id % 10000 == 0:
                print(str(id) + " lines writed.")
            title = d[key][0]
            if isinstance(title, float):
                title = ''
            body = d[key][1]
            if isinstance(body, float):
                body = ''
            row = [str(id), str(key), title.strip(), body.strip()]
            writer.writerow(row)

if __name__ == '__main__':
    input = '最新待测试train.csv'
    output = 'questions.csv'
    save_all_questions(input, output)


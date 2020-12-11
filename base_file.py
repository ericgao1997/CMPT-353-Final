import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys



def main(data_file):
    data = pd.read_json(data_file, lines=True) 
    bulk = data.drop(['tags'], axis=1)
    tags = pd.json_normalize(data['tags'])
    tags = tags.applymap(lambda x: int(False == pd.isnull(x)))
    flat_d = pd.concat([bulk, tags], axis=1, sort=False)
    print(flat_d)
    flat_d.to_csv('out/tag_cleaned.csv',index=False)
    with open("out/tags.txt", mode='w',encoding='utf-8') as outfile:
        for col in tags.columns: 
            outfile.write(col+"\n")

if __name__=='__main__':
    data_file = sys.argv[1]
    main(data_file,)         
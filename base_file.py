import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys



def main(data_file):
    data = pd.read_csv(data_file,header=True) 
    
    # bulk = data.drop(['tags'], axis=1)
    # tags = pd.json_normalize(data['tags'])
    tags = data[['food','medical','gathering','transport','notable']]
    tags = tags.applymap(lambda x: int(x))
    data[['food','medical','gathering','transport','notable']] = tags
    sample = data.sample(frac=0.25).reset_index(drop=True)
    sample.to_csv('training_data.csv',index=False)

    # flat_d = pd.concat([bulk, tags], axis=1, sort=False)
    # print(flat_d)
    # bulk.to_csv('out/to_rate.csv',index=False)
    # flat_d.to_csv('out/tag_cleaned.csv',index=False)
    # with open("out/tags.txt", mode='w',encoding='utf-8') as outfile:
    #     for col in data.columns: 
    #         outfile.write(col+"\n")

if __name__=='__main__':
    data_file = sys.argv[1]
    main(data_file,)         
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import sys

def give_rating(row, ratings):
    return ratings[row['amenity']]*len(row['tags'])

def main(data_file, rating_file):
    data = pd.read_json(data_file, lines=True) 
    with open(rating_file, mode='r',encoding='utf-8') as infile:
        reader = csv.reader(infile)
        ratings = {rows[0]:int(rows[1]) for rows in reader}
    print (ratings)
    data['risk'] = data.apply(lambda row: give_rating(row,ratings), axis=1)
    data = data[data['risk']>1]
    print(data['amenity'],data['risk'])
    data = data.drop('tags', axis=1)
    data.to_csv("basic_risk.csv",index=False)

if __name__=='__main__':
    data_file = sys.argv[1]
    rating_file = sys.argv[2]
    main(data_file, rating_file)         
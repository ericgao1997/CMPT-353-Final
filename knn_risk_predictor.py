import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import sys

neigh = KNeighborsRegressor(n_neighbors=6, weights='distance')
wider_neigh = KNeighborsRegressor(n_neighbors=50, weights='distance')

def risk_calc(row):
    base_risk = row['medical'] + row['food']*0.8 + row['gathering']*0.5 + row['transport']*0.5 + row['notable']*0.2
    if base_risk == 0:
        return 0
    # t_total = row['medical'] + row['food'] + row['gathering']+ row['transport'] + row['notable']
    t_total = 1
    return base_risk**t_total

def irl_risk(model):
    irl_cases = pd.read_csv("data/confirmed_cases.csv") 
    irl_cases['risk'] = model.predict(irl_cases)
    irl_cases.to_csv("out/irl_risk.csv")

def main(data_file):
    data = pd.read_csv(data_file) 
    data['risk'] = data.apply(lambda row: risk_calc(row),axis=1)
    data['risk'] = data.apply(lambda x: x['risk']/data['risk'].max(), axis=1)
    print (data)
    targets = data[(data['risk']==0) & (data['tag_count']>0)]

    known = data[~data.isin(targets)]
    known = known[known['lat'].notna()]
    print(len(known))
    print(len(targets))
    X = known[['lat','lon']]
    y = known['risk']
    neigh.fit(X,y)

    print (targets)
    X_t = targets[['lat','lon']]
    targets['risk'] = neigh.predict(X_t) 
    # * neigh.predict_proba(targets[['lat','lon']])

    indv_models = pd.concat([known,targets])
    indv_models.to_csv('out/checked_risks.csv',index = False)
    # print (indv_models)

    new_targets = indv_models[(indv_models['risk']==0)]
    known_2 = indv_models[~indv_models.isin(new_targets)]
    known_2 = known_2[known_2['lat'].notna()]
    wider_neigh.fit(known_2[['lat','lon']],known_2['risk'])
    new_targets['risk'] = wider_neigh.predict(new_targets[['lat','lon']]) 
    overall_risks = pd.concat([known_2,new_targets])

    overall_risks.to_csv('out/smart_risks.csv',index = False)

    irl_risk(wider_neigh)
    # print (overall_risks)
    # targets = data[ (data['food']==False) | (data['medical']==False) | (data['gathering']==False) | (data['transport']==False) | (data['notable']==False)  ]
    # targets = targets[targets['tag_count']>0]
    
if __name__=='__main__':
    data_file = sys.argv[1]
    main(data_file,)         
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def tag_untag(data):
    untagged = data[data['tag_count']==0]['risk']
    # print (untagged)
    tagged = data[data['tag_count']!=0]
    tagged = tagged.rename(columns={'risk':'tagged_risk'})
    tagged = tagged['tagged_risk']

    plt.hist(tagged, 12, alpha=0.5, label='tagged_risk')
    plt.hist(untagged, 12, alpha=0.5, label='untagged_risk')
    plt.legend(loc='upper right')
    plt.ylabel('number of landmarks')
    plt.xlabel('risk of covid exposure (0-1)')
    plt.title('Distribution of risk of tagged and untagged landmarks.')
    plt.savefig('figures/tag_untag_risk.png')   
    plt.clf()
    return

def risk_vs_tags(data):
    plt.scatter(data['tag_count'], data['risk'], label='risk to tags')
    plt.ylabel('risk (0-1)')
    plt.xlabel('# of tags')
    plt.title('Range of risks to # of tags.')
    plt.savefig('figures/risk-tag-range.png')   
    plt.clf()
    return

def main(data_file):
    data = pd.read_csv(data_file,header=0) 
    tag_untag(data)
    risk_vs_tags(data)

if __name__=='__main__':
    data_file = sys.argv[1]
    main(data_file,)         
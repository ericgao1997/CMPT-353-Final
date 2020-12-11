import sys, string, re
from pyspark.sql import SparkSession, functions, types
from pyspark.sql.functions import *
from scipy import stats

spark = SparkSession.builder.appName('datacleaning').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')
# {OFF, FATAL, ERROR, WARN, INFO, DEBUG, TRACE, ALL}

assert sys.version_info >= (3, 5)
assert spark.version >= '2.3'


# python3 datainsight.py data/amenities-vancouver.csv data/tag-data.csv

def main(amenity_input, tag_input):
  data = spark.read.csv(amenity_input)
  tags = spark.read.csv(tag_input)
  
  print(
  """
  ### DATA INSIGHT ###

  # takes 2 input pandas dataframes and creates summary graphs
  # used to illustrate vcarious traits of the data
  # as well as effectiveness of our assumptions
  """
  )
  # chi-square tests useful as the majority of our data is categorical
  # we check p values to verify correlation between tags and notability
  data.show()
  tags.show()
  
if __name__=='__main__':
  amenity_input = sys.argv[1]
  tag_input = sys.argv[2]
  main(amenity_input, tag_input)         
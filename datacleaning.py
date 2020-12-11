import sys, string, re
from pyspark.sql import SparkSession, functions, types
from pyspark.sql.functions import *


spark = SparkSession.builder.appName('datacleaning').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')
# {OFF, FATAL, ERROR, WARN, INFO, DEBUG, TRACE, ALL}

assert sys.version_info >= (3, 5)
assert spark.version >= '2.3'

OUTPUT_DIRECTORY = "out"

# python3 datacleaning.py osm/amenities-vancouver.json.gz

def main(input_file):
  data = spark.read.json(input_file)
  # json of form in SCHEMA.txt
  # https://wiki.openstreetmap.org/wiki/Tags
  # off the top of my head, I imagine tags we'd keep are something like:

  # tagsample = data[s]
  
  data.printSchema()
  # flat = 
  # data.write.option("header", "true").mode("overwrite").csv(OUTPUT_DIRECTORY)

  # TODO
  
  
if __name__=='__main__':
  input_file = sys.argv[1]
  main(input_file)         
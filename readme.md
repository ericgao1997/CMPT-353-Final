#OSM, Photos, and Tours
This is our final submission for CMPT, in which we [TBA]

##Usage
###Samples
WIP

###Full Demo
To run the whole thing locally, start to finish, using the [`amenities-vancouver.json.gz`]:https://coursys.sfu.ca/2020fa-cmpt-353-d1/pages/ProjectTourData data sample from the assignment page: 
```
# Cleans the base data and expands each location's tags before saving them as a csv.
python datacleaning.py osm/amenities-vancouver.json.gz 
# Runs the rest of the model creation, stats tests and data analysis. outputs then to /out and /data
python knn_risk_predictor.py data/amenities-vancouver.csv 
```

##Requirements
* Python 3.5+
* Spark 2.3+
* Scipy
* Sklearn
* Matplotlib

WIP

# **Setup**

First make sure that you have **Python3** installed!

run the commands:
```
#!cmd
cp config.temp.py config.py;
pip3 install numpy
pip3 install flask
pip3 install PyMySQL
```
Then edit `config.py`, by setting the right credentials for the Databse.
Lastly run:
```
#!cmd
python3 server.py
```
or
```
#!cmd
python server.py
```
or
```
#!cmd
pm2 start server.py --interpreter=python3
```
# **Current Endpoints**
## **GET** Weights: `/weights?tblname=<table-name>`
### Variables
* `<table-name>`: the mysql table name that belongs to the given contact
### Return Value
Will return a csv-style table with the respected weights for each indicator, their name, their level, and the contact they belong to.
Formatted as such:
```
   <contact>,<indicator-level>,<indicator-name>,<weight>
```
For example:
```
+16474217106,W2,hidden0,-1.5364521315223774,
+16474217106,W2,hidden1,-0.8427647033977645,
+16474217106,W2,hidden2,-1.282721525684368,
+16474217106,W2,hidden3,-1.2229838819074106,
+16474217106,W2,hidden4,-1.3161497175417665,
+16421417106,W2,hidden0,1.1189239323243267,
+16442117106,W2,hidden1,1.0039927366479966,
```
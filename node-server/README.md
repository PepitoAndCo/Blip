# **Setup**

First make sure that you have Node-JS installed!

run the commands:
```
#!cmd
cp config.temp.js config.js;
npm install
```
Then edit `config.js`, by setting the right credentials for the Databse.
Lastly run:
```
node .
```
or
```
nodemon .
```
or
```
pm2 start .
```

# **Current Endpoints**
## **POST** Send-Text `/send_text?id=<user-id>&type=<acc-type>`
This endpoint will store the text messages that are in body into a given database.
### Variables
* `<user-id>`: the users unique id, for google accounts its their google_id for generic it will be a unique key assigned to them (or for now just their phone number) 
* `<acc-type>`: defaults to `generic`, can be either `google` or `generic`.
### Body
The body of this message should be a csv-style message.
It should be formatted as such:
```
<contact-number>,<time>,<message>
```
for example:
```
+1 647-399-8552,1457293780747,Im sorry its last minute 
(416) 321-6244,1457282706263,Ok
(647) 722-4546,1457275477531,Thanks xD 
+1 647-444-9095,1457238951322,whats up man?
+1 416-900-4099,1457225227187,Yes I am
```
## **GET** Weights: `/weights?id=<user-id>?type=<acc-type>`
### Variables
* `<user-id>`: the users unique id, for google accounts its their google_id for generic it will be a unique key assigned to them (or for now just their phone number) 
* `<acc-type>`: defaults to `generic`, can be either `google` or `generic`.
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
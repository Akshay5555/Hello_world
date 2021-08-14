# Hello_world

A flask app which takes in input from user about their S3 account Details for creation of bucket and storing log files for our MyTD Service.

Download Code from the Repository.

GitHub Link : https://github.com/Akshay5555/Hello_world

Pre Requisites for running the script :
1) Python 3
2) Programmatic Access to IAM User on AWS


Clone Repository in VS Ccode or any Code Editor of your choice.

#Activate python virtual environment 
cd {folder}
source venv/src/activate

# Try running the app through Terminal 
export BUCKETNAME=my-td-service-bucket
export AWS_ACCESS_KEY_ID={AWS ACCESS KEY} 
export AWS_SECRET_ACCESS_KEY={AWS SECRET KEY}
python HelloWorld.py

Test Resp Api's , 
1) / - Default
2) /new - Post Api Which would get our data from api , fecth output , store the logs in S3 Bucket 

Test Out log file creation in S3

# Dockerise the app
docker build -t {ImageName} .        // It will take some time , Approx 10 mins

# Run the Docker App
docker run -e BUCKETNAME={BUCKET NAME} -e AWS_ACCESS_KEY_ID={AWS ACCESS KEY} -e AWS_SECRET_ACCESS_KEY={AWS SECRET KEY} {ImageName} HelloWorld.py

Test the Api's again.

##### If you are using VS code , Download extension Thunderbird , Similar product to Postman but lighter and faster.

from flask import Flask
from os import environ
import io
import boto3
import pandas as pd
import numpy as np
from flask import request, jsonify
import json
from datetime import datetime


app = Flask(__name__)

bucket_name = environ.get('BUCKETNAME')
AWS_ACCESS_KEY_ID = environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = environ.get("AWS_SECRET_ACCESS_KEY")


@app.route('/' ,  methods=['GET'])
def hello():
    return 'Hello From myTD Service !'

@app.route('/new', methods=['POST' , 'GET'])
def newProject():
    client = boto3.client(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY ,
        region_name = 'us-east-1'
    )
    clientResponse = client.list_buckets()
    # print('Printing bucket names...')
    bucketArray = []
    for bucket in clientResponse['Buckets']:
        bucketArray.append(bucket["Name"])
        # print(f'Bucket Name: {bucket["Name"]}')
    if bucket_name not in bucketArray:
        ##Creat a new bucket 
        # location = {'LocationConstraint': 'us-east-1'}
        client.create_bucket(
            Bucket=bucket_name
        )
#     record = json.loads(request.data)
#     id = record['input']['Id']
#     Age = record['input']['Age']
    Age = 23
    id = "127"
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    logId = id + "_" + str(Age) + str(dt_string)
    data=np.array([[logId , "Output Value" , str(record)]])
    logs_df = pd.DataFrame(
        data,
        columns=[["Log Id", "Input_json", "Output_Json"]],
    ).reset_index()
    # print(logs_df)
    with io.StringIO() as csv_buffer:

        # obj = client.get_object(Bucket=bucket_name, Key='files/logs.csv')
        # allLogs_df = pd.read_csv(obj['Body']).reset_index(drop=True)
        # allLogs_df =allLogs_df.append(logs_df).reset_index()
        # allLogs_df.to_csv(csv_buffer, index=False)

        logs_df.to_csv(csv_buffer, index=False)
        fileName = "files/" + logId + ".csv"

        response = client.put_object(
            Bucket=bucket_name, Key=fileName, Body=csv_buffer.getvalue()
        )

        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

        if status == 200:
            print(f"Successful S3 put_object response. Status - {status}")
        else:
            print(f"Unsuccessful S3 put_object rbooks_esponse. Status - {status}")

    return 'Excited for the new project, Logs Stored Successfully in S3 Bucket defined !'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 80, debug = True)



## Takes input as json and outputs of allocation from the model (Dummy data for now)

## For every request and response hit ,
# Write it back into s3 , $ things : unique Id , date , time , mins , status.



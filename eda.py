import boto3
from bson import json_util
import json

comprehend = boto3.client("comprehend")
# oms_text = Path('HemingwayBook/OldManSeaBook.txt').read_text()[:3000]
# response = client.detect_sentiment(Text=oms_text,LanguageCode='en')
# print(response)
number_of_topics = 15
#input_s3_url= "s3://aws-topic-modeling/input/input.txt"
input_s3_url="s3://aws-topic-modeling/input/input_MWW.txt"
input_s3_url="s3://aws-topic-modeling/input/input_SAR.txt"
input_doc_format = "ONE_DOC_PER_LINE"
output_s3_url= "s3://aws-topic-modeling/output/"
data_access_role_arn = "arn:aws:iam::740656944786:role/service-role/AmazonComprehendServiceRole-inandout2"

input_data_config = {"S3Uri": input_s3_url, "InputFormat": input_doc_format}
output_data_config = {"S3Uri": output_s3_url}

start_topics_detection_job_result = comprehend.start_topics_detection_job(NumberOfTopics=number_of_topics,
                                                                              InputDataConfig=input_data_config,
                                                                              OutputDataConfig=output_data_config,
                                                                              DataAccessRoleArn=data_access_role_arn)
 
print('start_topics_detection_job_result: ' + json.dumps(start_topics_detection_job_result))
 
job_id = start_topics_detection_job_result["JobId"]
 
print('job_id: ' + job_id)
 
describe_topics_detection_job_result = comprehend.describe_topics_detection_job(JobId=job_id)
 
print('describe_topics_detection_job_result: ' + json.dumps(describe_topics_detection_job_result, default=json_util.default))
 
list_topics_detection_jobs_result = comprehend.list_topics_detection_jobs()
 
print('list_topics_detection_jobs_result: ' + json.dumps(list_topics_detection_jobs_result, default=json_util.default))
 
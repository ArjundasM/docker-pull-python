import fileinput
import boto3
import docker
import os
from botocore.exceptions import ClientError

#Downloading location
file_location='/tmp/sample'

#Get environment variables
bucket_name = os.getenv('BUCKET_NAME')
file_name   = os.getenv('FILE_PATH')

#Creating AWS S3 client
s3 = boto3.client('s3')

#Downloading file from s3
try:
  s3.download_file(bucket_name, file_name, file_location)
except ClientError as e:
  print(e)
  quit()

#Remove empty lines, if any
for line in fileinput.FileInput(file_location,inplace=1):
  if line.strip():
    print(line)

#Get image name from the file
with open(file_location) as f:
  value = f.readline().strip()

#Function to pull docker image
def dockerPull(name):
  
  #Creating docker client
  client = docker.from_env()

  #Condition to check whether image name present or not in the downloaded file
  if (not name):
    print("\nImage name not found in 's3://{0}/{1}' file\n".format(bucket_name, file_name))
    quit()
  #Condition to check whether the image name ending with just ':'
  elif name.endswith(":") == True :
    print("Invalid image name, ending with ':', Please provide correct tag")
  else:
    try:
      print("\nDownloading {0} image".format(value))
      image = client.images.pull(value)
      print("{0} image downloaded Successfully".format(value))
    except docker.errors.APIError as e:
      print(e)

#call docker pull function
dockerPull(value)
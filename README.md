# PYTHON SCRIPT TO DOWNLOAD DOCKER IMAGE
Simple python programe to download a docker image which is specified in a file in s3 Bucket.

## Prerequisite

- Supported python versions: Python3.6+


## Setup instructions

1.Clone this repo into your machine
```
git clone https://github.com/ArjundasM/docker-pull-python.git
```

2.Install required python packages

```
cd docker-pull-python
python3 -m pip install -r requirements.txt
```

3.Update and export following environtment variables
```
export AWS_ACCESS_KEY_ID=<aws account access key>
```
```
export AWS_SECRET_ACCESS_KEY=<aws account secret key>
```
```
export BUCKET_NAME=<s3 bucket name>
```
```
export FILE_PATH=<s3 object path>
```
e.g., - S3 URL=s3://bucketname/folder1/file, then FILE_PATH=folder1/file
      - S3 URL=s3://bucketname/file, then FILE_PATH=file

4.Run the script

```
python3 main.py
```

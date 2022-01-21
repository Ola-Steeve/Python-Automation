import boto3
import os
import paramiko
import requests
import time

# get all the env vars set in Jenkinsfile
repo_name = os.environ['ECR_REPO_NAME']
ssh_host = os.environ['EC2_SERVER']
ssh_user = os.environ['EC2_USER']
ssh_privat_key_path = os.environ['SSH_KEY']

docker_registry = os.environ['DOCKER_REGISTRY']
docker_user = os.environ['DOCKER_USER']
docker_pwd = os.environ['DOCKER_PWD']
docker_image = os.environ['DOCKER_IMAGE'] # selected by user in Jenkins 
container_port = os.environ['CONTAINER_PORT']

ecr_client = boto3.client('ecr')

# Fetch all 3 images from ECR repo
images = ecr_client.describe_images(repositoryName=repo_name)

image_tags = []
for image in images['imageDetails']:
    image_tags.append(image['imageTags'][0])

# SSH into the EC2 server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ssh_host, username=ssh_user, key_filename=ssh_privat_key_path)

stdin, stdout, stderr = ssh.exec_command(f"echo {docker_pwd} | docker login {docker_registry} --username {docker_user} --password-stdin")
print(stdout.readlines())
stdin, stdout, stderr = ssh.exec_command(f"docker run -p {container_port}:{container_port} -d {docker_image}")
print(stdout.readlines())

ssh.close()

# Validate the application started successfully
try:
    # give the app some time to start up
    time.sleep(30) 
    
    response = requests.get(f"http://{ssh_host}:{container_port}")
    if response.status_code == 200:
        print('Application is running successfully!')
    else:
        print('Application deployment was not successful')
except Exception as ex:
    print(f'Connection error happened: {ex}')
    print('Application not accessible at all')
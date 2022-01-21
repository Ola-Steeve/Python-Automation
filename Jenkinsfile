#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        ECR_REPO_NAME = 'java-app'
        EC2_SERVER = '52.47.203.210'
        EC2_USER = 'ec2-user'
        SSH_KEY = credentials('ssh-creds')

        ECR_REGISTRY = '664574038682.dkr.ecr.eu-west-3.amazonaws.com'

        AWS_ACCESS_KEY_ID = credentials('jenkins_aws_access_key_id')
        AWS_SECRET_ACCESS_KEY = credentials('jenkins_aws_secret_access_key')
        AWS_DEFAULT_REGION = 'eu-west-3'
    }
    stages {
        stage('select image version') {
            steps {
               script {
                  echo 'fetching available image versions'
                  def result = sh(script: 'python3 test-get-images.py', returnStdout: true).trim()
                  // split returns an Array, but choices expects either List or String, so we do "as List"
                  def tags = result.split('\n') as List
                  version_to_deploy = input message: 'Select version to deploy on TEST', ok: 'Deploy', parameters: [choice(name: 'Select version', choices: tags)]
                  env.DOCKER_IMAGE = "${ECR_REGISTRY}/${ECR_REPO_NAME}:${version_to_deploy}"
                  echo env.DOCKER_IMAGE
               }
            }
        }
        stage('deploying image') {
            steps {
                script {
                   echo 'deploying docker image to EC2...'

                }
            }
        }
    }
}

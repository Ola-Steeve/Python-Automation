#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        ECR_REPO_NAME = 'java-app'
        EC2_SERVER = '52.47.203.210'
        EC2_USER = 'ec2-user'

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
                  def tags = result.split('\n') as List
                  env.VERSION_TO_DEPLOY = input message: 'Select version to deploy on TEST', ok: 'Deploy', parameters: [choice(name: 'Select version', choices: tags)]
                  echo env.VERSION_TO_DEPLOY
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

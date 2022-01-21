#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        ECR_REPO_NAME = 'java-app'
        EC2_SERVER = '52.47.203.210'
        EC2_USER = 'ec2-user'
        SSH_KEY = credentials('ec2-ssh-key')
    }
    stages {
        stage('select image version') {
            steps {
               script {
                  echo 'selected image version'
                  result = sh(script: 'python3 test-get-images.py', returnStdout: true).trim()
                  echo result
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

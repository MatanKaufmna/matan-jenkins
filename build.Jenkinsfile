pipeline {
    agent any

    environment {
        REGISTRY_URL = '700935310038.dkr.ecr.us-west-2.amazonaws.com'
        IMAGE_NAME = 'matan-jenkins'
    }

    stages {
        stage('Build') {
            steps {
                sh '''

                aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin $REGISTRY_URL
                docker build -t $IMAGE_NAME:$BUILD_NUMBER .
                docker tag $IMAGE_NAME:$BUILD_NUMBER $REGISTRY_URL /$IMAGE_NAME:latest
                docker push $REGISTRY_URL/$IMAGE_NAME:$BUILD_NUMBER
                '''

                }
            }
        }
    }
}


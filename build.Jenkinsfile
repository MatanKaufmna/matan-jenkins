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
                docker build -t $IMAGE_NAME .
                docker tag $IMAGE_NAME:latest $REGISTRY_URL /$IMAGE_NAME:latest
                docker push $REGISTRY_URL/$IMAGE_NAME:latest
                '''
            }
            post {
                always {
                    sh 'docker image prune -a --filter "until=240h" --force '
                }
            }
        }
    }
}

stage('Trigger Deploy') {
    steps {
        build job: 'AppDeploy', wait: false, parameters: [
            string(name: 'YOLO5_IMAGE_URL', value: "700935310038.dkr.ecr.us-west-2.amazonaws.com")
        ]
    }
}
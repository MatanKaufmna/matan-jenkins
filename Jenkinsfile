pipeline {
    agent any

    environment {
        REGISTRY_URL = '700935310038.dkr.ecr.us-west-2.amazonaws.com'
        IMAGE_NAME = ' matan-jenkins '
    }

    stages {
        stage('Buildd') {
            steps {
                sh '''
                aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 700935310038.dkr.ecr.us-west-2.amazonaws.com
                docker build -t matan-jenkins .
                docker tag matan-jenkins:latest 700935310038.dkr.ecr.us-west-2.amazonaws.com/matan-jenkins:latest
                docker push 700935310038.dkr.ecr.us-west-2.amazonaws.com/matan-jenkins:latest
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
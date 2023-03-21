pipeline {
   agent {
        docker {so
        image '700935310038.dkr.ecr.us-west-2.amazonaws.com/matan-jenkins-agent:1'
        args  '--user root -v /var/run/docker.ck:/var/run/docker.sock'
        }
   }



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
                '''

//                 withCredentials([
//                     string(credentialsId: 'snyk_token', variable: 'SNYK_TOKEN')
//                 ]) {
//                     sh '''
//                       snyk container test $IMAGE_NAME:$BUILD_NUMBER --severity-threshold=high --file=Dockerfile
//                     '''
//                 }


                sh '''
                docker tag $IMAGE_NAME:$BUILD_NUMBER $REGISTRY_URL/$IMAGE_NAME:$BUILD_NUMBER
                docker push $REGISTRY_URL/$IMAGE_NAME:$BUILD_NUMBER
                '''
            }
            post {
               always {
                   sh 'docker image prune -a --filter "until=240h" --force'
               }
            }
        }

stage('Trigger Deploy') {
            steps {
                build job: 'AppDeploy', wait: false, parameters: [
                    string(name: 'YOLO5_IMAGE_URL', value: "$REGISTRY_URL/$IMAGE_NAME:$BUILD_NUMBER")
                ]
            }
        }
    }
}
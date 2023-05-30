pipeline {
    agent {
        docker {
        image '700935310038.dkr.ecr.us-west-2.amazonaws.com/matan-jenkinsagent-cicd:1'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                echo "Build Dependencies"
                cd 15_fantastic_ascii
                pip install -r requirements.txt --admin

                '''
            }
        }

        stage('Build') {
            steps {


                sh '''
                echo "Nexus Integration Build"
                cd 15_fantastic_ascii
                python3 -m build
                '''
            }
        }
        stage('Publish') {
           steps {
                withCredentials([usernamePassword(credentialsId: 'matan_nexus', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')
              ]) {

                sh '''
                cd 15_fantastic_ascii
                echo $USERNAME
                echo $PASSWORD
                sed -i -e "s/<username>/$USERNAME/g" .pypirc
                sed -i -e "s/<password>/$PASSWORD/g" .pypirc
                python3 -m twine upload --config-file .pypirc --repository pypi-hosted dist/*
                '''
              }
            }
        }
    }
    post {
        cleanup {
            cleanWs()
        }
    }
}
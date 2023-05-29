pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            step{
                sh '''
                echo "Build Dependencies"

                pip3 install build twine

                '''
            }
        }

        stage('Build') {
            steps {
                 
                sh '''
                echo "Nexus Integration Build"
                python3 -m build
                '''
            }
        }
        stage('Publish') {
           steps {
                withCredentials([usernamePassword(credentialsId: 'nexus', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')
              ]) {

                sh '''
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
}
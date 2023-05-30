pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                echo "Build DependencieS"
                pip3 install build twine
                pip3 install urllib3==1.26.6

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
                withCredentials([usernamePassword(ID:'matan_nexus', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')
              ]) {

                sh '''
                cd 15_fantastic_ascii
                python3 -m twine upload --config-file .pypirc --repository pypi-hosted dist/*
                '''
              }
            }
        }
    }
}
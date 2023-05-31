pipeline {
    agent any


    stages {
        stage('Install dependencies') {
            steps {
                script {
                sh "echo 'Build Dependencies'"
                sh "cd 15_fantastic_ascii"
                def nexusUrl = 'http://35.90.150.243:8081/repository/general-pypi/'
                def nexusCredentialsId = 'matan-nexus'

                    withCredentials([usernamePassword(credentialsId: matan-nexus, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh "pip install --index-url=${http://35.90.150.243:8081/#browse/welcome} --trusted-host http://35.90.150.243:8081/repository/general-pypi/' --user --upgrade pip"
                        sh "pip install --index-url=${http://35.90.150.243:8081/#browse/welcome} --trusted-host http://35.90.150.243:8081/repository/general-pypi/' --user -r requirements.txt"
                sh '''
                echo "Build Dependencies"
                cd 15_fantastic_ascii

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
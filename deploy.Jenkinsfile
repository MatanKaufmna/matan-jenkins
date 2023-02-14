pipeline {
    agent any

    parameters {
     parameters { string(name: '700935310038.dkr.ecr.us-west-2.amazonaws.com', defaultValue: '', description: '') }

    }

    stages {
        stage('Deploy') {
            steps {
                sh 'echo 700935310038.dkr.ecr.us-west-2.amazonaws.com'
                sh '# kubectl apply -f ....'

            }
        }
    }
}
pipeline {
    agent any

    parameters {
     parameters { string(name: 'YOLO5_iMAGE_URL', defaultValue: '', description: '') }

    }

    stages {
        stage('Deploy') {
            steps {
                sh '$YOLO5_iMAGE_URL'
                sh '# kubectl apply -f ....'

            }
        }
    }
}
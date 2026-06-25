pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code downloaded from GitHub'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t salary-predictor .'
            }
        }

        stage('Show Images') {
            steps {
                sh 'docker images'
            }
        }
    }
}
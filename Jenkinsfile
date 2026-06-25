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
                sh 'docker --version'
            }
        }
    }
}
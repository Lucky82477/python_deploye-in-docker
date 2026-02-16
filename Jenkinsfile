pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/Lucky82477/python_deploye-in-docker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-add-app:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f python-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name python-container python-add-app:latest'
            }
        }
    }
}

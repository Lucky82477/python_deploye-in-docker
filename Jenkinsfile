pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-ec2-app"
        CONTAINER_NAME = "python_app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Lucky82477/jenkin-ci-cd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f $CONTAINER_NAME || true'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker run -d \
                --name $CONTAINER_NAME \
                -p 5000:5000 \
                $IMAGE_NAME:latest
                '''
            }
        }
    }

    post {
        success {
            echo "Python app deployed successfully 🎉"
        }
        failure {
            echo "Deployment failed ❌"
        }
    }
}

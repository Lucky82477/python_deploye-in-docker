pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Replace with your GitHub URL
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t my-python-app .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    # Stop and remove existing container if it exists
                    docker stop my-running-app || true
                    docker rm my-running-app || true
                    
                    # Run the new container
                    docker run -d -p 5000:5000 --name my-running-app my-python-app
                '''
            }
        }
    }
}

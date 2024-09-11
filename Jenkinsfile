pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Anurag11L/Jenkins_MLOps-Exp2', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt' // Use `bat` for Windows, assuming Python is installed
            }
        }
        stage('Build') {
            steps {
                echo 'Building the project...'
                bat 'python build.py' // Replace with your actual build command
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'python -m unittest discover tests' // Assuming you're using unittest for testing
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
                // Add your deployment steps here, e.g., pushing to an S3 bucket or another server
            }
        }
    }
    post {
        always {
            cleanWs()
            echo 'Pipeline completed.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}

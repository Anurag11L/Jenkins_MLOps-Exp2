pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the GitHub repository
                git branch: 'main', url: 'https://github.com/Anurag11L/Jenkins_MLOps-Exp2'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                // Train the ML model
                sh 'python train_model.py'
            }
        }

        stage('Test') {
            steps {
                // Run tests using pytest
                sh 'pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                // Add deployment steps (e.g., copying model.pkl, deploying to a server, etc.)
                echo 'Deploying the model...'
            }
        }
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}

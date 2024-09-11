pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    // Install dependencies
                    sh 'pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Train the model (generates model.pkl)
                    sh 'python train_model.py'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run the tests using pytest
                    sh 'pytest tests/'
                }
            }
        }
    }

    post {
        always {
            // Clean up after build
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

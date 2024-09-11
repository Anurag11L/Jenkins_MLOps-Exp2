pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from Git repository
                git 'https://github.com/Anurag11L/Jenkins_MLOps-Exp2'
            }
        }

        stage('Deploy') {
            steps {
                // For example, copy the index.html file to a deployment directory
                script {
                    def deployDir = 'E:\\Academics\\sem 7\\MLOps\\EXP 2'
                    bat "copy index.html ${deployDir}\\index.html"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
        always {
            cleanWs() // Clean workspace after the build
        }
    }
}

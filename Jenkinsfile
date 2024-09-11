pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the repository
                git branch: 'main', url: 'https://github.com/Anurag11L/Jenkins_MLOps-Exp2'
            }
        }

        stage('Build') {
            steps {
                echo 'Building...'
                
                // Example: Compile or build commands
                // For example, if you have a build script, you can run it here:
                // bat 'build-script.bat'  // Windows batch command
                // sh './build-script.sh'  // Unix shell command
                
                // Example: Just copy index.html to a build directory
                bat 'mkdir build'  // Create a build directory if it doesn't exist
                bat 'copy index.html build\\index.html'  // Copy index.html to the build directory
                
                // You can add more build steps here if needed
            }
        }


        stage('Deploy') {
            steps {
                script {
                    // Define source and destination directories
                    def sourceDir = 'build\\index.html'
                    def deployDir = 'E:\\Academics\\sem 7\\MLOps\\EXP 2'

                    // Ensure the deployment directory exists
                    bat "if not exist \"${deployDir}\" mkdir \"${deployDir}\""

                    // Copy the build output to the deployment directory
                    bat "copy \"${sourceDir}\" \"${deployDir}\\index.html\""
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}

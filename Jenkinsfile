pipeline {
    agent {
        label 'docker-build'   
    }

    stages {
        stage('Docker build') {
            steps {
                container('docker-build') {
                  sh 'printenv'
                }
            }
        }
    }
}
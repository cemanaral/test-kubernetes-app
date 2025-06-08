pipeline {
    agent {
        label 'docker-build'   
    }

    stages {
        stage('Docker build') {
            steps {
                container('docker-build') {
                  def image = docker.build "cemanaral425383/test-python-app:${env.GIT_COMMIT}"
                  image.push()
                }
            }
        }
    }
}
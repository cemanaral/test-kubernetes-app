pipeline {
    agent {
        label 'docker-build'   
    }

    stages {
        stage('Docker build') {
            steps {
                container('docker-build') {
                  sh '''
                    IMAGE_TAG="cemanaral425383/test-python-app:$GIT_COMMIT"
                    docker build -t $IMAGE_TAG .
                    docker push -t $IMAGE_TAG
                  '''
                }
            }
        }
    }
}
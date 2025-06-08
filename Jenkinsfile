pipeline {
    agent {
        label 'docker-build'   
    }

    options {
        disableConcurrentBuilds(abortPrevious: true)
        quietPeriod(30)
    }
    stages {
        stage('Docker build') {
            steps {
                container('docker-build') {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'docker-login') {
                            def image = docker.build "cemanaral425383/test-python-app:${env.GIT_COMMIT}"
                            image.push()
                        }
                    }
                }
            }
        }
        stage('Argocd deploy') {
            steps {
                script {
                    git branch: 'main', credentialsId: 'github-ssh-private-key', url: 'ssh://git@github.com/cemanaral/test-kubernetes-argocd.git'
                    sh '''
                        cat << EOF > "valuesOverrides/app-values.yaml"
image:
  tag: $GIT_COMMIT
EOF
                    '''

                    withCredentials([sshUserPrivateKey(credentialsId: 'github-ssh-private-key', keyFileVariable: 'PK')]) {
                        sh '''
                            git config --global user.email "jenkins@cemanaral.com"
                            git config --global user.name "Jenkins CI/CD"
                            git add valuesOverrides/app-values.yaml
                            git commit -m "Update image tag to $GIT_COMMIT"
                            git -c core.sshCommand="ssh -i $PK" push --set-upstream origin main
                        '''
                    }
                }
            }
        }
    }
}
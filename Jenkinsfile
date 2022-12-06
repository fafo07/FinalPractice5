def BDEV_statuscode
def FDEV_statuscode
def BQA_statuscode
def FQA_statuscode
pipeline{
    agent any
    stages{
        stage('Cloning Repository')
        {
            agent {label 'DEV'}
            steps
            {
                git branch: 'master' , url: 'https://github.com/fafo07/FinalPractice5.git'                
                sh "echo Cloned!" 
            }
        }
        stage('Build Images Docker')
        {
            agent {label 'DEV'}
            steps
            {
                sh "docker build --file=Frontend/frontend.dockerfile  -t web-frontend ."
                sh "docker build --file=Backend/backend.dockerfile  -t web-backend ."
                sh "docker save -o backend.tar web-backend"
                sh "docker save -o frontend.tar web-frontend"
                sh "docker compose up -d"
                stash name: "stash-backend", includes: "backend.tar"
                archiveArtifacts "backend.tar"
                stash name: "stash-frontend", includes: "frontend.tar"
                archiveArtifacts "frontend.tar"
                script
                {
                    BDEV_statuscode =sh(script: "curl -s -w %{http_code} http://192.168.0.26:8000/almacen/Productos/ -o /dev/null", returnStdout: true).trim() 
                    FDEV_statuscode =sh(script: "curl -s -w %{http_code} http://192.168.0.26:80 -o /dev/null", returnStdout: true).trim()
                    echo BDEV_statuscode
                }
            }
        }
        stage('Deploy in QA')
        {
            agent{ label 'QA'}
            when
            {
                 expression { BDEV_statuscode == '200' &&  FDEV_statuscode == '200' }
            }
            steps
            {
                unstash "stash-backend"
                unstash "stash-frontend"
                sh "docker load -i backend.tar"
                sh "docker load -i frontend.tar"
                sh "docker rm wbackend -f || true"
                sh "docker rm wfrontend -f || true"
                sh "docker run --name  wbackend web-backend"
                sh "docker run --name  wbackend front-backend"
                script
                {
                    BQA_statuscode =sh(script: "curl -s -w %{http_code} http://192.168.0.26:8000/almacen/Productos/ -o /dev/null", returnStdout: true).trim() 
                    FQA_statuscode =sh(script: "curl -s -w %{http_code} http://192.168.0.26:80 -o /dev/null", returnStdout: true).trim()
                    echo BQA_statuscode
                }
             }
        }
        stage('Deploy in PROD')
        {
            agent{ label 'PROD'}
            when
            {
                 expression { BQA_statuscode == '200' &&  FQA_statuscode == '200' }
            }
            steps
            {
                unstash "stash-backend"
                unstash "stash-frontend"
                sh "docker load -i backend.tar"
                sh "docker load -i frontend.tar"
                sh "docker rm wbackend -f || true"
                sh "docker rm wfrontend -f || true"
                sh "docker run --name  wbackend web-backend"
                sh "docker run --name  wbackend front-backend"
            }
        }
    }
}

pipeline{
    agent any
    stages{
        stage('Cloning Repository')
        {
            agent { label 'DEV'}
            steps
            {
                git branch: 'master' , url: 'https://github.com/fafo07/FinalPractice5.git'                
                sh "echo Cloned!" 
            }
        }
        stage('Build Images Docker')
        {
            steps
            {
                sh "docker build --file=Frontend/frontend.dockerfile  -t web-frontend ."
                sh "docker build --file=Backend/backend.dockerfile  -t web-backend ."
                sh "docker save -o backend.tar web-backend"
                sh "docker save -o frontend.tar web-frontend"
                stash name: "stash-backend", includes "backend.tar"
                archiveArtifacts "backend.tar"
                stash name: "stash-frontend", includes "frontend.tar"
                archiveArtifacts "frontend.tar"
            }
        }
        stage('Deploy in QA')
        {
            agent{ label 'QA'}
            steps
            {
                untash "stash-backend"
                untash "stash-frontend"
                sh "docker load -i backend.tar"
                sh "docker load -i frontend.tar"
                sh "docker rm wbackend -f || true"
                sh "docker rm wfrontend -f || true"
                sh "docker run --name  wbackend web-backend"
                sh "docker run --name  wbackend front-backend"
            }
        }
        stage('Deploy in PROD')
        {
            agent{ label 'PROD'}
            {
                steps
                {
                    untash "stash-backend"
                    untash "stash-frontend"
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
}


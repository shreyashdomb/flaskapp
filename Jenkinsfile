pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('636b92be-3bee-4bf0-a5bb-6596ca718256')
        DOCKER_IMAGE = 'dombshreyash/flask-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Run Unit Tests') {
            agent {
                docker {
                    image 'python:3.9-slim'
                }
            }
            steps {
                sh '''
                    pip install -r requirements.txt
                    python -m pytest test_app.py -v
                '''
            }
        }
        
        stage('Build Docker Image') {
            agent any
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }
        
        stage('Login to DockerHub') {
            agent any
            steps {
                sh 'echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin'
            }
        }
        
        stage('Push to DockerHub') {
            agent any
            steps {
                sh '''
                    docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                    docker push ${DOCKER_IMAGE}:latest
                '''
            }
        }
        
        stage('Deploy to Minikube') {
            agent any
            steps {
                sh '''
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    kubectl set image deployment/flask-app flask-app=${DOCKER_IMAGE}:${DOCKER_TAG}
                '''
            }
        }
    }
    
    post {
        always {
            sh 'docker logout'
            cleanWs()
        }
    }
} 
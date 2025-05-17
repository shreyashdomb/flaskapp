pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('636b92be-3bee-4bf0-a5bb-6596ca718256')
        DOCKER_IMAGE = 'dombshreyash/flask-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Setup') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m pytest test_app.py -v'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }
        
        stage('Login to DockerHub') {
            steps {
                sh 'echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin'
            }
        }
        
        stage('Push to DockerHub') {
            steps {
                sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                sh 'docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest'
                sh 'docker push ${DOCKER_IMAGE}:latest'
            }
        }
        
        stage('Deploy to Minikube') {
            steps {
                sh '''
                    apt-get install -y kubectl
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
pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
         stage('run') {
            steps {
                sh 'python manage.py runserver'
            }
        }
     
        }
    
}

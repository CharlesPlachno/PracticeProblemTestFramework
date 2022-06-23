pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('tests') {
            steps {
                sh 'pwd'
                sh 'pip install --no-cache-dir -r requirements.txt'
                sh 'pytest -v --junitxml=reports/result.xml'

                junit 'reports/result.xml'
            }
        }
    }
}
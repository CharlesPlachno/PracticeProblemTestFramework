pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('tests') {
            steps {
                sh 'ENV PYTHONPATH "${PYTHONPATH}:/var/jenkins_home/workspace/test-pipeline_master/"'
                sh 'pip install --no-cache-dir -r requirements.txt'
                sh 'pytest -v --junitxml=reports/result.xml'
            }
        }
    }
}
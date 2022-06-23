pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('tests') {
            steps {
                sh 'echo "current working directory"'
                sh 'pwd'
                sh 'export PYTHONPATH="$PWD/"'
                sh 'pip install --no-cache-dir -r requirements.txt'
                sh 'echo $PYTHONPATH'
                sh 'pytest -v --junitxml=reports/result.xml'
            }
        }
    }
}
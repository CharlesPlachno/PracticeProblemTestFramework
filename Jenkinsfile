pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('tests') {
            steps {
                sh 'echo "current working directory"'
                sh 'pwd'
                sh 'echo $PYTHONPATH'
                sh 'export PYTHONPATH="$PYTHONPATH:$PWD/"'
                sh 'echo $PYTHONPATH'
                sh 'pip install --no-cache-dir -r requirements.txt'
                sh 'pytest -v --junitxml=reports/result.xml'
            }
        }
    }
}
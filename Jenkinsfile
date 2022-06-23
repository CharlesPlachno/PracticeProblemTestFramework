pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('prepare_env') {
                steps{
                    sh 'pip install --no-cache-dir -r requirements.txt'
                }
            }
        stage('pylint') {
            steps{
                sh 'python3 -m pylint --output-format=parseable --fail-under=5.0 module --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" | tee pylint.log || echo "pylint exited with $?"'
                echo "linting Success, Generating Report"
                recordIssues enabledForFailure: true, aggregatingResults: true, tool: pyLint(pattern: 'pylint.log')
            }
        }
        stage('run_tests') {
            steps {
                sh 'pwd'
                sh 'pytest -v --junitxml=reports/result.xml'
            }
        }
        stage('publish_results') {
            steps {
                junit 'reports/result.xml'
            }
        }
    }
}
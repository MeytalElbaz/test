pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo "$A"
                echo "$B"
                python3 testHelpWithParameters.py $A $B
            }
        }
    }
}

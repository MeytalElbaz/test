pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo "$A"
                echo "$B"
                python testHelpWithParameters.py $A $B
            }
        }
    }
}

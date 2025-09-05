pipeline {
    agent { label 'Raspberrypi' }

    triggers {
        githubPush()
    }

    stages {
        stage('Teste de Conexao') {
            steps {
                sh 'hostname -I'
                sh 'docker images'
            }
        }
    }
}
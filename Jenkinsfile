pipeline {
    agent { label 'raspberry' }

    stages {
        stage('Teste de Conexao') {
            steps {
                sh 'hostname -I'
                sh 'docker images'
            }
        }
    }
}
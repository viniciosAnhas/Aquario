pipeline {
    agent { label 'raspberry' }

    triggers {
        githubPush()
    }

    stages {
        stage('Teste de Conexao') {
            when {
                branch 'main'
            }
            steps {
                sh 'hostname -I'
                sh 'pwd'
                sh 'docker images'
            }
        }
    }
}

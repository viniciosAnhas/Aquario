pipeline {
    agent { label 'Raspberrypi' }

    stages {
        stage('Teste de Conexao') {
            steps {
                sh 'hostname -I'
                sh 'docker images'
                sh 'mv * Aquario/* /home/pi/Aquario/'
            }
        }
    }
}
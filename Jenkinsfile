pipeline {
    agent { label 'Raspberrypi' }

    stages {
        stage('Teste de Conexao') {
            steps {
                sh 'hostname -I'
                sh 'docker images'
                sh 'shopt -s dotglob'
                sh 'mv -f /home/pi/JenkinsAgent/workspace/Aquario/* /home/pi/Aquario/'
            }
        }
    }
}
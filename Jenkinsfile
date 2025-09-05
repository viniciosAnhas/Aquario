pipeline {
    agent { label 'Raspberrypi' }

    stages {
        stage('Teste de Conexao') {
            steps {
                sh 'hostname -I'
                sh 'docker images'
            }
        }
    stage('Mover arquivos') {
        steps {
            sh '''
                # Vai até a pasta do workspace
                cd /home/pi/JenkinsAgent/workspace/Aquario
                # Move tudo para a pasta destino
                mv -f * /home/pi/Aquario/
            '''
        }
        }
    }
}
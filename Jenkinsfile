pipeline {
    agent { label 'Raspberrypi' }

    stages {
        stage('Verificando docker') {
            steps {
                sh '''
                    docker images
                    docker ps
                '''
            }
        }
        stage('Mover arquivos para a pasta Aquario') {
            steps {
                sh '''
                    cd /home/pi/JenkinsAgent/workspace/Aquario
                    mv -f * /home/pi/Aquario/
                '''
            }
        }
    }
}
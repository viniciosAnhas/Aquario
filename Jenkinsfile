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
                    rm -rf /home/pi/Aquario/*
                    cd /home/pi/JenkinsAgent/workspace/Aquario
                    mv -f * /home/pi/Aquario/
                '''
            }
        }
        stage('Limpando Memoria') {
            steps {
                sh '''
                    sysctl -w = 3 vm.drop_caches
                    sync && sudo sysctl vm.drop_caches=3
                '''
            }
        }
        stage('Temperatura Raspberry') {
            steps {
                sh '''
                    vcgencmd measure_temp
                '''
            }
        }
    }
}
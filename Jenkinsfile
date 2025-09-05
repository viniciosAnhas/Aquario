pipeline {
    agent { label 'Raspberrypi' }

    stages {
        stage('Limpando Memoria') {
            steps {
                sh '''
                    sudo sysctl -w = 3 vm.drop_caches 
                    sudo sync && sudo sysctl vm.drop_caches=3 
                    free -h
                '''
            }
        }
        stage('Temperatura do Raspberry') {
            steps {
                sh '''
                    vcgencmd measure_temp
                '''
            }
        }
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
    }
}
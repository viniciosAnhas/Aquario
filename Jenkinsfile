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
                    echo "Memória antes da limpeza:"
                    free -h
                    echo "Limpando cache de memória..."
                    sync
                    echo 3 | sudo tee /proc/sys/vm/drop_caches
                    echo "Memória depois da limpeza:"
                    free -h
                '''
            }
        }
    }
}
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
                    ls -l
                    cd ..
                    ls -l
                    pwd
                    rm -rf /home/pi/Aquario/
                    cp -r Aquario /home/pi/
                '''
            }
        }
        stage('Limpando Memoria') {
            steps {
                sh '''
                    free -h
                    sync
                    echo 3 | sudo tee /proc/sys/vm/drop_caches
                    free -h
                '''
            }
        }
    }
}
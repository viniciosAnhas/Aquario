pipeline {
    agent { label 'Raspberrypi' }

    stages {
        stage('Verificando Raspberry 🌡️⚡'){
            steps{
                sh '''
                    vcgencmd measure_temp && vcgencmd measure_volts
                '''
            }
        }
        stage('Realizando a primeira Limpeza 🧹'){
            steps{
                sh '''
                    free -h
                    sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches
                    echo 1 | sudo tee /proc/sys/vm/drop_caches
                    echo 2 | sudo tee /proc/sys/vm/drop_caches
                    sync
                    echo 3 | sudo tee /proc/sys/vm/drop_caches
                    sudo sysctl -w vm.drop_caches=3
                    free -h
                '''
            }
        }
        stage('Verificando Docker 🐋') {
            steps {
                sh '''
                    docker images
                    docker ps
                '''
            }
        }
        stage('Movendo a pasta Aquario 📂') {
            steps {
                sh '''
                    cd ..
                    rm -rf /home/pi/Aquario/
                    cp -r Aquario /home/pi/
                '''
            }
        }
        stage('Realizando a segunda Limpeza 🧹') {
            steps {
                sh '''
                    free -h
                    sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches
                    echo 1 | sudo tee /proc/sys/vm/drop_caches
                    echo 2 | sudo tee /proc/sys/vm/drop_caches
                    sync
                    echo 3 | sudo tee /proc/sys/vm/drop_caches
                    sudo sysctl -w vm.drop_caches=3
                    free -h
                '''
            }
        }
    }
    post {
        always {
            sh '''
                free -h
                sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches
                echo 1 | sudo tee /proc/sys/vm/drop_caches
                echo 2 | sudo tee /proc/sys/vm/drop_caches
                sync
                echo 3 | sudo tee /proc/sys/vm/drop_caches
                sudo sysctl -w vm.drop_caches=3
                free -h
            '''
        }
    }
}
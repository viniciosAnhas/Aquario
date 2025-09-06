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
                    pwd
                    ls -l
                    cd ..
                    ls -l
                    pwd
                    cp -r Aquario /home/pi/
                    // rm -rf /home/pi/Aquario/*
                    // shopt -s dotglob
                    // cd /home/pi/JenkinsAgent/workspace/Aquario
                    // mv -f * /home/pi/Aquario/
                '''
            }
        }
        // stage('Monitoramento do Sistema') {
        //     steps {
        //         sh '''
        //             vcgencmd measure_temp
        //             echo ""
        //             free -h
        //             echo ""
        //             df -h /
        //         '''
        //     }
        // }
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

    post {
        always {
            sh '''
                vcgencmd measure_temp
                free -h
            '''
        }
    }
}
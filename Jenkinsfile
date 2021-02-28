pipeline{
    agent any
    stages{

        stage("run test build") {
            when {
                branch "feature/*"
            }
            steps {
                sh '''
                    docker build -t service .
                    echo "Build was successful"
                    docker image rm service:latest
                '''
            }
        }

        stage("deploy") {
            when {
                anyOf {
                    branch "master";
                    branch "develop";
                }
            }
            steps {
                sh '''
                    export DEV_PORT=5001
                    export PROD_PORT=5002
                    if [ $GIT_BRANCH = "develop" ] ; then
                        export CONTAINER=dev
                    elif [ $GIT_BRANCH = "master" ] ; then
                        export CONTAINER=prod
                    else
                        export CONTAINER=release
                    fi

                    docker-compose up --build --force-recreate --no-deps -d ${CONTAINER}
                '''
            }
        }
    }
}
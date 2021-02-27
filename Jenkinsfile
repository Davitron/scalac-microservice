def get_branch_type(String branch_name) {
    def dev_pattern = ".*develop"
    def release_pattern = ".*release/.*"
    def feature_pattern = ".*feature/.*"
    def hotfix_pattern = ".*hotfix/.*"
    def master_pattern = ".*master"
    if (branch_name =~ dev_pattern) {
        return "dev"
    } else if (branch_name =~ release_pattern) {
        return "release"
    } else if (branch_name =~ master_pattern) {
        return "master"
    } else if (branch_name =~ feature_pattern) {
        return "feature"
    } else if (branch_name =~ hotfix_pattern) {
        return "hotfix"
    } else {
        return null;
    }
}

def get_image_name(Strinf branch_type_name) {
    if (branch_type_name == "develop") {
        return "microservice:dev"
    } else if (branch_type_name == "master") {
        return "microservice:prod"
    } else {
        return "microservice"
    }
}

def branch_type = get_branch_type "${env.BRANCH_NAME}"
def image_name  = get_image_name branch_type


pipeline{
    agent any
        environment {
            IMAGE_NAME = image_name
        }
    stages{

        stage("build image"){
            steps{
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage("deploy") {
            steps {
                sh '''
                    IMAGE_ID=\$(docker images $IMAGE_NAME --format "{{.ID}}")
                    if [ ! "\$(docker ps -aq -f ancestor=$IMAGE_NAME )" ] ; then
                        docker rm "$(docker ps -aq -f status=exited -f ancestor=\${IMAGE_NAME})"
                        docker run -d ${IMAGE_NAME}
                    fi
                '''
            }
        }
    }
}
def get_branch_type(String branch_name) {
    def dev_pattern = ".*develop"
    def release_pattern = ".*release/.*"
    def feature_pattern = ".*feature/.*"
    def hotfix_pattern = ".*hotfix/.*"
    def master_pattern = ".*master"
    if (branch_name =~ dev_pattern) {
        return "develop"
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

def get_container_name(String branch_type_name) {
    if (branch_type_name == "develop") {
        return "dev"
    } else if (branch_type_name == "master") {
        return "prod"
    } else {
        return "release"
    }
}

def branch_type = get_branch_type "${env.BRANCH_NAME}"
def image_name  = get_image_name branch_type


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
                    branch "staging";
                }
            }
            steps {
                def container_name = get_container_name

                sh '''
                    export DEV_PORT=5001
                    export PROD_PORT=5002
                    docker-compose up --build --force-recreate --no-deps -d ${container_name}
                '''
            }
        }
    }
}
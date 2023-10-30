pipeline{
    environment {
        credentialId = 'aliregistry'
        url = "https://registry-intl.ap-southeast-5.aliyuncs.com"
        // scannerHome = tool 'Sonarqube'
        servicename = 'ms-nifi-configuration'
    }
    //agent any
    agent { node { label 'agent1' } }
    stages {
        // stage('Sonar Scanner With PR') {
        //     when {
        //         branch 'PR-*';
        //     }
        //     steps {
        //         script {
        //             withSonarQubeEnv('Sonarqube') {
        //                 def prKey = "-Dsonar.pullrequest.key=${env.CHANGE_ID}"
        //                 def prBranch = "-Dsonar.pullrequest.branch=${env.CHANGE_BRANCH}"
        //                 def prBase = "-Dsonar.pullrequest.base=${env.CHANGE_TARGET}"
        //                 // Run the scan
        //                 sh "${scannerHome}/bin/sonar-scanner ${prKey} ${prBranch} ${prBase}"
        //             }
        //             timeout(time: 10, unit: 'MINUTES') {
        //                 waitForQualityGate abortPipeline: true
        //             }
        //         }
        //     }
        //     post {
        //         success {
        //             slackSend (color: '#008000', message: "PASSED: Sonarqube PR ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        //         }
        //         failure {
        //             slackSend (color: '#FF0000', message: "FAILED: Sonarqube PR ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        //         }
        //     }   
        // }
        stage('Publish Approval') {
            when { 
                tag "v*"
            }
            steps {
                script{
                //   input message: "Deploy these changes?", submitter "admin"
                def userName = input message: 'Deploy these changes?', submitter: "ericmoelyo,grandis", submitterParameter: "ericmoelyo,grandis"
                echo "Accepted by ${userName}"
                if (!(['ericmoelyo','grandis'].contains(userName))) {
                    error('This user is not approved to deploy to PROD.')
                }
                }
            }
        }
        // stage('Sonar Scanner Tag Release Prod') {
        //     when { 
        //         tag "release-*"
        //     }
        //     steps {
        //         script {
        //             withSonarQubeEnv('Sonarqube') {
        //                     sh "${scannerHome}/bin/sonar-scanner -Dsonar.branch.name=${env.BRANCH_NAME}"
        //             }
        //             timeout(time: 10, unit: 'MINUTES') {
        //                 waitForQualityGate abortPipeline: true
        //             }
        //         }
        //     }
        //     post {
        //         success {
        //             slackSend (color: '#008000', message: "PASSED: Sonarqube Prod ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        //         }
        //         failure {
        //             slackSend (color: '#FF0000', message: "FAILED: Sonarqube Prod ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        //         }
        //     }   
        // }
        stage('Build Image Tag Release Prod') {
            when { 
                tag "v*"
            }
            steps {
                slackSend (color: '#FFFF00', message: "STARTED: Build Image Prod ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                echo 'Build Image Prod'
                sh 'docker build -f Dockerfileprod . -t ${servicename}:${TAG_NAME}-${BUILD_NUMBER} --build-arg SSH_PRIVATE_KEY="$(cat /var/lib/jenkins/id_rsa)"'
                sh 'echo ini build image prod'
            }
            post {
                success {
                    slackSend (color: '#008000', message: "SUCCESS: Build Image Prod ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
                failure {
                    slackSend (color: '#FF0000', message: "FAILED: Build Image Prod ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
            }   
        }
        stage('Docker Login tag push Tag Release Prod') {
            when { 
                tag "v*"
            }
            steps {
                script {
                    echo 'Push docker image ke docker registry Ali Prod'
                    docker.withRegistry(url, credentialId) {
                        sh 'docker tag ${servicename}:${TAG_NAME}-${BUILD_NUMBER} registry-intl.ap-southeast-5.aliyuncs.com/majoo/${servicename}:${TAG_NAME}-${BUILD_NUMBER}'
                        sh 'docker push registry-intl.ap-southeast-5.aliyuncs.com/majoo/${servicename}:${TAG_NAME}-${BUILD_NUMBER}'
                        sh 'echo ini docker login tag push prod'
                    }
                }
            }
        }
        stage('Set Image Kubernetes Tag Release Prod') {
            when { 
                tag "v*"
            }
            steps {
                script {
                    sh 'kubectl --kubeconfig="../../kubeconfig-prod-enterprise-dataeng.yaml" set image deployment ${servicename} ${servicename}=registry-intl.ap-southeast-5.aliyuncs.com/majoo/${servicename}:${BRANCH_NAME}-${BUILD_NUMBER} -n=dataeng'
                    sh 'echo set image k8s prod'
                    sh 'kubectl --kubeconfig="../../kubeconfig-prod-enterprise-dataeng.yaml" scale deployment ${servicename} --replicas=1 -n dataeng'
                    //sh 'sleep 360'
                    //sh 'kubectl --kubeconfig="../../kubeconfig-prod-enterprise-dataeng.yaml" scale deployment ${servicename} --replicas=0 -n dataeng'
                }
            }
            post {
                success {
                    slackSend (color: '#008000', message: "SUCCESS: Deployment Prod ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
                failure {
                    slackSend (color: '#FF0000', message: "FAILED: Deployment Prod ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
            }
        }
        // stage('Sonar Scanner Branch Master') {
        //     when { 
        //         branch 'master';
        //     }
        //     steps {
        //         script {
        //             withSonarQubeEnv('Sonarqube') {
        //                     sh "${scannerHome}/bin/sonar-scanner -Dsonar.branch.name=${env.BRANCH_NAME}"
        //             }
        //             timeout(time: 10, unit: 'MINUTES') {
        //                 waitForQualityGate abortPipeline: true
        //             }
        //         }
        //     }
        //     post {
        //         success {
        //             slackSend (color: '#008000', message: "PASSED: Sonarqube Branch Master ${env.BRANCH_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        //         }
        //         failure {
        //             slackSend (color: '#FF0000', message: "FAILED: Sonarqube Branch Master ${env.BRANCH_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        //         }
        //     }   
        // }
        stage('Build Image Beta Branch Master') {
            when { 
                branch 'master';
            }
            steps {
                slackSend (color: '#FFFF00', message: "STARTED: Build Image Beta ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                echo 'Build Image beta'
                sh 'docker build -f Dockerfilestaging . -t ${servicename}:${BRANCH_NAME}-${BUILD_NUMBER} --build-arg SSH_PRIVATE_KEY="$(cat /var/lib/jenkins/id_rsa)"'
                sh 'echo ini build image beta'
            }
            post {
                success {
                    slackSend (color: '#008000', message: "SUCCESS: Build Image Beta ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
                failure {
                    slackSend (color: '#FF0000', message: "FAILED: Build Image Beta ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
            }   
        }
        stage('Docker Login tag push Beta Branch Master') {
            when { 
                branch 'master';
            }
            steps {
                script {
                    echo 'Push docker image ke docker registry Ali Beta'
                    docker.withRegistry(url, credentialId) {
                        sh 'docker tag ${servicename}:${BRANCH_NAME}-${BUILD_NUMBER} registry-intl.ap-southeast-5.aliyuncs.com/majoo/${servicename}:${BRANCH_NAME}-${BUILD_NUMBER}'
                        sh 'docker push registry-intl.ap-southeast-5.aliyuncs.com/majoo/${servicename}:${BRANCH_NAME}-${BUILD_NUMBER}'
                        sh 'echo ini docker login tag push Beta'
                    }
                }
            }
        }
        stage('Set Image Kubernetes Beta Branch Master') {
            when { 
                branch 'master';
            }
            steps {
                script {
                    sh 'kubectl --kubeconfig="../../kubeconfig-stg-enterprise-dataeng.yaml" set image deployment ${servicename} ${servicename}=registry-intl.ap-southeast-5.aliyuncs.com/majoo/${servicename}:${BRANCH_NAME}-${BUILD_NUMBER} -n=dataeng'
                    sh 'echo set image k8s Beta'
                    sh 'kubectl --kubeconfig="../../kubeconfig-stg-enterprise-dataeng.yaml" scale deployment ${servicename} --replicas=1 -n dataeng'
                    //sh 'sleep 360'
                    //sh 'kubectl --kubeconfig="../../kubeconfig-stg-enterprise-dataeng.yaml" scale deployment ${servicename} --replicas=0 -n dataeng'
                }
            }
            post {
                success {
                    slackSend (color: '#008000', message: "SUCCESS: Deployment Beta ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
                failure {
                    slackSend (color: '#FF0000', message: "FAILED: Deployment Beta ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
            }
        }
        // stage('Sonar Scanner Feature') {
        //     when { 
        //         branch 'feature/*';
        //     }
        //     steps {
        //         script {
        //             withSonarQubeEnv('Sonarqube') {
        //                     sh "${scannerHome}/bin/sonar-scanner -Dsonar.branch.name=${env.BRANCH_NAME}"
        //             }
        //             timeout(time: 10, unit: 'MINUTES') {
        //                 waitForQualityGate abortPipeline: true
        //             }
        //         }
        //     }
        //     post {
        //         success {
        //             slackSend (color: '#008000', message: "PASSED: Sonarqube Feature ${env.BRANCH_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        //         }
        //         failure {
        //             slackSend (color: '#FF0000', message: "FAILED: Sonarqube Feature ${env.BRANCH_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        //         }
        //     }   
        // }
        // stage('Sonar Scanner Hotfix') {
        //     when { 
        //         branch 'hotfix/*';
        //     }
        //     steps {
        //         script {
        //             withSonarQubeEnv('Sonarqube') {
        //                     sh "${scannerHome}/bin/sonar-scanner -Dsonar.branch.name=${env.BRANCH_NAME}"
        //             }
        //             timeout(time: 10, unit: 'MINUTES') {
        //                 waitForQualityGate abortPipeline: true
        //             }
        //         }
        //     }
        //     post {
        //         success {
        //             slackSend (color: '#008000', message: "PASSED: Sonarqube Hotfix ${env.BRANCH_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        //         }
        //         failure {
        //             slackSend (color: '#FF0000', message: "FAILED: Sonarqube Hotfix ${env.BRANCH_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        //         }
        //     }   
        // }
    }
    post {
        success {
            slackSend (color: '#008000', message: "SUCCESS: Pipeline ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        }
        failure {
            slackSend (color: '#FF0000', message: "FAILED: Pipeline ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        }
    }
}
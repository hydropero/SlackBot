pipeline {
  agent any
  stages {
    stage('TestStage') {
      steps {
        sh '''cd /home/ubuntu/Programming/Slack/SlackBot
git pull
start_slack'''
      }
    }

  }
}
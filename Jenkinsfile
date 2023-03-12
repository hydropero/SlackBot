pipeline {
  agent any
  stages {
    stage('TestStage') {
      steps {
        sh '''git -C /home/ubuntu/Programming/Slack/SlackBot pull
start_slack'''
      }
    }

  }
}
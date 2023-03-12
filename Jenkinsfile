pipeline {
  agent any
  stages {
    stage('TestStage') {
      steps {
        sh '''sudo git -C /home/ubuntu/Programming/Slack/SlackBot pull
start_slack'''
      }
    }

  }
}
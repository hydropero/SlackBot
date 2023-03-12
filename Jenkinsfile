pipeline {
  agent any
  stages {
    stage('TestStage') {
      steps {
        sh '''git config --global --add safe.directory /home/ubuntu/Programming/Slack/SlackBot
git -C /home/ubuntu/Programming/Slack/SlackBot pull
slack'''
      }
    }

  }
}
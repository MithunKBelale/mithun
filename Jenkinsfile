pipeline{
  agent any

  stages{

    stage('clone'){
      steps {
        git url: 'https://github.com/MithunKBelale/jenkins.git',
          branch: 'main'

      }
    }
    stage('Run Script'){
      steps{
        sh 'chmod +x script.sh'
        sh './script.sh'
      }
    }
    stage('Build Docker Image') {
    steps {
        sh 'docker build -t my-python-app:${env.BUILD_ID} .'
    }
}
  }
}

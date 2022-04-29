pipeline {
    agent any
    stages{
        stage ('Build'){
            steps{
                echo 'Building...'
                bat 'python labexam.py'
            }
        }
        stage ('Test'){
            steps{
                echo 'Using maven'
            }
        }
    }
}

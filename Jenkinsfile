pipeline { 
  agent any 
  stages { 
    stage('Testing') { 
      steps { 
        echo 'running Tests' 
        bat 'python myfile.py'
      } 
    } 
    stage('Build') { 
      steps { 
        echo 'Building jar files...'
      } 
    } 
  } 
}
node(){
    
    properties(
    [
        parameters(
            [string(defaultValue: '', name: 'Jenkins_URL', description: 'Enter Remote Jenkins Instance URL')]
            )
    ]
    )    

    stage('checkout'){
    	checkout scm
    }

    stage('Build Docker Image'){
    	sh "/usr/local/bin/docker build -t myscript:1.0 python-parse/dockerfile/"
    }
	
    // Python scripts are stored under python-parse folder of repository. So used dir step to change directory    
    
    stage('Python Script to match plugins information'){
 	   withCredentials([usernamePassword(credentialsId: 'github', passwordVariable: 'password', usernameVariable: 'username')]) {
    		sh "/usr/local/bin/docker run -i -v /var/lib/jenkins/workspace/plugin-docker/:/root myscript:1.0 $Jenkins_URL $username $password"
    	   }
    }
    
    stage('Send Report'){
	emailext attachmentsPattern: '**/report.csv', body: 'Please find the below report status for plugins configuration', 
        subject: 'Plugin Configuration Match Report', to: 'chakresh.kolluru@infostretch.com'
    }
    
}

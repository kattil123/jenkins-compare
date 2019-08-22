node(){
    
    properties([
        parameters([
            string(defaultValue: '', name: 'GoldCopy_Jenkins_URL', description: 'Enter Gold Copy Jenkins Instance URL'),
            string(defaultValue: '', name: 'GoldCopy_Username', description: 'Enter Gold Copy Jenkins Instance Username'),
            string(defaultValue: '', name: 'Remote_Jenkins_URL', description: 'Enter Remote Jenkins Instance URL'),
            string(defaultValue: '', name: 'Remote_Username', description: 'Enter Remote Jenkins Instance Username'),
            string(defaultValue: '', name: 'Remote_Host', description: 'Enter Remote Machine Host/Ipaddress'),
            string(defaultValue:'', name:'Remote_User',description: 'Enter Remote Machine User'),
            ])
    ])    

    stage('checkout'){
    	checkout scm
    }

    stage('Install Python Modules'){
    	def check = sh returnStatus: true, script: 'python -c "import pexpect"'
        if (check == 1){
            install()
            echo "Installed Successfully"    
        }
        else
        echo "Already Installed"
    }	
    // Store GoldCopy Master Password in GoldCopy_Password secret variable 
    // Store Remote Jenkins Master Password in Remote_Password secret variable
    // Store Remote Machine Password in Remote_vm_Password secret variable
    stage('Python Script to match plugins information'){ 
        withCredentials([string(credentialsId: 'GoldCopy_Password', variable: 'GoldCopy_Password'), string(credentialsId: 'Remote_Password', variable: 'Remote_Password'), string(credentialsId: 'Remote_vm_Password', variable: 'Remote_vm_Password')]) {
        sh "python plugin1.py $GoldCopy_Jenkins_URL $GoldCopy_Username $GoldCopy_Password $Remote_Jenkins_URL $Remote_Username $Remote_Password $Remote_Host $Remote_User $Remote_vm_Password"
        }  
    }
    
    stage('Send Report'){
	emailext attachmentsPattern: '**/report.csv', body: 'Please find the below report status for plugins configuration', 
        subject: 'Plugin Configuration Match Report', to: 'ajith.kattil@infostretch.com'
    }
    
}

def install(){
    sh "pip install pexpect"
    sh "pip install python-jenkins"
    sh "pip install jenkinsapi"
}

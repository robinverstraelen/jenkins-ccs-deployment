from settings import *
from cloudcenter import cloudcenter
from node import node

ccs = cloudcenter(url,account_id,api_token)

if(ccs.checkIfDeploymentIsRunning(deploymentname)):
    ips = ccs.getIPsFromDeployment(deploymentname, code_tier)
    for ip in ips:
        vm = node(ip)
        for command in commands:
            vm.executeCommand(command)
else:
    # creating deployment on GCP
    ccs.createDeployment(deploymentname, "gcp_deploy.json")
import requests
from requests.auth import HTTPBasicAuth
import json
import array
import os

class cloudcenter:
    def __init__(self, base_url, account_id, api_token):
        self.base_url = base_url
        self.account_id = account_id
        self.api_token = api_token
        self.deployments = ""

    def __getDeployments__(self):
        if not self.deployments == "":
            return self.deployments
        else:
            self.deployments = requests.get(self.base_url + '/cloudcenter-ccm-backend/api/v1/jobs/', auth=(self.account_id, self.api_token), headers={"content-type":"application/json"})
            return self.deployments

    def checkIfDeploymentIsRunning(self, deploymentName):
        for job in self.__getDeployments__().json()['jobs']:
            if(job['name'] == deploymentName):
                if job['status'] == "Running":
                    # job exists and is running
                    return True
                # job exists but isn't running
                return False
        # job doesn't exist
        return False

    def __getDeploymentURL__(self, deploymentName):
        for job in self.__getDeployments__().json()['jobs']:
            if(job['name'] == deploymentName):
                return job['resource']

    def getIPsFromDeployment(self, deploymentName, codeTier):
        ips = []
        r = requests.get(self.__getDeploymentURL__(deploymentName), auth=(self.account_id, self.api_token), headers={"content-type":"application/json"})
        for tier in r.json()['jobs']:
            if tier['name'] == codeTier:
                for vm in tier['virtualMachines']:
                    ips.append(vm['publicIp'])
        return ips

    def __replaceStringInFile__(self, filelocation, outputlocation, find, replace):
        fin = open(filelocation, "rt")
        fout = open(outputlocation, "wt")

        for line in fin:
            fout.write(line.replace(find, replace))
            
        fin.close()
        fout.close()

    def createDeployment(self, deploymentName, template_location):
        self.__replaceStringInFile__("gcp_deploy.json", "thisdeployment.json", "@jobname", deploymentName)
        reqdata = json.load(open('thisdeployment.json'))
        reqdata = open('thisdeployment.json').read()
        resp = requests.post(self.base_url + '/cloudcenter-ccm-backend/api/v2/jobs', auth=(self.account_id, self.api_token), headers={"content-type":"application/json"}, data=reqdata)
        print(resp.text)
        os.remove('thisdeployment.json')
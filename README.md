# jenkins-ccs-deployment
 
This repository contains the source of a provisioning script that can be called from a Jenkins pipeline.

## Concepts

This script will automate application deployment in cloudcenter. If the deployment doesn't already exists, the script will create a new one. Otherwise, the script will talk to the cloudcenter API, ssh into the code tier node(s) (specified in settings.py) using ssh keys and execute the update commands (array in settings.py).

## Customisation

You can specify all your settings in settings.py. Please note that this script is only meant to update one tier.
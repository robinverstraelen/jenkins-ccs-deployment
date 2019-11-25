# Name of your deployment
deploymentname = "jenkins-testing"

# Name of your app profile
appprofilename = "threetier"

# The path to your ssh keys to connect to your instances
public_ssh_key_location = "public.key"
private_ssh_key_location = "private.key"

# CloudCenter data
url = "https://eu.cloudcenter.cisco.com"
account_id = "[your account id]"
api_token = "[your token]"

# The name of the tier where code is stored
code_tier = "web"

# An array of commands to update the deployment on the code tier
commands = ["mkdir -p /var/www/html/php-sample/", "git clone https://github.com/robinverstraelen/ccc-provision.git /var/www/html/php-sample/", "mv /var/www/html/php-sample/src/index.php /var/www/html/index.php", "rm -r /var/www/html/php-sample/"]
# counter-service
This code contains a simple web server that counts the number of POST and GET requests it serves and returns the counter on every GET request it receives. 

* I've added a requirements.txt file (flask is the only one)
* The pipeline uses 2 AWS secrets I've set up for the repo, logins into AWS and ECR.
* Then I'm building the image and replacing latest, but also tagging it with branch-commit-id and date.
* After pushing the image we're getting the kubeconfig file for our cluster and installing with helm.

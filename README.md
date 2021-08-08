# Dynamic PR environments demo
## Note : Aws credentials will be needed to be added to Github Secrets
Steps to replicate demo :
1) Clone the repository locally
2) /website folder has the website that gets deployed to aws.
3) Add malicious code to test.py in /website
4) Commit and push the changes 
5) Create a pull request with label "PR-Deploy"
6) This will trigger the workflows which will scan your code using aws codeguru and deploy the website using AWS CDK 
7) After the workflows end , you will get a Deployment URL and codeguru scan results in the PR section (Scan results in "Changes" tab)
8) Merge or CLose the Pull Request , this will trigger the clean-up workflow which will clear all the aws resources and take down the website

*******************************************************************************************

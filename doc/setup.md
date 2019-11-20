---
This part hasn't set yet.
### To setup the env docker 1st time
sudo docker pull selenium/hub
sudo docker pull selenium/node-chrome
sudo docker pull selenium/node-firefox

### run
sudo docker-compose up -d --scale chrome=2 --scale firefox=2
---

### Add authentication data
`src/json/auth.json`
{
  "email": <Add email here>,
  "password": <Add password here>,
  "wrong_password": <Add anything here>,
  "github_id": <Add github id>,
  "github_password": <>,
  "bitbucket_id": <Add bitbucket id>,
  "bitbucket_password": <>,
  "gitlab_id": <Add gitlab id>,
  "gitlab_password": <>,
}

`src/json/integrations.json`
{
  "tfs_base_uri": "",
  "tfs_username":"",
  "tfs_token":"",
  "bbserver_base_uri": "",
  "bbserver_username":"",
  "bbserver_token":"",
  "glserver_base_uri": "",
  "glserver_token":""
}
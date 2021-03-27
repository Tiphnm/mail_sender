# Mail_sender

Creating a classic front-end interface where the user can enter its email and receice the new items from a scrapped website. The all is deployed on Azure web app service. You can try it by yourself by clicking [here](https://tiphn-email-sender.azurewebsites.net/home).

### 🧰  Languages and tools: 
- Python
- Postgres SQL
- Azure Web App

### 📁 Files and scripts architecture 

<p align="left">
  <img src="https://github.com/Tiphnm/mail_sender/blob/master/Architecture.png" width="350" title="hover text">
</p>

### Command lines 

First step was to create the VM on **Azure** and install **Portgresql** to store our database and tables on it.
Access your VM on your terminal and set up your psql password with the following : 
- `ssh -i <File/Path/To/Your/privatekey.pem> <yourazureusername>@<ipadresseofVM>`
- `sudo apt update`
- `sudo apt install postgresql`
- `sudo -i -u postgres`
- `postgres`
- `\ passord postgres`
- `sudo service postgresql restart`











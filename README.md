# Mail_sender

Creating a classic front-end interface where the user can enter its email and receice the new items from a scrapped website. The all is deployed on Azure web app service. You can try it by yourself by clicking [here](https://tiphn-email-sender.azurewebsites.net/home).

### 🧰  Languages and tools: 
- Python
- Postgres SQL
- Azure Web App

### 📁 Files and scripts architecture 

My work is divided in two files, one for the scrap and the other one within the first to build the interface and connect the psql to my webpage. What changed regarding my previous work is the **HTML/CSS**, the **postgres.py** -addding a table to store the email of my users- and also my **mail.py** fully dedicated to sent email to my users and specific data from my database. 

<p align="center">
  <img src="https://github.com/Tiphnm/mail_sender/blob/master/Architecture.png" width="350" title="hover text">
</p>

### Command lines 

🚨 Important to open the default port of psql on Azure: port **5432**. 

##### On VM 
First step was to create the VM on **Azure** and install **Portgresql** to store our database and tables on it.
Access your VM on your terminal and set up your psql password with the following : 
- `ssh -i <File/Path/To/Your/privatekey.pem> <yourazureusername>@<ipadresseofVM>`
- `sudo apt update`
- `sudo apt install postgresql`
- `sudo -i -u postgres`
- `postgres`
- `\ password postgres`
- `sudo service postgresql restart`

##### Locally 

- `az login`
- `git clone <repolink>`
- `python3 -m venv .venv source .venv/bin/activate `
- `pip install -r requirements.txt`
- `flask run`
- ` az webapp up --sku B1 --name <nameofurapp>` 
- `az webapp up`














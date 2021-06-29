# Remote Development and Debugging 

This scenario occurs when we want to develop, run and debug our python project in a remote server. 
The development, however, would be done in the local system and then the changes would be pushed into the remote server to run in that environment. 
Now, this can be easily done by just copying the entire folder structure to the remote. However, we will be leveraging **pycharm professional** to do it. 

## Author : Sudeshna Bora 

---

**Remote System:** Linux<br>
**Local System:** Windows/Linux<br>
**Required Setup:** pycharm professional<br>
**Assumption:** Virtual environment etc have been set up. <br>

---

## Step 1 : Configure remote deployment 

1. Go to **tools->deployment->configuration**.
2. If no configuration is present, click on **+** and add new **SFTP Configuration**.
3. Give a suitable name 

### Step 1.1 : Configure Connection

1. In **SSH CONFIGURATION** add the configuration details like *host ip*, *username*, *password*. 
2. Then check connection.
3. For **root path** , I autodetect the *home directory*.

### Step 1.2 : Configure mapping 

1. In **Mappings** , fill up **deployment path** with the path to the remote project directory [For this make sure you have created atleast an empty folder with that project name].

4. Then press ok.

---

## Step 2 : Sync local folder with remote 

1.  Go to **tools->deployment->Automatic Upload**. This will upload whenever you save the  particular file. 

**Note:** It is advised to have used ```scp -r``` to push the project to the remote first (as all files will go at the same time).

---

## Step 3 : Local development and remote debugging [linux,mac specific only]

Whenever we make changes and save, the changes would have been pushed into the remote folder. Now, we would like to do remote debugging. 



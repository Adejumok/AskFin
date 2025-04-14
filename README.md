# AskFin

A smart conversational assistant built with Rasa and integrated with Claude (Anthropic) to provide real-time, user-friendly answers to financial questions. The chatbot aims to improve financial literacy and promote inclusion by offering guidance on budgeting, credit scores, saving, banking, and more.

## Features  
🤖 Natural language chat interface for financial education

📊 Supports queries about budgeting, saving, credit, and banking

🌍 Promotes financial inclusion for users with varying levels of knowledge

💡 Handles both guided flows and free-form user questions

🔁 Easy to integrate into websites, mobile apps, or WhatsApp

🧠 Custom Rasa action that routes financial questions to Claude  

## Technologies Used  
Rasa - NLP engine & conversation orchestration

Claude (LLM) - Real-time financial answer generation

Python -	Custom actions and backend integration

YAML	- Rasa configuration files (nlu, domain)

Ngrok (optional) - Tunneling for local testing

Docker (optional) -	Containerization for deployment

## Installation and Setup  

### 1. Clone the Repository  
```bash  
git clone <repository-url>  
cd <repository-folder>  
```
### If cloning with SSH
Generate a new SSH public key following these steps:
- Open Terminal
- Paste the text below, replacing the email used in the example with your GitHub email address
```bash
$ ssh-keygen -t ed25519 -C "your_email@example.com" 
```
When you're prompted to "Enter a file in which to save the key", you can press Enter to accept the default file location. Please note that if you created SSH keys previously, ssh-keygen may ask you to rewrite another key, in which case we recommend creating a custom-named SSH key. To do so, type the default file location and replace id_ALGORITHM with your custom key name.
```bash
> Enter a file in which to save the key (/Users/YOU/.ssh/id_ALGORITHM): [Press enter]
```
At the prompt, type a secure passphrase.
```bash
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```
### Adding your SSH key to the ssh-agent:
Start the ssh-agent in the background
```bash
$ eval "$(ssh-agent -s)"
> Agent pid 59566
```
Depending on your environment, you may need to use a different command. For example, you may need to use root access by running ```sudo -s -H``` before starting the ssh-agent, or you may need to use exec ssh-agent bash or exec ```ssh-agent zsh```  to run the ssh-agent.
If you're using macOS Sierra 10.12.2 or later, you will need to modify your ```~/.ssh/config``` file to automatically load keys into the ssh-agent and store passphrases in your keychain.
- First, check to see if your ``` ~/.ssh/config ``` file exists in the default location.
- If the file doesn't exist, create the file.
```bash
$ touch ~/.ssh/config
```
- Open your ```~/.ssh/config``` file, then modify the file to contain the following lines. If your SSH key file has a different name or path than the example code, modify the filename or path to match your current setup.
```bash
  Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```
- Add your SSH private key to the ssh-agent and store your passphrase in the keychain. If you created your key with a different name, or if you are adding an existing key that has a different name, replace id_ed25519 in the command with the name of your private key file.
```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```
- Add the SSH public key to your account on GitHub. For more information, see [Adding a new SSH key to your GitHub account.](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

### 2. Create and Activate a Virtual Environment 
For Windows:
```bash  
python -m venv rasa_env
rasa_env\Scripts\activate
```
For macOS/Linux:
```bash  
python3 -m venv rasa_env
source rasa_env/bin/activate
```
### 3. Install Dependencies  
Once activated, you should see the virtual environment name in your terminal prompt.
Install Required Dependencies:
```bash  
pip install -r requirements.txt
```

### 4. Configure Environment Variables  
Set up sensitive credentials like claude keys, and others in a `.env` file for secure handling:  
```  
CLAUDE_API_KEY=<your_claude_api_key>  
```  

### 5. Run Rasa Locally
Build the Rasa Model:
```bash
rasa train
```

Start the Rasa server:  
```bash  
rasa run --endpoints endpoints.local.yml --enable-api
```  

Run the action server: 
In a seperate terminal run the action command
```bash  
rasa run actions  
```  

### 6. Set Up ngrok for Local Testing  
To expose your Rasa bot to the internet and connect it to Twilio:  
1. Install ngrok:  
   ```bash  
   pip install ngrok  
   ```  
2. Authenticate ngrok using your authtoken (get it from [ngrok dashboard](https://dashboard.ngrok.com/get-started/setup)):  
   ```bash  
   ngrok config add-authtoken <YOUR_NGROK_AUTHTOKEN>  
   ```  
3. Start an ngrok HTTP tunnel for port 5005:  
   ```bash  
   ngrok http 5005  
   ```  
4. Copy the HTTPS forwarding URL (e.g., `https://<your-ngrok-url>.ngrok.io`).  
 

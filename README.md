# What Is It?
GPG Keys is a command line tool created using Python3. It was originally intended to save Github Personal access token to make them easily accessible from your local machine. 

I am currently working on adding more functionality to it, such as: 
- [x] Deleting a key that was accidently entered.  
- [ ] Automatically purging expired keys. 

# Usage 
```bash 
./gpgkeys.py init # Initializes the database in the same folder that it is stored. 

./gpgkeys.py view # Displays the entire database entries

./gpgkeys.py view [<repository_name>] # Displays the database entry for the repository name that was specificied

./gpgkeys.py <gpg_key> <repository_name> # Stores the gpgkeys specified into the database. 

./gpgkeys.py delete <repository_name> # Deletes the access token stored for the specifed repository name.
```

# What's Included?
A number of files is included to facilitate customizability and flexibility. 

1. In the master branch, you have the `gpgkeys.py`; you can easily run/ customize the script using `./gpgkeys.py`. 
1. In the `dist/` folder, there is the full build you could run as is. If you do choose to use the `gppkeys` from the `dist/` folder, I recommend storing the script in an esily accessible folder and add it to your $PATH.

# Installation

```Bash 
# Clone the repository
git clone https://github.com/EzlosSWM/gpgkeys.git

# Moving into the gpgkeys directory: 
cd gpgkeys/

# Installing Requirements: 
pip install -r requirements.txt



# Alternatively (After cloning the repository) 
# Create a folder to store scripts
mkdir ~/.scripts/

# Copy the gpgkeys file into the directory. 
cp gpgkeys/dist/gpgkeys ~/.scripts/

# Appending the ~/.scripts directory to your PATH
export PATH=$PATH:$HOME/.scripts/
```

*Note: To make the PATH permanent, just add the export statement to your .bashrc or .zshrc*
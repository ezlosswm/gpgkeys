# What Is It?
GPG Keys is a command line tool created using Python3. It was originally intended to save Github Personal access token to make them easily accessible from your local machine. 

I am currently working on adding more functionality to it, such as: 
- Deleting a key that was accidently entered.  
- Automatically purging expired keys. 

# Usage 
```bash 
./gpgkeys.py init # Initializes the database in the same folder that it is stored. 

./gpgkeys.py view # Displays the entire database entries

./gpgkeys.py view [<repository_name>] # Displays the database entry for the repository name that was specificied

./gpgkeys.py <gpg_key> <repository_name> # Stores the gpgkeys specified into the database. 
```

# What's Included?
A number of files is included to facilitate customizability and flexibility. 

1. In the master branch, you have the `gpgkeys.py`; you can easily run/ customize the script using `./gpgkeys.py`. 
1. In the `dist/` folder, there is the full build you could run as is. If you do choose to use the `gppkeys` from the `dist/` folder, I recommend storing the script in an esily accessible folder and add it to your $PATH.

# Installation

```Bash 
# Step One: 
# Clone the repository
git clone https://github.com/EzlosSWM/gpgkeys.git

# Step One (B) (Optional): 
# Create a folder to store scripts
mkdir ~/.scripts/

# Step Three: 
# Move into the "dist/" folder 
cd gpgkeys/dist/

# Step Four: 
# Copy the gpgkeys file into the directory. 
cp ./gpgkeys ~/.scripts/

# Step Five (Optional): 
# If you want to use the gpgkeys.py: 
pip install -r requirements.txt
```

#!/usr/bin/env python3
# Takes the gpgkey as an argument and stores it locally into a database.

# Created by: Ezlos SWM 
# Contact Info: 
# email: ezlosswm@gmail.com 
# twitter: @EzlosSWM 
# github: https://github.com/EzlosSWM/

from docopt import docopt
from gpgfunc import *
from tabulate import tabulate

usage = '''

GitHub GPG Keys Storage 

Usage: 
    gpgkeys.py init 
    gpgkeys.py view [<view_repo_name>]
    gpgkeys.py <gpg_key> <repo_name>
'''

args = docopt(usage)

# Command Line Interface
if args['init']:
    init()

if args['view']:
    repo_name = args['<repo_name>']
    results = view(repo_name)
    print(tabulate(results))

if args['<gpg_key>']:
    try: 
        # repo_name = str(args['<repo_name>'])
        log(args['<gpg_key>'], args['<repo_name>'])
    except:
        print(usage)

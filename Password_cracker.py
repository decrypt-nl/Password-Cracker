 # -*-coding:Latin-1 -*
#Password cracker by decrypt.sh



import hashlib
import sys


print '''

 ___                      _    ___             _             _         
| _ \__ _ _______ __ ____| |  / __|_ _ __ _ __| |_____ _ _  | |__ _  _ 
|  _/ _` (_-<_-< V  V / _` | | (__| '_/ _` / _| / / -_) '_| | '_ \ || |
|_| \__,_/__/__/\_/\_/\__,_|  \___|_| \__,_\__|_\_\___|_|   |_.__/\_, |
                                                                  |__/ 
    _                  _        _    
 __| |___ __ _  _ _ __| |_   __| |_  
/ _` / -_) _| || | '_ \  _|_(_-< ' \ 
\__,_\___\__|\_, | .__/\__(_)__/_||_|
             |__/|_|                     

'''

while True:
        try :
            wordlist_user=raw_input('Entre ta wordlist : ')
            wordlist=open(wordlist_user,'r')
            hash=raw_input('Entre ton hash sha1 : ')

            break


        except:
                print('Aucun fichier portant ce nom !!! \n')
                sys.exit()

for word in wordlist.readlines():
    word=word.strip('\n')
    wordlist_hash=hashlib.sha1(word).hexdigest()

    if (hash==wordlist_hash):
             print('Password trouvé ===> '+word)
             break

    else:

             print('Password pas encore trouvé')



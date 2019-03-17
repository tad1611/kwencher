import requests
import json
from pprint import pprint
import time
import sys
import MySQLdb



# sudo apt-get install python-setuptools 
# sudo apt-get install python-virtualenv 
# sudo easy_install pip
# sudo pip install virtualenvwrapper 

class LocationLoad:

        
    @staticmethod
    def _loadlocationdim():
        ##connect to database##########################################
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="Shared1234",
                             use_unicode=True, 
                             charset="utf8"  # your password
                             )                    # name of the data base
        cur = db.cursor()
        a = cur.execute("use KWENCHER_DB");
        print("connected to database!")
        ###############################################################
        b = cur.execute("insert ignore into drinkinfo_location_fct values ('1'))
        c = cur.execute("commit;")
 
#             
#             
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
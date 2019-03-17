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
        apiurl = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
        apiloc = 'location=43.656829,-70.260017'
        apifilters ='&radius=5000&type=bar'
        apikey = '&key=AIzaSyBMi6hqDgmOL2ovMIIT4df16m6avTxdG6k'
       
        posturl = apiurl + apiloc + apifilters + apikey
        print(posturl)
        array = json.dumps(requests.get(posturl).json())
        a = json.loads(array)
        count = 0
        nextpagetoken = ''
        status = a['status']
        print(status)
        
#         while status == 'OK':
#             for place_id in a['results']:
#                 place_id = a['results'][count]['place_id']
#                 name = a['results'][count]['name']
#                 count = count + 1
#                 print(name)
#             try: 
#                 nextpagetoken = '&pagetoken=' + a['next_page_token']
#             except KeyError: nameDisplay = None
#             posturl = apiurl + nextpagetoken + apikey
#             time.sleep(2)
#             print('-------------------------------------------------')
#             print(posturl)
#             array = json.dumps(requests.get(posturl).json())
#             a = json.loads(array)
#             count = 0
# 
#             
#             
        while nextpagetoken != 'EXIT':
            for place_id in a['results']:
                place_id = a['results'][count]['place_id']
                name = a['results'][count]['name']

                
                b = cur.execute("insert ignore into drinkinfo_location_dim values (%s,%s,%s)",                                       
                                (count,
                                 place_id,
                                 name
                                 )                
                )
                count = count + 1
                print(name)
            try: 
                nextpagetoken = '&pagetoken=' + a['next_page_token']
            except KeyError: nextpagetoken = 'EXIT'
            posturl = apiurl + nextpagetoken + apikey
            time.sleep(2)
            print('-------------------------------------------------')
            array = json.dumps(requests.get(posturl).json())
            a = json.loads(array)
            c = cur.execute("commit;")
            count = 0
 
#             
#             
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
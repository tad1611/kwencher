import requests
import json
from pprint import pprint
from time import sleep
import sys
import MySQLdb



# sudo apt-get install python-setuptools 
# sudo apt-get install python-virtualenv 
# sudo easy_install pip
# sudo pip install virtualenvwrapper 

class BreweryLoad:

       
    @staticmethod
    def _loadBeerDim():
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
        apiurl = 'http://api.brewerydb.com'
        apiver = '/v2'
        apiendpoint = '/beers'
        apikey = '/?key=8c4d0e5e6e7b4807f9adead425143dbb'
        page = 1
        posturl = apiurl + apiver + apiendpoint + apikey +  '&p=' + str(page)
        count = 0
        total = 0
        abv = ''
        loop = 0
        commitcount = 200     
        print(posturl)
      
        array = json.dumps(requests.get(posturl).json())
        a = json.loads(array)     
        print(a) 
        while a['currentPage'] <= a['numberOfPages']:
            posturl = apiurl + apiver + apiendpoint + apikey +  '&p=' + str(loop)
            array = json.dumps(requests.get(posturl).json())
            a = json.loads(array) 
            #LOAD BEER DATA INTO MYSQL LOOP
            for beer_name in a['data']:
         
                beer_key = a['data'][count]['id']
                beer_name = a['data'][count]['name']
                try: 
                    nameDisplay = a['data'][count]['nameDisplay']
                except KeyError: nameDisplay = None
                try: 
                    catergoryId = a['data'][count]['style']['categoryId']
                except KeyError: catergoryId = None    
                try: 
                    description = a['data'][count]['description']
                except KeyError: description = None
                try: 
                    abv = a['data'][count]['abv']
                except KeyError: abv = None
                try: 
                    ibu = a['data'][count]['ibu']
                except KeyError: ibu = None
                try: 
                    glasswareId = a['data'][count]['glasswareId']
                except KeyError: glasswareId = None
                try: 
                    srmId = a['data'][count]['srmId']
                except KeyError: srmId = None
                try: 
                    availableId = a['data'][count]['availableId']
                except KeyError: availableId = None
                try: 
                    styleId = a['data'][count]['styleId']
                except KeyError: styleId = None
                try: 
                    isOrganic = a['data'][count]['isOrganic']
                except KeyError: isOrganic = None
                try: 
                    status = a['data'][count]['status']
                except KeyError: status = None
                try: 
                    statusDisplay = a['data'][count]['statusDisplay']
                except KeyError: statusDisplay = None
                try: 
                    servingTemperature = a['data'][count]['servingTemperature']
                except KeyError: servingTemperature = None
                try: 
                    servingTemperatureDisplay = a['data'][count]['servingTemperatureDisplay']
                except KeyError: servingTemperatureDisplay = None
                try: 
                    label_small = a['data'][count]['labels']['icon']
                except KeyError: label_small = None                
                try: 
                    label_medium = a['data'][count]['labels']['medium']
                except KeyError: label_medium = None
                try: 
                    label_large = a['data'][count]['labels']['large']
                except KeyError: label_large = None
                try: 
                    created_at = a['data'][count]['createDate']
                except KeyError: created_at = None
                try: 
                    updated_at = a['data'][count]['updateDate']
                except KeyError: updated_at = None
                b = cur.execute("insert ignore into drinkinfo_beer_dim values (%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s)",                                       
                                (beer_key,
                                 catergoryId,
                                 styleId,
                                 glasswareId,
                                 beer_name,
                                 nameDisplay,
                                 description,
                                 abv,
                                 ibu,
                                 srmId,
                                 availableId,                                
                                 isOrganic,
                                 status,
                                 statusDisplay,
                                 servingTemperature,
                                 servingTemperatureDisplay,
                                 label_small,
                                 label_medium,
                                 label_large,
                                 created_at,
                                 updated_at
                                 )                
                )
                if total > commitcount:
                    c = cur.execute("commit;")
                    print(" rows inserted! ")
                    total = 0
                count = count + 1 
                total = total + 1
                
                                  
            loop = loop + 1
            print("PAGE: " + str(loop))
            count = 0
            
    @staticmethod
    def _testloadBeerDim():
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
        apiurl = 'http://api.brewerydb.com'
        apiver = '/v2'
        apiendpoint = '/beers'
        apikey = '/?key=8c4d0e5e6e7b4807f9adead425143dbb'
        page = 1
        posturl = apiurl + apiver + apiendpoint + apikey +  '&p=' + str(page)
        count = 0
        total = 0
        abv = ''
        loop = 0
        commitcount = 200     
        print(posturl)
      
        array = json.dumps(requests.get(posturl).json())
        a = json.loads(array)     
        print(a) 
        while a['currentPage'] <15:
            posturl = apiurl + apiver + apiendpoint + apikey +  '&p=' + str(loop)
            array = json.dumps(requests.get(posturl).json())
            a = json.loads(array) 
            #LOAD BEER DATA INTO MYSQL LOOP
            for beer_name in a['data']:
         
                beer_key = a['data'][count]['id']
                beer_name = a['data'][count]['name']
                try: 
                    nameDisplay = a['data'][count]['nameDisplay']
                except KeyError: nameDisplay = None
                try: 
                    catergoryId = a['data'][count]['style']['categoryId']
                except KeyError: catergoryId = None    
                try: 
                    description = a['data'][count]['description']
                except KeyError: description = None
                try: 
                    abv = a['data'][count]['abv']
                except KeyError: abv = None
                try: 
                    ibu = a['data'][count]['ibu']
                except KeyError: ibu = None
                try: 
                    glasswareId = a['data'][count]['glasswareId']
                except KeyError: glasswareId = None
                try: 
                    srmId = a['data'][count]['srmId']
                except KeyError: srmId = None
                try: 
                    availableId = a['data'][count]['availableId']
                except KeyError: availableId = None
                try: 
                    styleId = a['data'][count]['styleId']
                except KeyError: styleId = None
                try: 
                    isOrganic = a['data'][count]['isOrganic']
                except KeyError: isOrganic = None
                try: 
                    status = a['data'][count]['status']
                except KeyError: status = None
                try: 
                    statusDisplay = a['data'][count]['statusDisplay']
                except KeyError: statusDisplay = None
                try: 
                    servingTemperature = a['data'][count]['servingTemperature']
                except KeyError: servingTemperature = None
                try: 
                    servingTemperatureDisplay = a['data'][count]['servingTemperatureDisplay']
                except KeyError: servingTemperatureDisplay = None
                try: 
                    label_small = a['data'][count]['labels']['icon']
                except KeyError: label_small = None                
                try: 
                    label_medium = a['data'][count]['labels']['medium']
                except KeyError: label_medium = None
                try: 
                    label_large = a['data'][count]['labels']['large']
                except KeyError: label_large = None
                try: 
                    created_at = a['data'][count]['createDate']
                except KeyError: created_at = None
                try: 
                    updated_at = a['data'][count]['updateDate']
                except KeyError: updated_at = None
                b = cur.execute("insert ignore into drinkinfo_beer_dim values (%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s)",                                       
                                (beer_key,
                                 catergoryId,
                                 styleId,
                                 glasswareId,
                                 beer_name,
                                 nameDisplay,
                                 description,
                                 abv,
                                 ibu,
                                 srmId,
                                 availableId,                                
                                 isOrganic,
                                 status,
                                 statusDisplay,
                                 servingTemperature,
                                 servingTemperatureDisplay,
                                 label_small,
                                 label_medium,
                                 label_large,
                                 created_at,
                                 updated_at
                                 )                
                )
                if total > commitcount:
                    c = cur.execute("commit;")
                    print(" rows inserted! ")
                    total = 0
                count = count + 1 
                total = total + 1
                
                                  
            loop = loop + 1
            print("PAGE: " + str(loop))
            count = 0

          
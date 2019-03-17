#!/usr/bin/Python
import BreweryLoad, LocationDataLoad


    
#test


if __name__ == '__main__':
    ans=True
    while ans:
        print("""
        ------------DATABASE LOAD SCRIPT---------------------------------------
        1.Load Full Database(takes some time)
        2.Load Test Data
        3.Don't do it
        4.Location Load
        -----------------------------------------------------------------------
        """)
        ans=raw_input("What would you like to do? ")
        
        if ans=="1":
          BreweryLoad.BreweryLoad._loadBeerDim()
          print("\n DATALOADED!")
          exit()
          
        elif ans=="2":
          BreweryLoad.BreweryLoad._testloadBeerDim()
          print("\n TEST DATALOADED!")
          exit()
        elif ans=="3":
          setupserver.setupserver._setup_server()
          print("\n done!")
          exit()
        elif ans=="4":
          LocationDataLoad.LocationLoad._loadlocationdim()
          print("\n done!")
          exit()
        else:
           print("\n Not Valid Choice Try again") 




#     BreweryLoad.BreweryLoad._buildBeerTables()
#     BreweryLoad.BreweryLoad._loadBeerDim()
#     BreweryLoad.BreweryLoad._loadBeerStyleDim()1
#     BreweryLoad.BreweryLoad._loadBeerCategoryDim()
#     BreweryLoad.BreweryLoad._loadBeerGlassDim()
#     
#     
#     BreweryLoad.BreweryLoad._buildBreweryTables()
#     BreweryLoad.BreweryLoad._loadBreweryDim()
#     
#     
#     BreweryLoad.BreweryLoad._buildLocationTables()
#     BreweryLoad.BreweryLoad._loadLocationDim()
    
    print("finished!")


 
  
    

    
    
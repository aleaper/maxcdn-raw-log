#!/usr/bin/python

'''
An actual working MaxCDN python script to pull raw log information from MaxCDNs API this is a slightly 
altered version from https://www.maxcdn.com/one/tutorial/trivial-way-to-manage-maxcdn-account-with-python/ 
A list of their APIs https://docs.maxcdn.com/
'''

from maxcdn import MaxCDN

# You will have to replace the following with the API information
api = MaxCDN("alias", "key", "secret")

print "Hit [ENTER] to get it"                                                                                                                                                                                                     
while raw_input() != "exit":                                                                                                                                                                                                      
        def fetch(dfrom, dto, option, value, zid):                                                                                                                                                                                
                if option != "":                                                                                                                                                                                                  
                        option = "&" + option + "=" + value                                                                                                                                                                       
                if zid != "":                                                                                                                                                                                                     
                        zid = "&zone_id=" + zid                                                                                                                                                                                   
                # Needed to add zid to this variable Original did not have it listed
		data = api.get('/v3/reporting/logs.json?start=' + dfrom + '&end=' + dto + option + zid)                                                                                                                                 
                records = data['records']                                                                                                                                                                                         
                lines = len(records)                                                                                                                                                                                              
                for i in range(0, lines):                                                                                                                                                                                         
                        print "\nZone ID: "                                                                                                                                                                                       
                        print records[i]['zone_id']                                                                                                                                                                               
                        print "Source IP: "                                                                                                                                                                                       
                        print records[i]['client_ip']
			# Added the Time and Status
			print "Time: "
       			print records[i]['time']
       			print "Status: "
       			print records[i]['status']                                                                                                                                                                             
                        print "Uri: "                                                                                                                                                                                             
                        print records[i]['uri']                                                                                                                                                                                   
                        print "Referrer: "                                                                                                                                                                                        
                        print records[i]['referer']                                                                                                                                                                               
        print "--------------------------\nFilter Options - type the number in front of an option:\n--------------------------\n1. summary\n2. status codes\n3. referrers\n4. host names\n5. URi\n6. source ip\n"                 
        print "Type in the report type you need: "                                                                                                                                                                                
        type = raw_input()                                                                                                                                                                                                        
        if type == "1":                                                                                                                                                                                                           
                print "FROM: (yyyy-mm-dd)\n"                                                                                                                                                                                      
                dfrom = raw_input()                                                                                                                                                                                               
                print "TO: (yyyy-mm-dd)\n"                                                                                                                                                                                        
                dto = raw_input()                                                                                                                                                                                                 
                print "Zone ID: (Empty for all)\n"                                                                                                                                                                                
                zid = raw_input()                                                                                                                                                                                                 
                fetch(dfrom, dto, "", "", zid)
        if type == "2":
                print "FROM: (yyyy-mm-dd)\n"
                dfrom = raw_input()
                print "TO: (yyyy-mm-dd)\n"
                dto = raw_input()
                print "Zone ID: (Empty for all)\n"
                zid = raw_input()
                print "Status Code: \n"
                scode = raw_input()
                fetch(dfrom, dto, "status", scode, zid)
        if type == "3":
                print "FROM: (yyyy-mm-dd)\n"
                dfrom = raw_input()
                print "TO: (yyyy-mm-dd)\n"
                dto = raw_input()
                print "Zone ID: (Empty for all)\n"
                zid = raw_input()
                print "Referrer: \n"
                ref = raw_input()
                fetch(dfrom, dto, "referer", ref, zid)
        if type == "4":
                print "FROM: (yyyy-mm-dd)\n"
                dfrom = raw_input()
                print "TO: (yyyy-mm-dd)\n"
                dto = raw_input()
                print "Zone ID: (Empty for all)\n"
                zid = raw_input()
                print "Host Name: \n"
                hname = raw_input()
                fetch(dfrom, dto, "hostname", hname, zid)
        if type == "5":
                print "FROM: (yyyy-mm-dd)\n"
                dfrom = raw_input()
                print "TO: (yyyy-mm-dd)\n"
                dto = raw_input()
                print "Zone ID: (Empty for all)\n"
                zid = raw_input()
                print "URi: \n"
                uri = raw_input()
                fetch(dfrom, dto, "uri", uri, zid)
        if type == "6":
                print "FROM: (yyyy-mm-dd)\n"
                dfrom = raw_input()
                print "TO: (yyyy-mm-dd)\n"
                dto = raw_input()
                print "Zone ID: (Empty for all)\n"
                zid = raw_input()
                print "Source IP: \n"
                cip = raw_input()
                fetch(dfrom, dto, "client_ip", cip, zid)
        print "Hit [enter] to return to menu or type 'exit' to go back"

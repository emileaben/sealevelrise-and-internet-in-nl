#!/usr/bin/env python3
import requests
import json
import io
import csv

r = requests.get("https://www.peeringdb.com/api/fac?country=NL")
j = json.loads( r.content.decode('utf-8') ) 
#r.json()
with io.open('facilities.NL.csv','w') as outf:
    #csvout = csv.writer(outf) # , dialect='excel')
    #fieldnames = ['pdb_id','name','net_count','latitude','longitude','address1','address2','city']
    #csvout.writeheader(fieldnames)
    #csvout.writeheader()
    #for fac in j['data']:
    #    csvout.writerow([
    #        fac['id'],
    #        fac['name'],
    #        fac['net_count'],
    #        fac['latitude'],
    #        fac['longitude'],
    #        fac['address1'],
    #        fac['address2'],
    #        fac['city']
    #    ])
    print("#pdb_id, name, net_count, latitude, longitude, address1, address2, city",
        file=outf
    )
    for fac in j['data']:
        print( u'%s,"%s",%s, %s, %s,"%s","%s","%s"' % (
            fac['id'],
            fac['name'],
            fac['net_count'],
            fac['latitude'],
            fac['longitude'],
            fac['address1'],
            fac['address2'],
            fac['city']
        ), file=outf )

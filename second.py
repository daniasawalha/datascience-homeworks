# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:53:41 2022

@author: Dania
"""

from faker import Faker
import json
output=open('data.json','w')
fake=Faker()
alldata={}
alldata['records']=[]
for i in range(1000):
    data={"name":fake.name(),"age":fake.random_int(min=18,max=80,step=1),"street":fake.street_address(),
          "city":fake.city(),"state":fake.state(),"zip":fake.zipcode(),"lng":float(fake.longitude()),"lat":float(fake.latitude())}
    alldata['records'].append(data)
json.dump(alldata,output)
with open("data.json",'r') as f:
    data=json.load(f)
    print(data['records'][0]['name'])


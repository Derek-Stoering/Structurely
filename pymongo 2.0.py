#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#conda install dnspython
#python -m pip install pymongo[srv]

import pymongo
import dns
import mongokeys
###mongokeys is where username and password are stored for mongodb

client = pymongo.MongoClient(f"mongodb+srv://{mongokeys.username}:{mongokeys.password}@cluster0.pqca2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

mylist = [
  { "_id": (vinny_id), "Lead_type": (lead_type_db), "Context": (context_db), "Bot_message": (bot_message_str), "Lead_message": (lead_message_str), "Intents_slots": (intents_str) },
]

x = mycol.insert_one(mylist)


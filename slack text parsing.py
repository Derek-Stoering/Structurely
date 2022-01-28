#!/usr/bin/env python
# coding: utf-8

# In[18]:


import re

context = 'Context:'

message = """vinny id: 61e85b947c9491b814ffa2a8, Moist Chicken Fingers :white_check_mark:
(claimed by @Derek Stoering) (edited) 
Task type: start of convo (make sure to include lead type)
Lead types: buyer
Allowed domains: real_estate
Context: received_information
Confidence: 0.3623
Show more
:robot_face: Last bot message:
Hello Allen! This is Denisha's assistant with The Dianna Romans Group (Keller Williams). I had a note you viewed some properties on Facebook in the Lubbock area. Are you looking for yourself or for someone else? If you're not interested in being texted, just let me know. <BREAK>
Can you confirm if this is Allen's number or if someone gave us the wrong info? If this is Allen's number, this is Denisha's assistant w/ The Dianna Romans Group (Keller Williams) and I found a few listings in Lubbock on our website. Here is a link: https://search.diannaromans.com/t/XPJ2F
:speech_balloon: Lead message:
This Is allen sorry for the delay just talking things over we may end up holding off on the house situation till we can get some work history under our belts here
Predicted intent: reconnect_later
New intents approved
New intent: fill_slot :arrow_left:
-- ► contact_confirmation: true"""
words = message.split() 

print( "vinny ID:" , words[2] )

match=(re.search(pattern, string))


# In[ ]:





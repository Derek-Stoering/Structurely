#!/usr/bin/env python
# coding: utf-8

# In[89]:


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
bot_message = []
lead_message = []

print(words)
print("")
vinny_id_temp = words.index("id:")
vinny_id_temp +=1
print( "Vinny id:" , words[vinny_id_temp] )

lead_types_temp = words.index("types:")
lead_types_temp +=1
print( "Lead Type:" , words[lead_types_temp] )

context_temp = words.index("Context:")
context_temp +=1
print( "Context:" , words[context_temp] )

body_temp = words.index(":robot_face:")
print("Bot Message:")
while words[body_temp] != ":speech_balloon:":
    body_temp += 1
    bot_message.append(words[body_temp])
    
del bot_message[0]
del bot_message[0]
del bot_message[0]
del bot_message[-1]    
bot_message_str = ' '.join(bot_message)
print(bot_message_str)   

lead_temp = words.index(":speech_balloon:")
print("Lead Message:")
while words[lead_temp] != "Predicted":
    lead_temp += 1
    lead_message.append(words[lead_temp])
    
del lead_message[0]
del lead_message[0]
del lead_message[-1]    
lead_message_str = ' '.join(lead_message)
print(lead_message_str)
print("")

intent_temp = words.index("intent:")
intent_temp +=1
print( "Intents Used:" , words[intent_temp],)

slot_temp = words.index("►")
slot_temp +=1
print( "Slots Used:" , words[slot_temp], "_", words[slot_temp + 1] )


# In[ ]:





# In[ ]:





# In[ ]:





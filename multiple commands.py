#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from datetime import datetime

app = App(token="xoxb-2970213766022-2976934764882-pf5VMdXnTiE1N4mAdFAKQevk")

total_leads = 0
total_leads_annotated = 0
total_leads_approved = 0

def metric_track(message_temp):
    global total_leads
    global total_leads_annotated
    global total_leads_approved
    global message1
    
    message_str = message_temp
    
    if 'New intents approved' in message_str:
        total_leads_annotated +=1
        total_leads +=1
    if 'Prediction approved' in message_str:
        total_leads_approved +=1
        total_leads +=1
        
    precent_leads_annotated = (total_leads_annotated / total_leads) * 100
    precent_leads_predicted = precent_leads_annotated - 100
    
    print(message_str)

    print(f'\n Total Leads annotated: ', total_leads_annotated, ', Precent:', precent_leads_annotated, '%')
    print(f'\n Total Vinny Predictions Approved: ', total_leads_approved, ', Precent:', precent_leads_predicted, '%')
    print(f'\n Total Leads: ', total_leads)


@app.event({
    "type": "message",
    "subtype": "message_changed"
})
def message_tracker(event, say):
    global message2
    message1 = event['message']
    message2 = message1['text']
    if ':white_check_mark:' in message2:
        metric_track(message2)
        
@app.event({"type": "message"}, middleware=[extract_subtype])
def just_ack(logger, context):
    subtype = context["subtype"] 

        
@app.command("/sentiment report")
def repeat_text(ack, respond, command):
    current_date_time = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    
    ack()
    respond(f"{command['Generating Report...']}")
        
    sentiment_report_gen()
        
    file_name = ("report_gen" + current_date_time)
            
    channel_id = "vinny-analysis"
        
    result = client.files_upload(
    channels = channel_id,
    initial_comment = ("Here's your for:" + current_date_time),
    file=file_name,
        
@app.command("/metric report")
def repeat_text(ack, respond, command): 
    current_date_time = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        
    ack()
    respond(f"{command['Generating Report...']}")
        
    metric_report_gen()
    
    file_name = ('report_gen' + current_date_time)

    channel_id = "vinny-analysis"
            
    result = client.files_upload(
    channels = channel_id,
    initial_comment = ("Here's your report for:" + current_date_time)
    file=file_name,

    
if __name__ == "__main__":
    SocketModeHandler(app, "xapp-1-A02UJ6YTLEA-3023246363889-a2fddf4485c6ab0be3d7a7586522a0d446dce8f9cd82012d887abe21c2655eed").start()
   
    


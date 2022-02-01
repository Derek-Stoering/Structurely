#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from datetime import datetime
#pip install fpdf
from fpdf import FPDF

app = App(token="xoxb-2970213766022-2976934764882-pf5VMdXnTiE1N4mAdFAKQevk")

total_leads = 0
total_leads_annotated = 0
total_leads_approved = 0

def text_parse(message_temp):
    global message1 
    message = message1
    words = message.split() 
    bot_message = []
    lead_message = []
    intents_lst = []

    print(words)
    print("")
    vinny_id_temp = words.index("id:")
    vinny_id_temp +=1
    print( "Vinny id:" , words[vinny_id_temp] )
    ###vinny id var

    lead_types_temp = words.index("types:")
    lead_types_temp +=1
    print( "Lead Type:" , words[lead_types_temp] )
    ###lead type var

    context_temp = words.index("Context:")
    context_temp +=1
    print( "Context:" , words[context_temp] )
    ###context var

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
    ###bot message var
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
    ###lead message var
    print(lead_message_str)

    intents_temp = words.index("Predicted")
    print("Slots and Intents:")
    while intents_temp < len(words)-1:
        intents_temp += 1
        intents_lst.append(words[intents_temp])

    intents_str = ' '.join(intents_lst)
    ###intents var
    print(intents_str)   

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
    text_parse()
        
    precent_leads_annotated = (total_leads_annotated / total_leads) * 100
    precent_leads_predicted = precent_leads_annotated - 100
    
    print(message_str)

    print(f'\n Total Leads annotated: ', total_leads_annotated, ', Precent:', precent_leads_annotated, '%')
    print(f'\n Total Vinny Predictions Approved: ', total_leads_approved, ', Precent:', precent_leads_predicted, '%')
    print(f'\n Total Leads: ', total_leads)
    
    #------------------------------------------------------
    
    
    
def sentiment_track(message_temp):
    
    
    
    
    
    
    
    
    
    
    
    

def sentiment_report_gen():
     # 1. Set up the PDF doc basics
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    # 2. Layout the PDF doc contents
    ## Title
    pdf.cell(40, 10, 'Slack Sentiment Report')
    ## Line breaks
    pdf.ln(20)
    ## Image
    pdf.image('sentiment_chart.png')
    ## Line breaks
    pdf.ln(20)
    ## Show table of historical data
    ### Transform the DataFrame to include index of Date
    sp500_history_pdf = sp500_history.reset_index()
    ### Transform the Date column as str dtype
    sp500_history_pdf['Date'] = sp500_history_pdf['Date'].astype(str)
    ### Round the numeric columns to 2 decimals
    numeric_cols = sp500_history_pdf.select_dtypes(include='number').columns
    sp500_history_pdf[numeric_cols] = sp500_history_pdf[numeric_cols].round(2)
    ### Use the function defined earlier to print the DataFrame as a table on the PDF 
    output_df_to_pdf(pdf, sp500_history_pdf.tail(3))
    ## Line breaks
    pdf.ln(20)
    ## Show table of historical summary data
    sp500_history_summary_pdf = sp500_history_summary.reset_index()
    numeric_cols = sp500_history_summary_pdf.select_dtypes(include='number').columns
    sp500_history_summary_pdf[numeric_cols] = sp500_history_summary_pdf[numeric_cols].round(2)

    output_df_to_pdf(pdf, sp500_history_summary_pdf)
    # 3. Output the PDF file
    pdf.output('fpdf_pdf_report.pdf', 'F')
    
    
    
def metric_report_gen():
     # 1. Set up the PDF doc basics
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    # 2. Layout the PDF doc contents
    ## Title
    pdf.cell(40, 10, 'Slack Metrics Report')
    ## Line breaks
    pdf.ln(20)
    ## Image
    pdf.image('metric_chart.png')
    ## Line breaks
    pdf.ln(20)
    ## Show table of historical data
    ### Transform the DataFrame to include index of Date
    sp500_history_pdf = sp500_history.reset_index()
    ### Transform the Date column as str dtype
    sp500_history_pdf['Date'] = sp500_history_pdf['Date'].astype(str)
    ### Round the numeric columns to 2 decimals
    numeric_cols = sp500_history_pdf.select_dtypes(include='number').columns
    sp500_history_pdf[numeric_cols] = sp500_history_pdf[numeric_cols].round(2)
    ### Use the function defined earlier to print the DataFrame as a table on the PDF 
    output_df_to_pdf(pdf, sp500_history_pdf.tail(3))
    ## Line breaks
    pdf.ln(20)
    ## Show table of historical summary data
    sp500_history_summary_pdf = sp500_history_summary.reset_index()
    numeric_cols = sp500_history_summary_pdf.select_dtypes(include='number').columns
    sp500_history_summary_pdf[numeric_cols] = sp500_history_summary_pdf[numeric_cols].round(2)

    output_df_to_pdf(pdf, sp500_history_summary_pdf)
    # 3. Output the PDF file
    pdf.output('fpdf_pdf_report.pdf', 'F')

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
        sentiment_track(message2)
        
@app.event({"type": "message"}, middleware=[extract_subtype])
def just_ack(logger, context):
    subtype = context["subtype"] 

        
@app.command("/sentiment report")
def sentiment_report(ack, respond, command):
    current_date_time = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    
    ack("Generating Sentiment Report...")
        
    #sentiment_report_gen()
        
    #file_name = ("report_gen" + current_date_time)
            
    #channel_id = "vinny-analysis"
        
    #result = client.files_upload(channels = channel_id,initial_comment = ("Here is your report for:" + current_date_time),
    #file=file_name
        
@app.command("/metric report")
def metric_report(ack, respond, command): 
    current_date_time = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        
    ack("Generating Metric Report...")
        
    #metric_report_gen()
    
    #file_name = ('report_gen' + current_date_time)

    #channel_id = "vinny-analysis"
            
    #result = client.files_upload(
    #channels = channel_id,
    #initial_comment = ("Here is your report for:" + current_date_time)
    #file=file_name

    
if __name__ == "__main__":
    SocketModeHandler(app, "xapp-1-A02UJ6YTLEA-3023246363889-a2fddf4485c6ab0be3d7a7586522a0d446dce8f9cd82012d887abe21c2655eed").start()
   


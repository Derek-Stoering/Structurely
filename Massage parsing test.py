#!/usr/bin/env python
# coding: utf-8

# In[19]:


import string
import os

total_leads = 0
total_leads_annotated = 0
total_leads_approved = 0

message_str = """vinny id: 61e85b783a1889467b44b77b, Piping Apple Sauce :white_check_mark: 
(claimed by @Derek Stoering) (edited) 
Task type: messageLead types: buyer
Allowed domains: real_estateContext: expect_motivationConfidence: 0.5661
Open in dashboard
Go to convo
:robot_face:
 Last bot message:
Hi Allan - Are you still looking to make a move in 3 to 6 months or just browsing? - Dennis
:speech_balloon: Lead message:
Looking to move in 3 to 6 if I can find a suitable place to move to.
Predicted intent: fill_slot
-- ► timeframe: 3 to 6
Predicted intent: cancel_slot
New intents approved
N*ew intent: fill_slot* 
:arrow_left:
-- ► timeframe: 3 to 6
New intent: cancel_slot :arrow_left:"""

total_lead +=1

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


# In[20]:


@app.command("/report")
def repeat_text(ack, respond, command):
    # Acknowledge command request
    ack()
    respond(f"{command['Generating Report...']}")
    
    report_gen_meathod()

file_name = 'report_gen'
# ID of channel that you want to upload file to
channel_id = "C12345"

# Call the files.upload method using the WebClient
# Uploading files requires the `files:write` scope
result = client.files_upload(
channels = channel_id,
initial_comment = "Here's your report :smile:",
file=file_name,
    


# In[25]:


#pip install fpdf
from fpdf import FPDF

def report_gen_meathod():
    # 1. Set up the PDF doc basics
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    # 2. Layout the PDF doc contents
    ## Title
    pdf.cell(40, 10, 'Slack Analytics Report')
    ## Line breaks
    pdf.ln(20)
    ## Image
    pdf.image('chart.png')
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


# In[ ]:





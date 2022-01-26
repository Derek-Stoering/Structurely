#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token="xoxb-2970213766022-2976934764882-q5DRvDojNKE5SSMKR2QDGVN7")


@app.message(":white_check_mark:")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"{message['text']}")    
    
if __name__ == "__main__":
    SocketModeHandler(app, "xapp-1-A02UJ6YTLEA-2989274523474-384bd83b165274dd94c6bd11382a371a8fb93d60c68ea25150c59f9e483766dc").start()


# In[ ]:





# In[ ]:





# Rowan-bragging-detector
Detects if Rowan or anyone else is bragging about food

Basic process:
1) Takes all messages sent by Rowan or anyone else specifically. All other messages are ignored
2) Sees if the message contains any words that might suggest bragging i.e. "Donut", "Steak", "Ate", etc.
3) Assigns the whole message a confidence value to determine how sure it is that he's bragging 
4) Returns whatever I put as the response

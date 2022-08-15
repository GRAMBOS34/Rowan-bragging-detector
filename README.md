# Rowan-bragging-detector
Detects if Rowan or anyone else is bragging about food

Basic process:
1) Takes all messages sent by Rowan or anyone else specifically. All other messages are ignored
2) Sees if the message contains any words that might suggest bragging i.e. "Donut", "Steak", "Ate", etc.
3) Assigns the whole message a confidence value to determine how sure it is that he's bragging 
4) Returns whatever I put as the response

# Miscellaneous notes
1) Facebook/Meta and by extension, Messenger, doesn't have an API(Application Programming Interface) so this is a pain in the ass to make 
2) Feel free to edit the code, I won't stop you because I physically don't care and can't anyway
3) This program won't be the fastest out there because I'm too lazy to make it so
4) This would've been easier if we mostly talked through Discord tbh since Discord has an API(Application Programming Interface)

# Updates
Aug. 15, 2022: Implemented the basic functionality of the "Bragging Confidence" system

Aug. 15, 2022 (20:11): Started working on the connection code :D

Aug. 15, 2022 (20:14): Figured out that I can't connect to Messenger using code so I'll try something else (Maybe screen scraping idk)

Aug. 15, 2022 (20:17): Found an unofficial fb api (https://github.com/Schmavery/facebook-chat-api) so I'll try using that

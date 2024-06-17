import re
from nltk.corpus import wordnet
words=['hello','timings','rating','location']
syn={}
for word in words:
    synonyms=[]
    for x in wordnet.synsets(word):
        for lem in x.lemmas():
            lem_name = re.sub(r'[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.append(lem_name)
    syn[word]=set(synonyms)
#print (syn)
keywords={}
keywords_dict={}
keywords['greet']=[]
 
for synonym in list(syn['hello']):
    keywords['greet'].append('.*\\b'+synonym+'\\b.*')

keywords['location']=[]

for synonym in list(syn['location']):
    keywords['location'].append('.*\\b'+synonym+'\\b.*')

keywords['timings']=[]

for synonym in list(syn['timings']):
    keywords['timings'].append('.*\\b'+synonym+'\\b.*')

keywords['rating']=[]

for synonym in list(syn['rating']):
    keywords['rating'].append('.*\\b'+synonym+'\\b.*')

for intent, keys in keywords.items():
    keywords_dict[intent]=re.compile('|'.join(keys))
#print (keywords_dict)
responses={
    'greet':'Hello! How can I help you?',
    'timings':'We are open from 9AM to 5PM, Monday to Sunday.',
    'rating':'5-Star Rating',
    'location':'Address: 654 Charminar Road, Hyderabad, Telangana',
    'fallback':'I dont quite understand. Could you repeat that?',
}
print ("Welcome to Taj Restaurant. How may I help you?")
while (True):  
    user_input = input().lower()
    if user_input == 'quit': 
        print ("Thank you for visiting.")
        break    
    matched_intent = None 
    for intent,pattern in keywords_dict.items():
        if re.search(pattern, user_input): 
           matched_intent=intent  
    key='fallback' 
    if matched_intent in responses:
        key = matched_intent
    print (responses[key]) 

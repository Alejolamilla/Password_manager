import json

English = {'keyword_in1' : 'Site: ',
'user' : 'Username: ',
'password' : 'Password: ',
'corrUser': 'The user {} was creat correctly!',
'wrongUser': 'The user {} was not created correctly, be sure the user containd just alphanumeric letters (a-z or A-Z) and (0-9), or next symbols ({}) , without spaces.',
'wrongpass': 'The password was not created correctly, be sure the user containd just alphanumeric letters (a-z or A-Z) and (0-9), or next symbols ({}) , without spaces.',
'passAgain': 'Write a correct password: ',
'keyAgain': 'Write a correct site name: ',
'userAgain': 'Write a correct username: ',
'shortPass': 'The password is too short and weakness, try with minimum 6 characters',}

with open("English.json", "w") as outfile:
    json.dump(English, outfile)
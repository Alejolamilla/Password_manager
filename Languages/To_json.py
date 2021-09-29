import json

# English = {'keyword_in1' : 'Site: ',
# 'user' : 'Username: ',
# 'password' : 'Password: ',
# 'corrUser': 'The user {} was creat correctly!',
# 'wrongUser': 'The user {} was not created correctly, be sure the user containd just alphanumeric letters (a-z or A-Z) and (0-9), or next symbols ({}) , without spaces.',
# 'wrongpass': 'The password was not created correctly, be sure the user containd just alphanumeric letters (a-z or A-Z) and (0-9), or next symbols ({}) , without spaces.',
# 'passAgain': 'Write a correct password: ',
# 'keyAgain': 'Write a correct site name: ',
# 'userAgain': 'Write a correct username: ',
# 'shortPass': 'The password is too short and weakness, try with minimum 6 characters',}

Español ={'user': 'Usuario o correo: ',
'password': 'Contraseña: ',
'sign_in':'Entrar',
'not_account': '¿No tiene una cuenta aún?',
'sign_up':'Registrarse',
'out_len':'El usuario y contraseña deben tener entre 5 y 25 caracteres',
'unexistent_user':'El usuario {} no existe',
'unmatch_password':'La contraseña no coincide',
'unknown_error':'Surgio un error, intente nuevamente',
'many_tries':'Demasiados intentos, intente de nuevo en unos minutos',
}

English ={'user': 'User or email: ',
'password': 'Password: ',
'sign_in':'Log in',
'not_account': "Don't have an account yet?",
'sign_up':'Sign up',
'out_len':'User and password shoul have between 5 and 25 characters',
'unexistent_user': "User {} doesn't exists",
'unmatch_password':"The password doesn't match",
'unknown_error':'Unknown error, try again',
'many_tries':'Too many tries, try again in some minutes',
}

with open("Español.json", "w") as outfile:
    json.dump(Español, outfile)

with open("English.json", "w") as outfile:
    json.dump(English, outfile)
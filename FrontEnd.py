from os import link
import string
from pathlib import Path
from dash import html
from dash import dcc
from dash.html.H4 import H4

# Permited characters
perm_chars = string.ascii_letters+ string.digits+ 'ñÑ'+ string.punctuation

# def read_languages():

#     languages = []

#     for p in Path('.').glob('Languages/*.json'):
#         languages.append({'label':f"{p.name}"[0:-5], 'value':f"{p.name}"[0:-5]})

#     return languages

def home(text):
    home = [
        #     html.Div(className='language_drop',
        #     children=[
        #         dcc.Dropdown(
        #         id='language-dropdown',
        #         optionHeight= 60,
        #         options=read_languages(),
        #         value='Español',
        #         clearable=False)
        # ]),
            # ------------------------------------Title--------------------------------------------
            html.Div(className ='app-header',
                children=[html.H1("Password Manager")]),

            # ------------------------------------Output-Message--------------------------------------------
            html.Div(className='error_message', id='error_message_login', children=[]),
            html.Br(),

            # ------------------------------------Inputs--------------------------------------------
        html.Form(id='login_form', acceptCharset= perm_chars, children=[
            html.Div(className= 'grid-container',
            children=[
                html.Div(className= 'input-name', id='input-name', children=[text['user']]),
                html.Div(className= 'input-box',
                children=[
                    dcc.Input(id='Name-input', type='text'),
                    ]),

                html.Div(className= 'input-name', id='input-password',children=[text['password']]),
                html.Div(className= 'input-box',
                    children=[
                        dcc.Input(id='password-input', type='password'),
                        ])
            ])
        ]),
            # -------------------------------------Button-------------------------------------------
            html.Div(className='button-container', id='b-container-1',
            children=[html.Button(text['sign_in'], className='button', id='btn-login', n_clicks=0)]),

            # -------------------------------------Register-------------------------------------------
            html.Div(className= 'span-text', id='not-account-span', children=[text['not_account']]),

            html.Div(className='button-container',
            children=[html.Button(text['sign_up'], className='button', id='btn-signup', n_clicks=0)]),
    ]

    return home

# ==================================================================================================================

def sign_up(text):
    register_tab=[
        html.Div(className ='app-header',
                children=[html.H1("Password Manager")]),
    # ----------------------------------------------------------------------------------------
        html.Div(className='span-text', children=text['register']),
        html.Br(),
        html.Br(),
        html.Div('', className='error_message', id='error_message_signup'),

        html.Form(id='signup_form', acceptCharset= perm_chars, children=[
            html.Div(className= 'grid-container', children=[
             html.Div(className= 'input-name', id='sign-name', children=[text['username']]),
                html.Div(className= 'input-box',
                children=[dcc.Input(id='name-signup', value='', type='text'),]),

                html.Div(className= 'input-name', id='sign-password', children=[text['password']]),
                html.Div(className= 'input-box',
                    children=[dcc.Input(id='password-sign', value='', type='password'),]),

                html.Div(className= 'input-name', id='sign-password-verification', children=[text['password_verif']]),
                html.Div(className= 'input-box',
                    children=[dcc.Input(id='password-sign-verif', value='', type='password'),]),

                html.Div(className= 'input-name', id='sign-email', children=[text['email']]),
                html.Div(className= 'input-box',
                    children=[dcc.Input(id='email-sign', value='', type='text'),]),
            ])
        ]),
    # ----------------------------------------Button------------------------------------------------
        html.Div(className='button-container',
        children=[html.Button(text['sign_up'], className='button', id='btn-register', n_clicks=0)])

    ]
    return register_tab

Front_2= [
    html.Div(['Pagina 2']),
    html.Div(['Pagina 2']),
    html.Div(['Pagina 2']),
    html.Div(['Pagina 2']),
    html.Div(['Pagina 2']),
]


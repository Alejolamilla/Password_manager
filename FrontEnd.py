import string
from pathlib import Path
from dash import html
from dash import dcc

# Permited characters
perm_chars = string.ascii_letters+ string.digits+ 'ñÑ'+ string.punctuation

def read_languages():

    languages = []

    for p in Path('.').glob('Languages/*.json'):
        languages.append({'label':f"{p.name}"[0:-5], 'value':f"{p.name}"[0:-5]})

    return languages

# ------------------------------------------Language-------------------------------------------------

Front = [
        dcc.Store(id='language'),

        html.Div(className='language_drop',
            children=[
                dcc.Dropdown(
                id='language-dropdown',
                optionHeight= 60,
                options=read_languages(),
                value='Español'),
            ]),

            # ------------------------------------Title--------------------------------------------
            html.Div(className ='app-header',
                children=[html.H1("Password Manager")]),

            # ------------------------------------Output-Message--------------------------------------------
            html.Div(id='error_message'),
            html.Br(),

            # ------------------------------------Inputs--------------------------------------------
        html.Form(id='login_form', acceptCharset= perm_chars, children=[
            html.Div(className= 'grid-container',
            children=[
                html.Div(className= 'input-name', id='input-name'),
                html.Div(className= 'input-box',
                children=[
                    dcc.Input(id='Name-input', value='', type='text'),
                    ]),

                html.Div(className= 'input-name', id='input-password',children=['Password: ']),
                html.Div(className= 'input-box',
                    children=[
                        dcc.Input(id='password-input', value='', type='password'),
                        ])
            ])
        ]),
            # -------------------------------------Button-------------------------------------------
            html.Div(className='button-container', id='b-container-1',
            children=[html.Button('submit', className='button', id='btn-login', n_clicks=0)]),

            # -------------------------------------Register-------------------------------------------
            html.Div(className= 'span-text', id='not-account-span', children=["Doesn't have an account yet?"]),

            html.Div(className='button-container',
            children=[html.Button('Register', className='button', id='btn-signup', n_clicks=0)]),
    ]

Front_2= [
    html.Div(['Pagina 2']),
    html.Div(['Pagina 2']),
    html.Div(['Pagina 2']),
    html.Div(['Pagina 2']),
    html.Div(['Pagina 2']),
]
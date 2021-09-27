import json
from pathlib import Path
from dash import html
from dash import dcc
from dash.html.Div import Div

def read_languages():

    languages = []

    for p in Path('.').glob('Languages/*.json'):
        languages.append({'label':f"{p.name}"[0:-8], 'value':f"{p.name}"[-7:-5]})

    return languages

# -------------------------------------------------------------------------------------------

Front = html.Div(className='body',
    children=[
        html.Div(className='language_drop',
            children=[
                dcc.Dropdown(
                id='language-dropdown',
                optionHeight= 60,
                options=read_languages(),
                value='Sp'),
            ]),
            # --------------------------------------------------------------------------------
            html.Div(className ='app-header',
                children=[html.H1("Password Manager")]),

            html.Div(className= 'input-data',
                children=[
                    "Name: ",
                    dcc.Input(id='Name-input', value='', type='text'),
                    ]),

            html.Br(),

            html.Div(className= 'input-data',
                children=[
                "Password: ",
                dcc.Input(id='password-input', value='', type='text'),
                ]),

            html.Div(className='button',
            children=[html.Button('submit', id='btn-nclicks-1', n_clicks=0)]),
            html.Br(),
            html.Div(id='my-output'),
    ])
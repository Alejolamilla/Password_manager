import json
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from FrontEnd import home

layout = html.Div([

    html.Div(id='home_content')
])

@app.callback(
    Output('home_content','children'),
    Input('language', 'data')
)
def change_language(text):
    return home(text)

@app.callback(
    Output('url', 'pathname'),
    Input('btn-signup', 'n_clicks'),
    Input('error_message_signup', 'children')
)
def new_user(clicks, message):

    if clicks<1:
        raise PreventUpdate

    elif message == 'The user was created successfully':
        return '/succes'
    
    elif message==None:
        raise PreventUpdate

    else:
        return '/app2'
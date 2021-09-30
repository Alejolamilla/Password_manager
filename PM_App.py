import json
from logging import error
import CRUD
from pathlib import Path
from FrontEnd import front, Front_2
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State


def read_languages():

    languages = []

    for p in Path('.').glob('Languages/*.json'):
        languages.append({'label':f"{p.name}"[0:-5], 'value':f"{p.name}"[0:-5]})

    return languages
#==============================================================================================

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),

    dcc.Store(id='language'),

    html.Div(className='language_drop',
        children=[
            dcc.Dropdown(
            id='language-dropdown',
            optionHeight= 60,
            options=read_languages(),
            value='Español'),
        ]),

    html.Div(id = 'app-content', children=front())
    ])

@app.callback(
    Output('app-content', 'children'),
    Input('url','pathname'),
    State(component_id='btn-login', component_property='n_clicks'),
    State(component_id='Name-input', component_property='value'),
    State(component_id='password-input', component_property='value'),
    State('error_message', 'children'),
)
def change_page(pathname, clicks, name_value, password_value, error):

    if pathname == '/user':
        return Front_2
    else: return front(name_value, password_value, clicks, error)

# --------------------------------------------------------------------------------
@app.callback(
    Output('language','data'),
    Input('language-dropdown','value'),
)
def select_language(value):

    text = json.load(open('Languages/'+value+'.json', 'r'))
    return text

# --------------------------------------------------------------------------------
@app.callback(
    Output('input-name','children'),
    Output('input-password','children'),
    Output('btn-login','children'),
    Output('not-account-span','children'),
    Output('btn-signup','children'),
    Input('language','data')
)
def change_language(text):
    return text['user'], text['password'], text['sign_in'], text['not_account'], text['sign_up']

# --------------------------------------------------------------------------------
@app.callback(
    Output(component_id='error_message', component_property='children'),
    State(component_id='Name-input', component_property='value'),
    State(component_id='password-input', component_property='value'),
    Input(component_id='btn-login', component_property='n_clicks'),
    Input('language','data')
)
def verifying_user(name, password, n_clicks, text):

    if (len(name) < 5 or len(password) < 5) or (len(name) > 25 or len(password) > 25):
            return text['out_len']
    else:
        if n_clicks > 0 and n_clicks <= 10:
            message = CRUD.user_verification(name, password)
            if message == 'success':
                return 'loged_in'
            elif message == 'unexistent':
                return text['unexistent_user'].format(name)
            elif message == 'unmatch_password':
                return text['unmatch_password']
            else: return text['unknow_error']

        elif n_clicks > 10: return text['many_tries']

        else: return ''

@app.callback(
    Output('url','pathname'),
    Input('error_message', 'children'),
)

def log_in(message):

    if message == 'loged_in':
        return '/user'
    else: return ''
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
if __name__ == '__main__':
    # app.run_server(debug=True, host= '26.228.152.186')
    app.run_server(debug=True, host= '0.0.0.0')
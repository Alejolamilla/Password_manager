import json
from logging import error
import CRUD

from FrontEnd import front, sign_up,Front_2
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State



#==============================================Frontend=========================================

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    dcc.Store(id='language'),
    dcc.Store(id='messages'),


    html.Div(id = 'app-content')
    ])
# ========================================Languages==============================================

@app.callback(
    Output('language','data'),
    Input('language-dropdown','value'),
)
def select_language(value='Español'):

    text = json.load(open('Languages/'+value+'.json', 'r'))
    return text
#---------------------------------------------------------------------
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

# ========================================Change-page==============================================

@app.callback(
    Output('app-content', 'children'),
    Input('url','pathname'),
    Input('language', 'data'),
)
def change_page(pathname, language):

    if pathname == '/user':
        return Front_2
    elif pathname == '/register':
        return sign_up(language)
    else: return front()


# ========================================BD==============================================

@app.callback(
    Output(component_id='error_message_login', component_property='children'),
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
    Output('error_message_signup', 'children'),
    Input('language','data'),
    Input('btn-register', 'n_clicks'),
    State('sign-name', 'value'),
    State('sign-password', 'value'),
    State('sign-password-verf', 'value'),
    State('sign-email', 'value'),
    prevent_initial_call=True
)
def sign_up_new_user(text, clicks, name, password, verification, email):

    if len(name)<5 or len(password)<5 or len(name)>25 or len(password)>25:
        return 'out_len'
    else:
        if  password == verification:

            message = CRUD.new_user(name, password, email)

            if clicks>0:
                if message == 'duplicate error':
                    return text['already_exist']
                elif message =='success':
                    return text['created']
                else:
                    return text['unknown_error']
            else:
                return dash.no_update
        else:
            return text['not_match']


# ========================================Redirect==============================================

@app.callback(
    Output('url','pathname'),
    Input('error_message_login', 'children'),
    Input('btn-signup', 'n_clicks')
)

def log_in(message, sign_up):

    if message == 'loged_in':
        return '/user'
    elif sign_up > 0:
        return '/register'
    else:
        return dash.no_update

# ========================================Run-App==============================================

if __name__ == '__main__':
    # app.run_server(debug=True, host= '26.228.152.186')
    app.run_server(debug=True, host= '0.0.0.0')
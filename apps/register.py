import CRUD
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import dash
from dash.exceptions import PreventUpdate

from app import app
from FrontEnd import sign_up

layout = html.Div(id='reg_content')

@app.callback(
    Output('reg_content','children'),
    Input('language', 'data')
)
def change_language(text):
    return sign_up(text)

# ---------------------------------------------------------------------------------
@app.callback(
    Output('error_message_signup', 'children'),
    Input('language','data'),
    Input('btn-register', 'n_clicks'),
    State('name-signup', 'value'),
    State('password-sign', 'value'),
    State('password-sign-verif', 'value'),
    State('sign-email', 'value'),
)
def sign_up_new_user( text, clicks, name, password, verification, email):

    if clicks>0:
        if name==None or password==None or len(name)<5 or len(password)<5 or len(name)>25 or len(password)>25:
            return text['out_len']
        else:
            if  password == verification:

                message = CRUD.new_user(name, password, email)

                if message == 'duplicate error':
                    return text['already_exist']
                elif message =='success':
                    return text['created']
                else:
                    return text['unknown_error']

            else:
                return text['not_match']
    else:
        return dash.no_update
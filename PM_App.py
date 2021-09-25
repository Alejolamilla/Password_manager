import CRUD
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H4("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Name: ",
        dcc.Input(id='Name-input', value='', type='text'),
        ]),
    html.Br(),
    html.Div([
        "Password: ",
        dcc.Input(id='password-input', value='', type='text'),
        html.Button('submit', id='btn-nclicks-1', n_clicks=0) ]),
    html.Br(),
    html.Div(id='my-output'),

])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    State(component_id='Name-input', component_property='value'),
    State(component_id='password-input', component_property='value'),
    Input(component_id='btn-nclicks-1', component_property='n_clicks')
)
def create_new_user(name, password, n_clicks):

    credentials = CRUD.postgres_credentials(dbname="password_manager", user='postgres', password='toor', host='127.0.0.1', port= '5432')

    message = CRUD.new_user(name, password)
    if message == 'success':
        return 'User {} was created succesfully'.format(name)
    elif message == 'duplicate error':
        return 'User {} already exists'.format(name)
    else: return 'Unknown error, try again'

    clicks = n_clicks

if __name__ == '__main__':
    app.run_server(debug=True)
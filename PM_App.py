import CRUD
from FrontEnd import Front
import dash
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)
app.layout = Front

@app.callback(
    Output(component_id='my-output', component_property='children'),
    State(component_id='Name-input', component_property='value'),
    State(component_id='password-input', component_property='value'),
    Input(component_id='btn-nclicks-1', component_property='n_clicks')
)
def create_new_user(name, password, n_clicks):

    credentials = CRUD.postgres_credentials(dbname="password_manager", user='postgres', password='toor', host='127.0.0.1', port= '5432')

    if n_clicks > 0 and n_clicks <= 10:
        message = CRUD.new_user(name, password)
        if message == 'success':
            return 'User {} was created succesfully'.format(name)
        elif message == 'duplicate error':
            return 'User {} already exists'.format(name)
        else: return 'Unknown error, try again'

    elif n_clicks > 10: return 'Demasiados intentos'

    else: return ''

if __name__ == '__main__':
    app.run_server(debug=True)
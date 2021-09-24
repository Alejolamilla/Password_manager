import json
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H4("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text'),
        html.Button('submit', id='btn-nclicks-1', n_clicks=0),

        dcc.Store(id='intermediate-value')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    State(component_id='my-input', component_property='value'),
    Input(component_id='btn-nclicks-1', component_property='n_clicks')
)
def update_output_div(value, n_clicks):
    return 'Output: {}, {} clicks'.format(value, n_clicks)

@app.callback(
    Output('intermediate-value', 'data'),
    State(component_id='my-input', component_property='value'),
    Input(component_id='btn-nclicks-1', component_property='n_clicks'))

def input_value(value, n_clicks):
    return json.dumps(value, n_clicks)

if __name__ == '__main__':
    app.run_server(debug=True)
import json
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from pathlib import Path

from app import app
from apps import home, register


def read_languages():

    languages = []

    for p in Path('.').glob('Languages/*.json'):
        languages.append({'label':f"{p.name}"[0:-5], 'value':f"{p.name}"[0:-5]})

    return languages
# =======================================================================================

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='language'),
    dcc.Store(id='url_change'),


     html.Div(className='language_drop',
            children=[
                dcc.Dropdown(
                id='language-dropdown',
                optionHeight= 60,
                options=read_languages(),
                value='Español',
                clearable=False)
        ]),

    html.Div(id='page-content')
])

# =======================================================================================

@app.callback(
    Output('language','data'),
    Input('language-dropdown','value'),
)
def select_language(value='Español'):

    text = json.load(open('Languages/'+value+'.json', 'r'))
    return text

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

def display_page(pathname):
    if pathname == '/':
         return home.layout
    elif pathname == '/app2':
         return register.layout
    elif pathname == '/succes':
         return 'succes'
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
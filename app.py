import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import dash_table as dt

import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px


dm = pd.read_csv("https://raw.githubusercontent.com/Nibs007/OxyCare/main/Refined_WBO2.csv")

dm.head()

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import base64




import urllib.request
img = urllib.request.urlretrieve("https://www.homecaremag.com/sites/default/files/O2-oxygen-507182002-_0.jpg", "gender.jpg")


encoded_image = base64.b64encode(open(img[0], 'rb').read())
tab1 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

ll = dm['Area'].values.tolist()
ll= list(set(ll))

body = html.Div([
    dbc.Row([
               dbc.Col(html.Div(dbc.Alert("This is a repository collected from various sources. Contacts have to be verified by user.", color="dark"))),
               
                dbc.Col(dcc.Dropdown(id='x2',
            options=[{'label': i, 'value': i} for i in ll], style={'height': '60px'},
            multi=False,
            placeholder="Select an area"))
              ],className="mt-2"),
        dbc.Row([
            dbc.Col([dbc.Row(html.Div([
    html.Img(src='data:image/jpg;base64,{}'.format(encoded_image.decode()), style={'height': '200px',"margin-left": "20px","margin-right":'10-px'})
])), dbc.Row(html.Div(id="grp1"))])], className="mt-2")])

    
tab1.layout = html.Div([body])

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import base64


tab2 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

import urllib.request
img = urllib.request.urlretrieve("https://raw.githubusercontent.com/mllover5901/dat/main/gender-equality.jpg", "gender.jpg")


encoded_image = base64.b64encode(open(img[0], 'rb').read())







app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True
server = app.server

app.layout = html.Div([
    html.H1('OxyCare'),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Oxygen Near You', value='tab-1-example',style={'color':'white'}),
        dcc.Tab(label='Coming Soon', value='tab-2-example',style={'color':'white'}),
    ],colors={
            "border": "white",
            "primary": "black",
            "background": "black"}),
    html.Div(id='tabs-content-example')
])

@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return tab1.layout
    elif tab == 'tab-2-example':
        return tab2.layout

@app.callback(Output('grp1', 'children'),
                                  [Input('x2', 'value')])
def update_figure1(year):
            global dff 
            if year==None:

                dff=dm
            else: 
                dff = dm[dm['Area']==year]
               
       
            df1 = dff[['Area','State','Contact Number']]
         
            data = df1.to_dict('rows')
            columns =  [{"name": i, "id": i,} for i in (df1.columns)]
            return dt.DataTable(data=data, columns=columns,style_header={ 'whiteSpace': 'normal','height': 'auto','backgroundColor': 'rgb(30, 30, 30)','color':'white','font_size':18},
                style_table={'overflowX': 'auto'},
                style_cell={'backgroundColor': 'white',
                    'color': 'black','font_size':18,'height':100,'fontWeight': 'bold',
                    # all three widths are needed
                    'minWidth': '500px', 'width': '500px', 'maxWidth': '500px',
                    'overflow': 'hidden','border': '1px solid grey',"margin-left": "40px","margin-left": "40px",
                    'textOverflow': 'ellipsis','textAlign': 'center','whiteSpace': 'normal'
       
                })
               

if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)

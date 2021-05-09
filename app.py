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
img = urllib.request.urlretrieve("https://cdn.dribbble.com/users/338126/screenshots/10073371/media/7903e2af9ad301fadfc04d20dfaebdd9.gif", "gender.jpg")


encoded_image = base64.b64encode(open(img[0], 'rb').read())
tab1 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

img2 = urllib.request.urlretrieve("https://img.freepik.com/free-photo/equipment-medical-oxygen-tank-cylinder-regulator-gauge_101276-199.jpg?size=626&ext=jpg", "mask.jpg")
encoded_image2 = base64.b64encode(open(img2[0], 'rb').read())

ll = dm['Area'].values.tolist()
ll= list(set(ll))
dd = dm['District'].values.tolist()
dd= list(set(dd))

body = html.Div([
    dbc.Row([
               dbc.Col(html.Div(dbc.Alert("All information comes from a repository built using various sources. Contacts have to be verified by user.", color="info"))),
               
                dbc.Col(dcc.Dropdown(id='dist',
            options=[{'label': i, 'value': i} for i in dd], style={'height': '60px','font-size':25,'font-family':"Arial"},
            multi=False,
            placeholder="Select a District"))
              ],className="mt-2"),
        dbc.Row([
            dbc.Col([dbc.Row([dbc.Col(html.Div([
    html.Img(src='data:image/jpg;base64,{}'.format(encoded_image.decode()), 
             style={'height': '300px','width': '500px',"margin-left": "20px","margin-right":'10-px'})])), 
            dbc.Col(dcc.Dropdown(id='x2',
            options=[{'label': i, 'value': i} for i in ll], style={'height': '60px','font-size':25},
            multi=False,
            placeholder="Select a Locality"))]), 
                     
                     dbc.Row([dbc.Col(html.Div(id="grp1")), dbc.Col(html.Div([
    html.Img(src='data:image/jpg;base64,{}'.format(encoded_image2.decode()), 
             style={'height': '300px','height': '500px',"margin-left": "20px","margin-right":'10-px'})]))])], className="mt-2")])])

    
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
    html.H1('OxyCares'),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Oxygen Near You', value='tab-1-example',style={'color':'white','font-size':25}),
        dcc.Tab(label='Coming Soon', value='tab-2-example',style={'color':'white','font-size':25}),
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


p = dm.groupby('District')['Area'].unique()
district = pd.DataFrame(p)
district.reset_index(inplace=True)

dik={}
k1 = dict(district.values)
for k,v in k1.items():
    m=[]
    for it in v:
        m.append(it)
    dik[k]=list(set(m))


    

@app.callback(
    Output('x2', 'options'),
    [Input('dist', 'value')]
)
def update_date_dropdown(name):
    return [{'label': i, 'value': i} for i in dik[name]]    
    
    
@app.callback(Output('grp1', 'children'),
                                  [Input('x2', 'value'),Input('dist', 'value')])
def update_figure1(area,dist):
            global dff 
            if area==None and dist==None:

                dff=dm
            elif area==None and dist!=None: 
                dff = dm[dm['District']==dist]
            elif area!=None and dist==None: 
                dff = dm[dm['Area']==area]
            elif area!=None and dist!=None:
                dff = dm[(dm['Area']==area)&(dm['District']==dist)]
               
       
            df1 = dff[['Area','District','State','Contact Number']]
         
            data = df1.to_dict('rows')
            columns =  [{"name": i, "id": i,} for i in (df1.columns)]
            return dt.DataTable(data=data, columns=columns,style_header={ 'whiteSpace': 'normal','height': 'auto','backgroundColor': 'rgb(30, 30, 30)','color':'white','font_size':18},
                style_table={'overflowX': 'auto'},
                style_cell={'backgroundColor': 'white',
                    'color': 'black','font_size':18,'height':100,'fontWeight': 'bold',
                    # all three widths are needed
                    'minWidth': '300px', 'width': '300px', 'maxWidth': '300px',
                    'overflow': 'hidden','border': '1px solid grey',"margin-left": "40px","margin-left": "40px",
                    'textOverflow': 'ellipsis','textAlign': 'center','whiteSpace': 'normal'
       
                })
               
               
               


if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)

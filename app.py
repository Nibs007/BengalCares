# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:44:13 2021

@author: nibed
"""

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
img = urllib.request.urlretrieve("https://image.freepik.com/free-vector/family-wearing-face-masks_52683-38547.jpg", "gender.jpg")


encoded_image = base64.b64encode(open(img[0], 'rb').read())
tab1 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

img2 = urllib.request.urlretrieve("https://thumbs.dreamstime.com/b/portable-oxygen-tank-green-pressurized-cart-ready-to-use-patient-106923200.jpg", "mask.jpg")
encoded_image2 = base64.b64encode(open(img2[0], 'rb').read())

ll = dm['Area'].values.tolist()
ll= list(set(ll))
dd = dm['District'].values.tolist()
dd= list(set(dd))

body = html.Div([
    dbc.Row([
               dbc.Col(html.Div(dbc.Alert("** This app collects publicly available data posted on modern digital channels. Leads shared may not be verified or accurate, or may lead to misleading content.", color="info",style={'height':'90px','font-size':16,'font-style':'italic','fontWeight': 'bold','font-family':"Arial"}))),
               
                dbc.Col(dcc.Dropdown(id='dist',
            options=[{'label': i, 'value': i} for i in dd], style={'height': '60px','font-size':25,'font-family':"Arial","margin-bottom":'0.1px'},
            multi=False,
            placeholder="Select a District"))
              ],className="mt-2"),
        dbc.Row([
            dbc.Col([dbc.Row([dbc.Col(html.Div([
    html.Img(src='data:image/jpg;base64,{}'.format(encoded_image.decode()), 
             style={'height': '380px','width':'450px',"margin-left": "2px","margin-right":'5-px'})])), 
            dbc.Col(dcc.Dropdown(id='x2',
            options=[{'label': i, 'value': i} for i in ll], style={'height': '60px','font-size':25,"margin-bottom":'0.1px'},
            multi=False,
            placeholder="Select a Locality"))]), 
                     
                     dbc.Row([dbc.Col(html.Div(id="grp1")), dbc.Col(html.Div([
    html.Img(src='data:image/jpg;base64,{}'.format(encoded_image2.decode()), 
             style={'height': '300px','height': '500px',"margin-left": "20px","margin-right":'10-px'})]))])], className="mt-2")])])

    
tab1.layout = html.Div([body])


#tab2 details
meal = pd.read_csv("https://raw.githubusercontent.com/Nibs007/OxyCare/main/Meals_Refined.csv")
ard = meal['Area'].values.tolist()
ard = list(set(ard))
tab3 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

img3 = urllib.request.urlretrieve("https://scontent.fdel6-1.fna.fbcdn.net/v/t1.6435-9/184226439_10159312065084679_3015433159858468173_n.jpg?_nc_cat=100&ccb=1-3&_nc_sid=b9115d&_nc_ohc=CPq0tPLaxDUAX-Y_vwg&_nc_ht=scontent.fdel6-1.fna&oh=aae98928061c3af89225864e1d53d4b6&oe=60BF6C0F", "food.jpg")
encoded_image3 = base64.b64encode(open(img3[0], 'rb').read())

img4 = urllib.request.urlretrieve("https://i.pinimg.com/736x/aa/32/f6/aa32f68771f47e6fdde9fe2510bca952.jpg","food1.jpg")
encoded_image4 = base64.b64encode(open(img4[0], 'rb').read())

body3 = html.Div([
    dbc.Row([
               dbc.Col(html.Div(dbc.Alert("All information comes from a repository built using various sources. This website is updated every 12 hours. Contacts have to be verified by user.", color="info",style={'font-size':18,'fontWeight': 'bold'}))),
               
                dbc.Col(dcc.Dropdown(id='ard',
            options=[{'label': i, 'value': i} for i in ard], style={'height': '60px','font-size':25,'font-family':"Arial"},
            multi=False,
            placeholder="Select a Locality"))
              ],className="mt-2"),
        dbc.Row([
            dbc.Col([dbc.Row([dbc.Col(html.Div([
    html.Img(src='data:image/jpg;base64,{}'.format(encoded_image3.decode()), 
             style={'height': '350px','width': '450px',"margin-left": "2px","margin-right":'5-px'})]))]), 
                     
                     dbc.Row([dbc.Col(html.Div(id="tab2")), dbc.Col(html.Div([
    html.Img(src='data:image/jpg;base64,{}'.format(encoded_image4.decode()), 
             style={'height': '300px','height': '500px',"margin-left": "20px","margin-right":'10-px'})]))])], className="mt-2")])])

    
tab3.layout = html.Div([body3])

#tab3 details

tab2 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

img7 = urllib.request.urlretrieve("https://i.pinimg.com/originals/72/a8/0b/72a80b08f5d07a2066fa89830e1ae148.png", "ambulance.jpg")
encoded_image7 = base64.b64encode(open(img7[0], 'rb').read())

img8 = urllib.request.urlretrieve("https://img.freepik.com/free-vector/emergency-car-with-doctor-wear-hazmat-suit-carrying-patient-hospital-concept-cartoon-illustration_201904-432.jpg?size=626&ext=jpg", "ambulance1.jpg")
encoded_image8 = base64.b64encode(open(img8[0], 'rb').read())


amb = pd.read_csv("https://raw.githubusercontent.com/Nibs007/OxyCare/main/RefinedLead_Ambulances.csv")


lamb = amb['Area'].values.tolist()
lamb= list(set(lamb))
damb = amb['District'].values.tolist()
damb= list(set(damb))


body2 = html.Div([
    dbc.Row([
               dbc.Col(html.Div(dbc.Alert("** This app collects publicly available data posted on modern digital channels. Leads shared may not be verified or accurate, or may lead to misleading content.", color="info",style={'height':'90px','font-size':16,'font-style':'italic','fontWeight': 'bold','font-family':"Arial"}))),
               
                dbc.Col(dcc.Dropdown(id='dstr',
            options=[{'label': i, 'value': i} for i in damb], style={'height': '60px','font-size':25,'font-family':"Arial","margin-bottom":'0.1px'},
            multi=False,
            placeholder="Select a District"))
              ],className="mt-2"),
        dbc.Row([
            dbc.Col([dbc.Row([dbc.Col(html.Div([
    html.Img(src='data:image/jpg;base64,{}'.format(encoded_image7.decode()), 
             style={'height': '380px','width':'450px',"margin-left": "2px","margin-right":'5-px'})])), 
            dbc.Col(dcc.Dropdown(id='am',
            options=[{'label': i, 'value': i} for i in lamb], style={'height': '60px','font-size':25,"margin-bottom":'0.1px'},
            multi=False,
            placeholder="Select a Locality"))]), 
                     
                     dbc.Row([dbc.Col(html.Div(id="ambu")), dbc.Col(html.Div([
    html.Img(src='data:image/jpg;base64,{}'.format(encoded_image8.decode()), 
             style={'height': '500px','width': '700px',"margin-left": "20px","margin-right":'10-px'})]))])], className="mt-2")])])




    
tab2.layout = html.Div([body2])



import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import base64



import urllib.request
img = urllib.request.urlretrieve("https://raw.githubusercontent.com/mllover5901/dat/main/gender-equality.jpg", "gender.jpg")


encoded_image = base64.b64encode(open(img[0], 'rb').read())

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-90VMKHLP8Q"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', 'G-90VMKHLP8Q');
        </script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""


app.config['suppress_callback_exceptions'] = True
server = app.server

app.layout = html.Div([
    html.H1('OxyCares'),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Oxygen Near You', value='tab-1-example',style={'color':'white','font-size':25}),
        dcc.Tab(label='Ambulance Near You', value='tab-2-example',style={'color':'white','font-size':25}),
        dcc.Tab(label='Meal Delivery Near You', value='tab-3-example',style={'color':'white','font-size':25}),
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
    elif tab == 'tab-3-example':
        return tab3.layout


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
               
       
            df1 = dff[['Area','District','Contact Number']]
         
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
   

@app.callback(Output('tab2', 'children'),
                                  [Input('ard', 'value')])
def update_figure1(area):
            global dff 
            if area==None:

                dff=meal
           
            elif area!=None:
                dff = meal[(meal['Area']==area)]
               
       
            df1 = dff[['Area','Name of Supplier/CovidHero','Contact Number']]
         
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
                              
               
pam = amb.groupby('District')['Area'].unique()
distr = pd.DataFrame(pam)
distr.reset_index(inplace=True)

dik1={}
k2 = dict(distr.values)
for k,v in k2.items():
    m=[]
    for it in v:
        m.append(it)
    dik1[k]=list(set(m))
    

@app.callback(
    Output('am', 'options'),
    [Input('dstr', 'value')]
)
def update_date_dropdown1(name):
    return [{'label': i, 'value': i} for i in dik1[name]]                 
               

amb = pd.read_csv("https://raw.githubusercontent.com/Nibs007/OxyCare/main/RefinedLead_Ambulances.csv")
  
@app.callback(Output('ambu', 'children'),
                                  [Input('am', 'value'),Input('dstr', 'value')])
def update_figure2(area,dist):
            global dff 
            if area==None and dist==None:

                dff=amb
            elif area==None and dist!=None: 
                dff = amb[amb['District']==dist]
            elif area!=None and dist==None: 
                dff = amb[amb['Area']==area]
            elif area!=None and dist!=None:
                dff = amb[(amb['Area']==area)&(amb['District']==dist)]
               
       
            df1 = dff[['Service Provider','District','Contact Number']]
         
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

import dash
import dash_core_components as dcc
import dash_html_components as html
app=dash.Dash()
from dash.dependencies import Input,Output
import datetime as dt
import pandas_datareader as web
import pandas as pd
from app import app
df=pd.read_csv('tickers.csv')
# graph_data=web.DataReader(value,)

app.layout=html.Div(
[

html.Div([
  html.Div([
     html.H5('Stock Comparison'),
     html.H6('Step towards deciding the Company to invest in',style=dict(color='#7F90AC')),
     ],className="ten columns padded"),
     html.Div([
       html.H1([html.Span('24'),html.Span('×',style=dict(opacity=0.5)),html.Span('7')]),
       html.H6('Stock Update')
       ],className="two columns gs-header gs-accent-header padded",style=dict(float='right')),
       ],className="row gs-header gs-text-header",style={'paddingLeft':10}),
       html.Br([]),
       html.Div([
       html.Div([
        html.Label('Select Company I:',style=dict(color='#7F90AC')),
        dcc.Dropdown(
        id='stock_ticker_input1',
        options=[{'label':s[0],'value':str(s[1])} for s in zip(df.Company,df.Symbol)],
        value='GOOGL',multi=False
)]),
# ,style={'width':'1200','float':'left'}
html.Br([]),
html.Br([]),
html.Div([
 html.Label('Select Company II:',style=dict(color='#7F90AC')),
 dcc.Dropdown(
 id='stock_ticker_input2',
 options=[{'label':s[0],'value':str(s[1])} for s in zip(df.Company,df.Symbol)],
 value='YHOO',multi=False
)],style={'marginBottom':20}),
],style={'padding':20}),
html.Br([]),
html.Div(id='graphing_area',style={'marginTop':150})

])



@app.callback(
Output(component_id='graphing_area',component_property='children'),
[Input(component_id='stock_ticker_input1',component_property='value'),
Input(component_id='stock_ticker_input2',component_property='value')]

)
def update(graph_1,graph_2):
    graph_data1=web.DataReader(graph_1,'morningstar',dt.datetime(2017,5,5),dt.datetime.now())
    graph_data1.reset_index(inplace=True)
    graph_data2=web.DataReader(graph_2,'morningstar',dt.datetime(2017,5,5),dt.datetime.now())
    graph_data2.reset_index(inplace=True)

    graph=dcc.Graph(id='graph',figure={'data':[{'x':graph_data1.Date,'y':graph_data1.Close,'name':graph_1},
                                    {'x':graph_data2.Date,'y':graph_data2.Close,'name':graph_2}
                                    ],
                            'layout':{'title':'Comparison of two companies on the basis of closing Prices:'}
                            })
    return graph













external_css = [ "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                 "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                 "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                 "https://codepen.io/plotly/pen/KmyPZr.css",
                 "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({ "external_url": css })
if __name__ == '__main__':
    app.run_server(debug=True)

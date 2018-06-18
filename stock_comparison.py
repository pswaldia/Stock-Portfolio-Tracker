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

layout=html.Div(
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
       ],className="row gs-header gs-text-header"),
       html.Br([]),
       html.Div([
        html.Label('Select Company I:',style=dict(color='#7F90AC')),
        dcc.Dropdown(
        id='stock-ticker-input1',
        options=[{'label':s[0],'value':str(s[1])} for s in zip(df.Company,df.Symbol)],
        value='GOOGL',multi=False
)],style={'width':'1200','float':'left'}),
html.Br([]),
html.Br([]),
html.Div([
 html.Label('Select Company II:',style=dict(color='#7F90AC')),
 dcc.Dropdown(
 id='stock-ticker-input2',
 options=[{'label':s[0],'value':str(s[1])} for s in zip(df.Company,df.Symbol)],
 value='YHOO',multi=False
)],style={'width':'1200','float':'left','marginBottom':20,'marginLeft':20,'marginRight':20}),

html.Br([]),



# html.Div([
#     dcc.DatePickerRange(
#         id='my-date-picker-range',
#         min_date_allowed=dt(1995, 8, 5),
#         max_date_allowed=dt(2025, 12, 30),
#         initial_visible_month=dt(2017, 8, 5),
#         end_date=dt(2017, 8, 25)
#     ),
#     html.Div(id='output-container-date-picker-range')]),
    html.Div(id='graphing_area',style={'marginTop':150})

],style={'marginLeft':20,'marginRight':20})


# @app.callback(
#     dash.dependencies.Output('output-container-date-picker-range', 'children'),
#     [dash.dependencies.Input('my-date-picker-range', 'start_date'),
#      dash.dependencies.Input('my-date-picker-range', 'end_date')])
# def update_output(start_date, end_date):
#     string_prefix = 'You have selected: '
#     if start_date is not None:
#         start_date = dt.strptime(start_date, '%Y-%m-%d')
#         start_date_string = start_date.strftime('%B %d, %Y')
#         string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
#     if end_date is not None:
#         end_date = dt.strptime(end_date, '%Y-%m-%d')
#         end_date_string = end_date.strftime('%B %d, %Y')
#         string_prefix = string_prefix + 'End Date: ' + end_date_string
#     if len(string_prefix) == len('You have selected: '):
#         return 'Select a date to see it displayed here'
#     else:
#         return string_prefix
@app.callback(
Output(component_id='graphing_area',component_property='children'),
[Input(component_id='stock-ticker-input1',component_property='value')
,Input(component_id='stock-ticker-input2',component_property='value')]
)
def update_graph(graph_1,graph_2):
    graph_data1=web.DataReader(graph_1,'morningstar',dt.datetime(2017,5,5),dt.datetime.now())
    graph_data1.reset_index(inplace=True)
    graph_data2=web.DataReader(graph_2,'morningstar',dt.datetime(2017,5,5),dt.datetime.now())
    graph_data2.reset_index(inplace=True)

    graph=dcc.Graph(id='graph',figure={'data':[{'x':graph_data1.Date,'y':graph_data1.Close,'name':graph_1},
                                    {'x':graph_data2.Date,'y':graph_data2.Close,'name':graph_2}
                                    ],
                            'layout':{'title':'Comparison of two companies on the basis of closing Prices:'},
                            'xaxis':{'title':'Dates'},
                            'yaxis':{'title':'Closing Prices'}
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

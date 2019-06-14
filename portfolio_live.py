import dash
import os

app = dash.Dash()
server = app.server
app.config['suppress_callback_exceptions'] = True

import os
import dash
import requests
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from bs4 import BeautifulSoup

# from app import app

colors = {'text':'#7FDBFF',
          'background': '#1D3461'}

app.layout = html.Div(children = [
    html.Div([
    html.Div([
       html.H2('Live Stock Prices'),
       html.H6('Search for live stock prices of companies',style=dict(color='#7F90AC')),
       ],className="ten columns padded"),
       html.Div([
         html.H1([html.Span('24'),html.Span('×',style=dict(opacity=0.5)),html.Span('7')]),
         html.H6('Stock Update')
         ],className="two columns gs-header gs-accent-header padded",style=dict(float='right')),
         ],className="row gs-header gs-text-header",style={'paddingLeft':20}),

    html.Br(),
    html.Br(),
    html.Br(),


    html.Div(style = {'margin':'10px'},children = [
    html.H6('Enter Ticker Symbol (Ex: MSFT, GOOGL, HPQ)') ,
    dcc.Input(placeholder = 'Enter ticker: for ex: GOOGL,HPQ,MSFT etc',type = 'text',value = 'AAPL',id = 'tickername',className = 'col-lg-3 col-sm-6 form-control ',style = {'width':'30%'}),

    html.P('   '),
    html.Button(type = 'submit',className="btn btn-outline-primary my-2 my-sm-0 ",id='submit-button',n_clicks = 0, children='Search'),

    ]),

    html.Br(),
    html.Br(),

    html.Div(id = 'liveprice',style = {'backgroundColor':'#34345A','paddingTop':12},className = 'w3-card-4 '),

    html.Br(),
    html.Div(className = 'w3-card-4',id = 'table',style={'paddingLeft':10,'paddingRight':10}),


    html.Br(),
    html.Br(),

    html.Div(className = 'w3-card-4',children = [
    html.Header(style = {'backgroundColor':'#34345A','color':'white'},children = [html.H5('Company Info')],className = 'w3-container '),
    html.Div(
    html.Div(children = 'Company Info here..',id = 'info',className = 'w3-card-4',style = {'fontSize':'large','padding':'10px','backgroundColor':'white','fontFamily':'Exo sens-serif'}),className = 'w3-container',style = {'padding':'20px'}
    )
    ])





])

@app.callback(
Output('liveprice','children'),
[Input('submit-button','n_clicks')],
[State('tickername','value')]
)
def update_price(n_clicks,ticker):
    try:
###################################################################################################################     
#                                                                                                                 #
#              WEB SCRAPING USING BEAUTIFUL-SOUP LIBRARY , FROM YAHOO FINANCE WEBSITE                             # 
#                                                                                                                 #
###################################################################################################################
        url = 'https://finance.yahoo.com/quote/' + ticker
        data = requests.get(url)
        soup = BeautifulSoup(data.text,'html.parser')
        result = soup.findAll('span')
        price = result[10].text
        change = result[11].text
        if change[0] == '+':
            return [html.H4(str(price)  ,style = {'display':'inline-block','marginLeft':'10px','color':'white'}),
                    html.H6('  USD',style = {'display':'inline-block','padding':'10px','color':'white'}),
                    html.H6(str(change),style = {'display':'inline-block','padding':'10px','color':'#00ff08'})]
        elif change[0] == '-':
            return [html.H4(str(price)  ,style = {'display':'inline-block','marginLeft':'10px','color':'white'}),
                    html.H6('  USD',style = {'display':'inline-block','padding':'10px','color':'white'}),
                    html.H6(str(change),style = {'display':'inline-block','padding':'10px','color':'#ff0000'})]
    except :
        return 'NaN'

@app.callback(
Output('table','children'),
[Input('submit-button','n_clicks')],
[State('tickername','value')])
def make_table(n_clicks,ticker):
    try:
###################################################################################################################     
#                                                                                                                 #
#              WEB SCRAPING USING BEAUTIFUL-SOUP LIBRARY , FROM YAHOO FINANCE WEBSITE                             # 
#                                                                                                                 #
###################################################################################################################
        url = 'https://finance.yahoo.com/quote/' + ticker

        data = requests.get(url)
        
        soup = BeautifulSoup(data.text,'html.parser')
        
        results=soup.findAll('td',attrs={'class':'C(black) W(51%)'})
        
        results2=soup.findAll('span',attrs={'Trsdu(0.3s)'})
        records=[]
        for i in range(len(results)):
            records.append(results[i].text)
        records2=[]
        for i in range(len(results2)):
            records2.append(results2[i].text)   
        x=dict(zip(records,records2))
        df = pd.DataFrame(x,index=list(range(16))).loc[0,:]
        df.drop(df.index[2:6],inplace = True)
        return(html.Div(html.Table(
        [html.Tr(
            [html.Th(col) for col in df.index ]
            )]  +

        [html.Tr(
            [html.Td(j) for j in df.values]
             )],className = 'w3-card-4',style = {'paddingRight':20,'paddingLeft':20,'backgroundColor':'white','fontSize':18})))

    except:
        return 'Nan'


@app.callback(
Output('info','children'),
[Input('submit-button','n_clicks')],
[State('tickername','value')])
def generateComponyInfo(n_clicks,ticker):
    try:
###################################################################################################################     
#                                                                                                                 #
#              WEB SCRAPING USING BEAUTIFUL-SOUP LIBRARY , FROM YAHOO FINANCE WEBSITE                             # 
#                                                                                                                 #
###################################################################################################################

        url = 'https://finance.yahoo.com/quote/'+ticker+'/profile'
        data = requests.get(url)
        soup = BeautifulSoup(data.text,'html.parser')

        data2 = soup.find('p',attrs = {'class':'Mt(15px) Lh(1.6)'})

        return data2.text
    except:
        return 'Sorry!!..Company info not found'



app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.css.append_css({'external_url':'https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css'})
app.css.append_css({'external_url': 'https://www.w3schools.com/w3css/4/w3.css'})

if __name__ == '__main__':
    app.run_server(debug=True)




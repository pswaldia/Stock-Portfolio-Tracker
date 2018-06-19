import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os
from app import app
import home_page,historical,stock_comparison,portfolio_live
app.layout=html.Div([
dcc.Location(id='url',refresh=False),
 html.Div(className='w3-bar w3-black w3-large sticky-top ',children=[
  dcc.Link('Home ',className='w3-bar-item w3-button w3-mobile w3-padding-16',href='/home_page',style={'width':'10%'}),
  dcc.Link('Historical ',className='w3-bar-item w3-button w3-mobile w3-padding-16',href='/historical',style={'width':'10%'}),
  dcc.Link('Comparison ',className='w3-bar-item w3-button w3-mobile w3-padding-16',href='/stock_comparison',style={'width':'10%'}),
  dcc.Link('Live ',className='w3-bar-item w3-button w3-mobile w3-padding-16',href='/portfolio_live',style={'width':'12%'})]),


html.Div(id='page-content')
],style={'marginBottom':40})


# 'marginLeft':20,'marginRight':20,'width':1400,
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/home_page':
         return home_page.layout
    elif pathname == '/portfolio_live':
         return portfolio_live.layout
    elif pathname == '/historical':
         return historical.layout
    elif pathname == '/stock_comparison':
         return stock_comparison.layout
    else:
        return '404'
external_css = ['https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css',
                'https://www.w3schools.com/w3css/4/w3.css',
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/plotly/pen/KmyPZr.css",]




for css in external_css:
    app.css.append_css({"external_url": css})




if __name__ == '__main__':
    app.run_server(debug=True)


import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from app import app
# app=dash.Dash()
layout=html.Div(
[

html.Div([
  html.Div([
     html.H5('Portfolio Management'),
     html.H6('Searching and Comparing Stocks Made Easy',style=dict(color='#7F90AC')),
     ],className="ten columns padded"),
     html.Div([
       html.H1([html.Span('24'),html.Span('×',style=dict(opacity=0.5)),html.Span('7')]),
       html.H6('Stock Update')
       ],className="two columns gs-header gs-accent-header padded",style=dict(float='right')),
       ],className="row gs-header gs-text-header",style={'paddingLeft':20}),


       html.Br([]),
      #Row 2
       html.Div([
       html.H5(dcc.Link('Historical Stock Prices',href='/historical'),className="gs-header gs-text-header padded",style={'paddingLeft':10}),
       html.Strong('Historical Overview',style={'paddingLeft':10,'fontSize':16}),
       html.P(),
       html.P("Historical Data permits you to know whether stocks are worth buying at the price they are being offered or not.It provides you the confidence needed to become a true long-term buy-and-hold investor.",className="blue-text",style={'fontSize': 14,'paddingLeft':10}),
       html.P("Looking at historical data can provide some insight into how a security or market has reacted to a variety of different variables, from regular economic cycles to sudden world events. Investors looking to interpret historical returns should keep one caveat in mind: you can't assume that the future will be like the past. The older the historical return data is, the more likely it is to be less useful when predicting future returns.",
       className="blue-text",style={'fontSize': 14,'paddingLeft':10}),
       html.H5("Live Stock Data",style={'paddingLeft':10},className="gs-header gs-text-header padded"),
       html.Strong('Why Live Stock Data is useful?',style={'paddingLeft':10,'fontSize':16}),

       html.P(),
       html.P("The stock market can be a volatile place; some actively traded stocks can fluctuate dramatically in price from minute to minute, or even from second to second. For investors looking to buy or sell a stock, knowing the current price is imperative. In a rapidly rising or falling market, also known as a fast market, even real-time quotes can have a hard time keeping up. In that market scenario, a quote that’s delayed 15 or 20 minutes is virtually useless, as a stock could have moved by a significant percentage in that time frame.",className="blue-text",style={'fontSize':14,'paddingLeft':10}),
       html.P("If you’re a rapid trader, it can be critical to get real-time quotes instead of delayed quotes so you know exactly where the market is when you’re investing.This Website Makes this Task quite easy for you.",style={'fontSize': 14,'paddingLeft':10},className="blue-text"),
       html.H5(dcc.Link('Compare The Stocks',href='/compare'),className="gs-header gs-text-header padded",style={'paddingLeft':10}),
       html.Strong('On What Basis Comparison is to be made?',style={'fontSize':16,'paddingLeft':10}),
       html.P(),
       html.P("Warren Buffett,arguably the greatest investor of all time, avoids high-growth companies that fall outside his circle of competence that is, the scope of his knowledge and understanding. There's no reason you shouldn't do the same.And among the companies you are familiar with, it's usually best to compare companies that operate in the same industry. You may be familiar with both Dunkin' Brands and Apple (NASDAQ:AAPL), but it's tough to compare a restaurant chain to the world's largest technology company.",className='blue-text',style={'fontSize':14,'paddingLeft':10}),
       html.P("A company's absolute stock price tells you almost nothing about how expensive the company is. It's far more useful to look at three different valuation tools: price-to-earnings ratio, or P/E; price-to-free cash flow ratio, or P/FCF; and price-to-earnings-growth ratio, or PEG. Each of these metrics is important to consider. Both P/E and P/FCF are backward-looking measurements, while the PEG ratio attempts to value a company based on how much it is expected to grow in the future.Our Site gives you all the information required to compare the Stocks of two companies, and thereby helps in deciding the company in which the investment should be made.",className='blue-text',style={'fontSize':14,'paddingLeft':10}),
       html.H5('Things one must know before investing in stock market',style={'paddingLeft':10},className="gs-header gs-text-header padded"),
       html.Strong("1. Never jump blindly into stock markets",style={'fontSize':16,'paddingLeft':10}),
       html.P(),
       html.P('Many a times it happens that while talking to your friends and colleagues, the discussion heads towards the stock market, and also how the stock market helps investors make big money. You might never have invested in the market, but after hearing about all those things you also decide to buy some stocks. However, if you entered the market just to remain in the mainstream fashion, you have landed in for the wrong reason. You should invest in the stock market after getting the basic knowledge about it and in accordance with your financial goals.',className='blue-text',style={'fontSize':14,'paddingLeft':10}),
       html.Strong("2. Stock market is not a money-making machine",style={'fontSize':16,'paddingLeft':10}),
       html.P(),
       html.P('You must have heard the story about many investors who made their fortune through the market. Many believe that the stock market is like a money-making machine, which can turn them into millionaires over a period of time. Well, it is true that a lot of investors have made profits through the stock market. But it was only possible because they’ve good market knowledge, made some really smart choices by adopting carefully thought of strategies, and are also much disciplined in their approach. Many people forget that a lot of people have lost their entire wealth, while some have been forced to sell their personal assets to cover the loss in the market.',className='blue-text',style={'fontSize':14,'paddingLeft':10}),
       html.Strong('3. Educate yourself, handle basics first',style={'fontSize':16,'paddingLeft':10}),
       html.P('Before making your first investment, take the time to learn the basics about the stock market and the individual securities composing the market. There is an old adage: It is not a stock market, but a market of stocks. Your focus will be upon individual securities which you are investing in and the relationship with the broader economy and the factors that drive your stock.',className='blue-text',style={'fontSize':14,'paddingLeft':10,'marginBottom':50})
]),
 html.Div([
html.Div([
 html.A(
 html.I(className="fa fa-facebook fa-lg white-text mr-md-5 mr-3 fa-2x"),href="http://www.facebook.com"),
 # html.A('text',href="http://www.google.com"),

 html.A(
 html.I(className="fa fa-twitter fa-lg white-text mr-md-5 mr-3 fa-2x"),href="https://twitter.com/ps_waldia"
 ),
 html.A(
 html.I(className="fa fa-google-plus fa-lg white-text mr-md-5 mr-3 fa-2x"),href="https://plus.google.com/100109978314734187475"),
 html.A(
 html.I(className="fa fa-linkedin fa-lg white-text mr-md-5 mr-3 fa-2x"),href="https://www.linkedin.com/in/pradeep-singh-9b0bb114a"),
 html.A(
 html.I(className="fa fa-instagram fa-lg white-text mr-md-5 mr-3 fa-2x"),href="http://www.instagram.com"),
 html.A(
 html.I(className="fa fa-pinterest fa-lg white-text mr-md-5 mr-3 fa-2x"),href="http://www.pinterest.com")
],style={'marginTop':20,'marginBottom':20})








 ],className="row gs-header gs-text-header",style={'paddingLeft':'40%','backgroundColor':'#243147'})








])











external_css = [ "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
        "//fonts.googleapis.com/css?family=Raleway:400,300,600",
        "https://codepen.io/plotly/pen/KmyPZr.css",
        "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
        "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"]

for css in external_css:
    app.css.append_css({ "external_url": css })
if __name__ == '__main__':
    app.run_server(debug=True)

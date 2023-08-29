# Import packages
import pandas as pd
import plotly
import pickle
import warnings
from dash import Dash, dash_table, callback, dcc, html, Input,Output,State
import numpy as np

warnings.filterwarnings("ignore")


# Incorporate data
# df = pd.read_csv("source_code/Cars.csv")

owner_type =["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner"]
# Initialize the app
app = Dash(__name__)

#load model
loaded_model = pickle.load(open('/root/code/carprice_predict.model', 'rb'))


app.layout = html.Div([
    html.H1("Car Price Prediction for Chaky's Company"),
    html.Div([

        html.H3(children='Instruction' , style={'textAlign':'left'}),
        html.H4("In order to predict car price, you need to choose maximum power, mileage, and  year."),
        html.H4("If you don't know maximum power and mileage, you can use provided defualt values to help you to predict car price."),
        html.H3(children='max power (bhp)' , style={'textAlign':'left'}),
         dcc.Input( id='max_power', type='number', value=82.4 , min=0), 

         
        html.H3(children='mileage (kmpl)', style={'textAlign':'left'}, ),
         dcc.Input( id='mileage', type='number', value=19.392 , min=0), 

         html.H3(children='year', style={'textAlign':'left'}),
         dcc.Input( id='year',type='number',value=2023, min=1983, placeholder ="select year" ),

         html.H3(""),
         html.Button(n_clicks=0, id='submit', children='predict'),
         html.H4(id="y"),

  
        
    ])
])

@callback(
    Output("y" ,"children"),
    Input('submit', 'n_clicks'),
    State('max_power', 'value'),
    State('mileage', 'value'),
    State('year', 'value')
    
)


def update_price( n_clicks,max_power, mileage, year):
    if int(n_clicks) >= 1:
        if max_power == None:
            max_power == 82.4
        if mileage == None:
            mileage == 19.392
        if year == None:
            year == 2015

        sample = np.array([[max_power, mileage,year]])
        price = int(np.exp(loaded_model.predict(sample)))
        car_price = price
        return f'The predicted car price is = {price} Baht'

# Run the app

if __name__ == '__main__':
    app.run(debug=True)

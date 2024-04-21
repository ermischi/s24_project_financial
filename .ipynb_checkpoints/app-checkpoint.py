import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import statsmodels.api as sm
import pandas as pd
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

housing = pd.read_csv("realtor-data.zip.csv", delimiter=',').dropna()
MI = housing[housing["state"] == "Michigan"]
EL = MI[MI["city"] == "East Lansing"]
EL_sale = EL[EL["status"] == "for_sale"]

X = EL_sale.drop(["brokered_by", "status", "price", "street", "city", "state", "zip_code", "prev_sold_date"], axis=1)
Y = EL_sale["price"]
X = sm.add_constant(X)
multi_model = sm.OLS(Y, X).fit()

app.layout = dbc.Container([
    html.H1("House Price Estimator", className="display-4"),
    dbc.Row([
        dbc.Col([
            html.Label("Bedrooms"),
            dcc.Input(id="bedrooms", type="number", value=3, className="form-control"),
        ]),
        dbc.Col([
            html.Label("Bathrooms"),
            dcc.Input(id="bathrooms", type="number", value=2, className="form-control"),
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            html.Label("Square Feet"),
            dcc.Input(id="sqft", type="number", value=2000, className="form-control"),
        ]),
        dbc.Col([
            html.Label("Lot Size"),
            dcc.Input(id="lot_size", type="number", value=5000, className="form-control"),
        ]),
    ]),
    html.Button("Submit", id="submit-val", n_clicks=0, className="btn btn-primary mt-3"),
    html.Div(id='output-container-button', className="mt-3")
])

@app.callback(
    Output('output-container-button', 'children'),
    [Input('submit-val', 'n_clicks')],
    [Input('bedrooms', 'value'),
     Input('bathrooms', 'value'),
     Input('sqft', 'value'),
     Input('lot_size', 'value')]
)
def update_output(n_clicks, bedrooms, bathrooms, sqft, lot_size):
    if n_clicks > 0:
        # Prepare input for prediction
        user_input = sm.add_constant([[1, bedrooms, bathrooms, sqft, lot_size]])  # Adding constant term
        # Make prediction
        prediction = multi_model.predict(user_input)[0] - 2000000
        while prediction < 0:
            prediction += 200000
        return f"The estimated price of the house is ${prediction:,.2f}"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

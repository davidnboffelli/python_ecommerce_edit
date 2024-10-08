import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .dbaccess import getCategoriesandOrders

# Sample data

category, orders = getCategoriesandOrders()
df = pd.DataFrame(
    {
        "category": category,
        "orders": orders,
    }
)


def categories_Orders(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash3/")
    dash_app.layout = html.Div(
            children=[
            html.H1(
            "Trending Categories",
            style={
                'textAlign': 'center',
                'font-family': 'Arial',
                'font-size': '24px',
                'margin-bottom': '10px',  # Add some spacing below the title
            }
            ),
            html.Div(
            "Categories with Highest Orders",
            style={
                'textAlign': 'center',
                'font-family': 'Arial',
                'font-size': '16px',
                'margin-bottom': '20px',  # Add more spacing below this text
            }
            ),
            dcc.Graph(
            id="example-graph",
            style={'width': '100%'},
            config={'displayModeBar': False}  # Hide the plotly toolbar
            ),
            dcc.Interval(
                id='interval-component',
                interval=1*60000,  # in milliseconds (update every minute)
                n_intervals=0
            )
            ],
    )

    @dash_app.callback(
        Output("example-graph", "figure"),
        [Input("interval-component", "n_intervals")]
    )
    def update_graph(selected_id):
        # Load the data within the callback function
        category, orders = getCategoriesandOrders()
        df = pd.DataFrame(
            {
                "category": category,
                "orders": orders,
            }
        )
        # Create a bar chart using Plotly Express
        fig = px.bar(df, x="orders", y="category", title="Categories with Orders")
          
        fig.update_layout(

        font=dict(family="Arial", size=18),
        legend=dict(font=dict(family="Arial", size=15)),
   
    )
        return fig

    return dash_app

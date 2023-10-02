from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Sleep data
df = pd.read_csv('./sleep_dataset.csv')

# Initialize the app -> team name is ada
ada = Dash(__name__)

ada.layout = html.Div
([
    html.Div(children= "Sleep Analysis"),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
    dcc.Graph(figure=px.histogram(df, x='Occupation'))
])

if __name__ == '__main__':
    ada.run(debug=True)

from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Sleep data
df = pd.read_csv('./sleep_dataset.csv')

# Initialize the app -> team name is ada
app = Dash(__name__)

app.layout = html.Div([
    html.Div(children= "Sleep Analysis"),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x=df.Occupation.sort_values(), title='Sleep Occupation'))
    dcc.Graph(figure=px.histogram(df, x=test.index, y=test.values, 
             labels={"x": "Occupation", "y": "Avg Sleep Duration"}, title='Avg Sleep Duration'))
])

if __name__ == '__main__':
    app.run(debug=True)

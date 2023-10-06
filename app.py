from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Sleep data
df = pd.read_csv('./sleep_dataset.csv')
df.sort_values('Occupation', inplace=True)

# Initialize the app -> team name is ada
app = Dash(__name__)

app.layout = html.Div([
    html.Div(className='row', children='My First App with Data, Graph, and Controls',
             style={'textAlign': 'center', 'color': 'Lightblue', 'fontSize': 25, 'font-weight': 'bold'}),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x=df['Occupation'], title='Sleep Occupation')),
    dcc.Graph(figure=px.histogram(df, x=df['Occupation'].unique(), y=df.groupby('Occupation')['Sleep Duration'].mean().round(2), labels={"x": "Occupation", "y": "Avg Sleep Duration"}, title='Avg Sleep Duration'))
])

if __name__ == '__main__':
    app.run(debug=True)

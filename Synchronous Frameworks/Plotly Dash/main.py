from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

fig = px.line(x=[98,1,54], y=[0,90,10], title="My Line Chart")

app.layout = html.Div([
    html.H1("My Dashboard"),
    dcc.Graph(figure=fig)
])

app.run(debug=True)
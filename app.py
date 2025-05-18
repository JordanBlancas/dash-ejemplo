import dash
from dash import html, dcc, Input, Output
import numpy as np
import plotly.graph_objs as go

app = dash.Dash(__name__)

x = np.linspace(0, 10, 100)

app.layout = html.Div([
    html.H1("Gráfico con slider interactivo (Dash)", style={"textAlign": "center"}),
    dcc.Slider(id='amp-slider', min=1, max=5, step=0.5, value=2),
    dcc.Graph(id='plot')
])

@app.callback(
    Output('plot', 'figure'),
    Input('amp-slider', 'value')
)
def update_plot(amplitud):
    y = amplitud * np.sin(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'Amplitud: {amplitud}'))
    fig.update_layout(template='plotly_white')
    return fig

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)



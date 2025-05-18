import dash
from dash import html, dcc, Input, Output
import numpy as np
import plotly.graph_objs as go

app = dash.Dash(__name__)

x = np.linspace(0, 10, 100)

app.layout = html.Div([
    html.H1("Gráfico con slider interactivo (Dash)", style={"textAlign": "center"}),

    html.Div([
        dcc.Slider(id='amp-slider', min=1, max=5, step=0.5, value=2),
        html.Div(id="slider-output", style={"textAlign": "center", "marginTop": "10px"})
    ], style={"padding": "0 30px"}),

    dcc.Loading(
        id="loading-graph",
        type="default",  # Puedes cambiarlo a "circle", "dot", etc.
        children=[
            dcc.Graph(id='plot')
        ],
        fullscreen=False
    )
])

@app.callback(
    Output('plot', 'figure'),
    Output('slider-output', 'children'),
    Input('amp-slider', 'value')
)
def update_plot(amplitud):
    y = amplitud * np.sin(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'Amplitud: {amplitud}'))
    fig.update_layout(template='plotly_white')
    return fig, f"Amplitud seleccionada: {amplitud}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=False)

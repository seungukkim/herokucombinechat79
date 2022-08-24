import dash
from dash import html 
from dash import html, dcc
from .layout import html_layout
import pandas as pd 
import plotly.express as px

# 가상 데이터 프레임
# SQL 코드
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# plotly 시각화 코드
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Dash 코드 생성
def add_dash(server):

    # Dash 클래스 호출 + Flask 두개의 프레임워크 연동 지점
    app = dash.Dash(
        server=server,
        url_base_pathname="/dashapp1/",
        suppress_callback_exceptions=True
    )
    
    # 
    app.index_string = html_layout

    # Dash 코드 (Flask 코드 (X))
    app.layout = html.Div([
        html.H2('Hello World'),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA'
        ),
        html.Div(id='display-value'), 
            dcc.Graph(
            id='example-graph',
            figure=fig)
    ])

    @app.callback(dash.dependencies.Output('display-value', 'children'),
                  [dash.dependencies.Input('dropdown', 'value')])
    
    def display_value(value):
        return 'You have selected "{}"'.format(value)
        
    return server
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard", style={'textAlign': 'center'}),
    
    # Dropdown for Launch Site
    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'All Sites', 'value': 'ALL'}] + 
                [{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()],
        value='ALL',
        placeholder="Select a Launch Site",
        searchable=True
    ),
    
    html.Br(),
    
    # Pie chart for success rate
    dcc.Graph(id='success-pie-chart'),
    
    html.Br(),
    
    # Range slider for Payload Mass
    dcc.RangeSlider(
        id='payload-slider',
        min=0, max=10000, step=1000,
        marks={i: str(i) for i in range(0, 10001, 2500)},
        value=[spacex_df['Payload Mass (kg)'].min(), spacex_df['Payload Mass (kg)'].max()]
    ),
    
    html.Br(),
    
    # Scatter chart for Payload vs Success
    dcc.Graph(id='success-payload-scatter-chart'),
])

# Callback for pie chart
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        fig = px.pie(spacex_df, names='Launch Site', values='class', title="Total Success Launches by Site")
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        fig = px.pie(filtered_df, names='class', title=f"Total Success Launches for site {selected_site}")
    return fig

# Callback for scatter plot
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'), Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
                            (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
    
    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version',
                     title="Payload vs. Outcome by Booster Version")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

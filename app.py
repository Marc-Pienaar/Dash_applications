import dash
import dash_bootstrap_components as dbc
#external_stylesheets=[dbc.themes.SUPERHERO]
external_stylesheets=[dbc.themes.GRID, 'box_style.css']
app = dash.Dash(__name__,external_stylesheets = external_stylesheets, suppress_callback_exceptions=True)
if __name__ == '__main__':
    app.run_server(debug=True)
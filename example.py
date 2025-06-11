import dash
from dash import html

# Import the disable devtool plugin
from dash_disable_devtool_plugin import setup_disable_devtool_plugin

# Enable the disable devtool plugin for the current app
setup_disable_devtool_plugin()

app = dash.Dash(__name__)

app.layout = html.Div("Test App.", style={"padding": 50})

if __name__ == "__main__":
    app.run(debug=True)

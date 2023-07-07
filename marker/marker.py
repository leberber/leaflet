import dash_leaflet as dl
from dash_extensions.javascript import Namespace
from dash import Dash, html

point =  Namespace("myNamespace", "point")

geojson = dl.GeoJSON(
    url="assets/us_cities.geojson", 
    zoomToBounds=True,
    options=dict(pointToLayer=point("pointToLayer")),
    hideout=dict(colorProp='county_name')
)

app = Dash()
app.layout = html.Div([
    dl.Map([dl.TileLayer(), geojson]),
], style={'width': '100%', 'height': '100vh'})

if __name__ == '__main__':
    app.run_server(debug = True)
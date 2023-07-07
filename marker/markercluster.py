import dash_leaflet as dl
from dash_extensions.javascript import assign, Namespace
from dash import Dash, html, no_update, Input,Output
import json

cluster = Namespace("myNamespace", "cluster")

point =  Namespace("myNamespace", "point")

classes = ['King', 'Spokane', 'Benton', 'Kitsap' ,'Pierce' ,'Thurston','Snohomish' ]
colorscale = ['#ff66ff','#ff0000','#003366','#996633',  '#ccff33', '#33ccff','#99ff66']

my_colors={'King': '#ff66ff',
 'Spokane': '#ff0000',
 'Benton': '#003366',
 'Kitsap': '#996633',
 'Pierce': '#ccff33',
 'Thurston': '#33ccff',
 'Snohomish': '#99ff66'}


geojson = dl.GeoJSON(url="assets/us_cities.geojson", id="geojson", 
                     zoomToBounds=True,  # when true, zooms to bounds when data changes
                     cluster=True,  # when true, data are clustered
                 
                     zoomToBoundsOnClick=True,  # when true, zooms to bounds of feature (e.g. cluster) on click
               
                     options=dict(pointToLayer=point("pointToLayer")),
                     clusterToLayer=cluster("pointToLayer"),
                     superClusterOptions=dict(radius=150),   # adjust cluster size
                     hideout=dict(colorProp='county_name', circleOptions=dict(fillOpacity=1, stroke=False, radius=5),
                                  colorscale=list(my_colors.values()), classes=list(my_colors.keys()))
                                  )
# Create the app.
app = Dash( prevent_initial_callbacks=True)
app.layout = html.Div([
    dl.Map([dl.TileLayer(), geojson]),
     html.Div(id = 'locationlayeroutput'),  
], style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block", "position": "relative"})


@app.callback(Output("locationlayeroutput", "children"), Input("geojson", "click_feature"))
def log(feature):
  
    if feature is None:
        raise PreventUpdate

    else:
        if feature['properties']['cluster'] == True:
            return no_update
        else:
           return f" leadbichtrobnm: {json.dumps(feature['properties']['county_name'])}"
if __name__ == '__main__':
    app.run_server(debug = True)

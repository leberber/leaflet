window.myNamespace = Object.assign({}, window.myNamespace, {

    point: {
        pointToLayer: function(feature, latlng, context) {

            const {
                classes,
                colorscale,
                circleOptions,
                colorProp
            } = context.props.hideout;

            const value = feature.properties[colorProp]; // get value the determines the color
            // console.log(classes)

            // for (let i = 0; i < classes.length; ++i) {

            //     if (value == classes[i]) {

            //         circleOptions.fillColor = colorscale[i]; // set the fill color according to the class
            //     }
            // }

            const icon = L.divIcon({
                html: `<div">${value}</div>`,
                className: "map-marker-style",
                // iconSize: L.point(40, 40),
                color: 'red'
            });
            return L.marker(latlng, {
                icon: icon
            })
            //  L.circleMarker(latlng); // sender a simple circle marker.
        },

    },

    cluster: {
        pointToLayer: function(feature, latlng, index, context) {

            const {

                classes,
                colorscale,
                colorProp
            } = context.props.hideout;
            // const csc = chroma.scale(colorscale).domain([min, max]);
            // Set color based on mean value of leaves.
            const leaves = index.getLeaves(feature.properties.cluster_id);


            const counts = {};
            // for (const i of leaves) 
            for (let i = 0; i < leaves.length; ++i) {
                // console.log(leaves[i].properties[colorProp])

                counts[leaves[i].properties[colorProp]] = counts[leaves[i].properties[colorProp]] ? counts[leaves[i].properties[colorProp]] + 1 : 1;
                // console.log(leaves)
            }

            var color_index = classes.indexOf(Object.keys(counts)[0])

            var myclor = colorscale[color_index];
            console.log(myclor);

            // console.log();



            // Render a circle with the number of leaves written in the center.
            const icon = L.divIcon.scatter({
                html: '<div style="background-color:white;"><span>' + feature.properties.point_count_abbreviated + '</span></div>',
                className: "marker-cluster",
                iconSize: L.point(40, 40),
                color: myclor
            });
            return L.marker(latlng, {
                icon: icon
            })
        }
    },
});


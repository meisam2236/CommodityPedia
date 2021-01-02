
const map = new ol.Map({
    view: new ol.View({
        center: [5720461.899924258, 4244805.015866431],
        zoom: 5,
        minZoom: 3,
        
    }),
    
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    target: 'js-map'
})


map.on('click', function(){
    if (typeof layer !== 'undefined') {
    map.removeLayer(layer);
    }
    
})


map.on('click', function (e) {
    layer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [
                new ol.Feature({
                    geometry: new ol.geom.Point([e.coordinate[0], e.coordinate[1]])
                })
            ]
        })
    });
    map.addLayer(layer);
    document.getElementById("address_lat").value = e.coordinate[0];
    document.getElementById("address_lon").value = e.coordinate[1];
})

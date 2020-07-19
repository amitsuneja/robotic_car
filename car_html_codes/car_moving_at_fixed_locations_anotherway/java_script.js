var ContactUs = function () {
    return {
        //main function to initiate the module
        init: function () {
            var neighborhoods = [{
                lat: 41.02688344,
                lng: 28.97104517,
                icon: 'http://maps.google.com/mapfiles/ms/micons/blue.png',
                content: "a"
            }, {
                lat: 41.07992535,
                lng: 29.02025431,
                icon: 'http://maps.google.com/mapfiles/ms/micons/green.png',
                content: "b"
            }, {
                lat: 41.059097,
                lng: 28.983857,
                icon: 'http://maps.google.com/mapfiles/ms/micons/yellow.png',
                content: "c"
            }, {
                lat: 41.08476948,
                lng: 28.97748649,
                icon: 'http://maps.google.com/mapfiles/ms/micons/orange.png',
                content: "d"
            }, {
                lat: 41.05635465,
                lng: 28.95114452,
                icon: 'http://maps.google.com/mapfiles/ms/micons/red.png',
                content: "e"
            }];

            var markers = [];
            var map;
            var infowindow = new google.maps.InfoWindow();
            map = new google.maps.Map(document.getElementById("map"), {
                zoom: 12,
                center: {
                    lat: 41.052244,
                    lng: 28.985637
                }
            });

            function addMarkerWithTimeout(position, timeout, icon, content) {
                window.setTimeout(function () {
                    var marker = new google.maps.Marker({
                        position: position,
                        map: map,
                        animation: google.maps.Animation.DROP,
                        icon: icon
                    });
                    google.maps.event.addListener(marker,'click', function(e) {
                        infowindow.setContent(content);
                        infowindow.open(map,marker);
                    });
                    markers.push(marker);
                }, timeout);
            }

            for (var i = 0; i < neighborhoods.length; i++) {
                addMarkerWithTimeout(neighborhoods[i], i * 300, neighborhoods[i].icon, neighborhoods[i].content);
            }
        }
    };
}();
ContactUs.init();

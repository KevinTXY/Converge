for (var i = 0; i < total; i++) {
              console.log(items[i]);
              $.getJSON("https://maps.googleapis.com/maps/api/geocode/json?address="
                + encodeURIComponent(items[i])
                + "&key=AIzaSyASFadX1MvoP2EccKogmGEyyza8UGcwHbU",
                function(data) {
                    console.log(data);
                    sum_lat += data.results[0].geometry.location.lat;
                    sum_long += data.results[0].geometry.location.lng;
                    points.push([data.results[0].geometry.location.lat, data.results[0].geometry.location.lng]);
                    console.log("LAT:" + data.results[0].geometry.location.lng);
                    console.log("LNG:" + data.results[0].geometry.location.lat);
                    calls_remaining--;
                    if (calls_remaining <= 0) {
                      var avg_lat = sum_lat / total;
                      var avg_long = sum_long / total;
                      console.log(avg_lat, avg_long);

                      map = new google.maps.Map($("#map").get(0), {
                            center: {lat: avg_lat, lng: avg_long},
                            disableDefaultUI: true,
                            mapTypeId: google.maps.MapTypeId.ROADMAP,
                            maxZoom: 14,
                            panControl: true,
                            zoom: 13,
                            zoomControl: true
                        });
                        console.log(data.results)

                        var i = 0
                        points.forEach(function(element){
                          console.log("THIS ELEMENT:  " + element);
                          var loc = new google.maps.LatLng(element[0], element[1]);
                          var mark = new google.maps.Marker({
                            position: loc,
                            label: i.toString(),
                            icon: image
                          });
                          i++;
                          mark.setMap(map);
                        });

                      var location = new google.maps.LatLng(avg_lat, avg_long);
                      var label = "P";
                      var marker = new google.maps.Marker({
                        position: location,
                        label: label,
                      });
                      marker.setMap(map);

                      var service = new google.maps.places.PlacesService(map);
                                  service.nearbySearch({
                                    location:position,
                                    radius: 5000,
                                    type: ['restaurant']
                                  }, callback);
                      function callback(results, status) {
                        if (status === google.maps.places.PlacesServiceStatus.OK){
                          for (var i=0; i < results.length; i++) {
                            createMarker(results[i]);
                          }
                        }
                      }
                      function createMarker(place) {
                        var placeLoc = place.geometry.location;
                        var marker = new google.maps.Marker({
                          map:map,
                          position: place.geometry.location
                        });
                        google.maps.event.addListener(marker, 'click', function() {
                          infowindow.setContent(place.name);
                          infowindow.open(map, this);
                        });
                      }
                    }
                  });
            }
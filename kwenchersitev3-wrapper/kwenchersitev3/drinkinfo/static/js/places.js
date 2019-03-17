// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 43.6615, lng: -70.2556},
    zoom: 13
  });

  var infowindow = new google.maps.InfoWindow();
  var service = new google.maps.places.PlacesService(map);
  // var place1 = ['ChIJNSMk8RKcskwROiqUHcHqawM', 'ChIJ5fqyTRCcskwRohgCeF8hFHM',];

for( i = 0; i < place1.length; i++ ) {
  // console.log(place1[i][0]);
  service.getDetails({
    placeId: place1[i][0]

  }, function(place, status) {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
      var marker = new google.maps.Marker({
        map: map,
        position: place.geometry.location
      });
      google.maps.event.addListener(marker, 'click', function() {
        infowindow.setContent('<div><strong>' + place.name + '</strong><br>' +
          place.formatted_address + '</div>');
        infowindow.open(map, this);
      });
    }
  });
}
}

<script>
	let USAcoordinates = [-98.5795,39.8283]//lat then long
	let parkCoordinates = '{{ parks.coordinates }}'
	console.log(parkCoordinates)

	mapboxgl.accessToken = "{{ mapbox_access_token }}"

	map = new mapboxgl.Map({
	container: 'map', // container id
	style: 'mapbox://styles/mapbox/streets-v11', // style URL
	center: USAcoordinates, // starting position [lng, lat]
	zoom: 3.5 // starting zoom
	});

	var marker = new mapboxgl.Marker()
		.setLngLat(parkCoordinates)
	.addTo(map);

</script>
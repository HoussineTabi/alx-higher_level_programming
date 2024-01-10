#!/usr/bin/node
/*
the script number seven
*/
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (resp) {
	$('#character').text(resp.name);
});

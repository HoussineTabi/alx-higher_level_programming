$.get('https://swapi.co/api/films/?format=json', function(resp) {
	for (let i = 0; i < resp.length; i++) {
		$('#list_movies').append(`<li>$(resp.results[i].title}</li`);
	}
});

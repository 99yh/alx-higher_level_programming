// fetch data from a url and display it
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', null, (data) => {
  parent = $('UL#list_movies');
  data.results?.map(film => parent.append(`<li>${film.title}</li>`));
})

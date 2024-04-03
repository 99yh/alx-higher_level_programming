// fetch data from a url and display it
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', null, (data) => {
  $('DIV#character').text=(data.name);
})

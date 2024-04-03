// fetch data from a url and display it
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', null, (data) => {
  $('DIV#hello').text(data.hello);
})

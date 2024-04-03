// add a list item on click
$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  const lang = $('INPUT#language_code');
  const hello = $('DIV#hello');
  const sayHello = () => {
    $.get(url + lang.val(), (data) => hello.html(data.hello));
  }

  $('INPUT#btn_translate').on('click', sayHello );
})

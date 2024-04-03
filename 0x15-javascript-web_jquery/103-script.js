// add a list item on click
$(function () {
  const lang = $('INPUT#language_code');
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  const hello = $('DIV#hello');
  const sayHello = () => {
    $.get(url + lang.val(), (data) => hello.html(data.hello));
  }

  $('INPUT#btn_translate').on('click', sayHello );
  lang.on('keyup', e => {if (e.key === 'Enter') sayHello();});
})

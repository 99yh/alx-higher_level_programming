// change the color of <header> when <div id='red_header'> clicked
$('div#toggle_header').on('click', () => $('header').toggleClass(['green', 'red'], 1));

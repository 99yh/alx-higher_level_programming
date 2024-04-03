// add a list item on click
$(function () {
  const my_list = $('UL.my_list');
  $('DIV#add_item').on('click', () => my_list.append('<li>Item</li>'));
  $('DIV#remove_item').on('click', () => my_list.find('li').last().remove());
  $('DIV#clear_list').on('click', () => my_list.find('*').remove());
})

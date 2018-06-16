$("#load1").click(function() {
  $("#if").attr('src', 'http://onsemi.com');
});
$("#load2").click(function() {
  $("#if").contents().find('html').html("hello");
});
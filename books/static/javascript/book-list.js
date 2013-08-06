$(function() {
  $('.review-link').on('click', function() {
    var $this = $(this);
    console.log('Will start a review for book ' + $this.attr('data-book_id'));

    $('#book_id').val($this.attr('data-book_id'));
    $('form').removeClass('invisible');
    return false;
  });

  $('form button:submit').on('click', function() {
    $.post('/review', { book_id: $('#book_id').val(), text: $('#text').val() }, function (data) {
      console.log(data);
      $('#book_id').val('');
      $('form').addClass('invisible');

      
    });
    return false;
  });

});

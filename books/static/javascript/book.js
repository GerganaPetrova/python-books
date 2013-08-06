function quote(book_id) {
  var quote = window.getSelection().toString();
  if (!quote) return;
  console.log("Saving quote: " + quote);
  jQuery.post('/quote', { 'book_id': book_id, 'quote_text': quote }, function(data) {
    console.log(data)
  });
};

function translate_selection() {
  var text = window.getSelection().toString();
  if(!text) return;
  console.log("Translate" + text);
  jQuery.get('/translate', { 'text': text }, function(data) {
    alert(text + ': ' + data);
  });
}

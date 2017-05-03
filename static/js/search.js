function search(searchTerm) {
  event.preventDefault();
  console.log(searchTerm);

  var client = new $.es.Client({
    hosts: '192.168.99.100:32771'
  });

  client.search({
  index: 'avacat',
  type: 'resource_index',
  body: {
    query: {
      match: {
        name: searchTerm
      }
    }
  }
}).then(function (resp) {
    var hits = resp.hits.hits;
    var searchResults = document.getElementById('searchResults');
    $('#searchResults').empty();
    hits.forEach(function(hit) {
        $("#searchTemplate").tmpl(hit).appendTo("#searchResults");

    });

}, function (err) {
    console.trace(err.message);
});


};

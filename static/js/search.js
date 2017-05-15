// function search(searchTerm) {
//   event.preventDefault();
//   console.log(searchTerm);
//
//   var client = new $.es.Client({
//     hosts: '192.168.99.100:32771'
//   });
//
//   client.search({
//   index: 'avacat',
//   type: 'resource_index',
//   body: {
//     query: {
//       match: {
//         name: searchTerm
//       }
//     }
//   }
// }).then(function (resp) {
//     var hits = resp.hits.hits;
//     var searchResults = document.getElementById('searchResults');
//     $('#searchResults').empty();
//     hits.forEach(function(hit) {
//         $("#searchTemplate").tmpl(hit).appendTo("#searchResults");
//
//     });
//
// }, function (err) {
//     console.trace(err.message);
// });
// };
function loadSearchTerm(searchTerm)
{
  $('#search-term').val(searchTerm);
  search(searchTerm);
}

function search(searchTerm) {
  if (searchTerm == "")
    return;
  console.log(searchTerm);
  event.preventDefault();
  var data = {
    searchTerm : searchTerm
  };
  $.ajax({
      url : "search/", // the endpoint
      type : "POST", // http method
      data : JSON.stringify(data),
      success : function(json) {
        var searchResults = document.getElementById('searchResults');
        $('#searchResults').empty();
        json.forEach(function(hit) {
            $("#searchTemplate").tmpl(hit).appendTo("#searchResults");

        });
      },
      error : function(xhr,errmsg,err) {
          $('#answer-error-' + id).show();
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  });
};

function like(id) {
  event.preventDefault();
  $.ajax({
      url : "like/" + id,
      type : "GET",
      success : function(json) {
        var likes = Number($("#" + "likes-" +  id).text());
        $("#likes-" + id).text(likes+1);
      },
      error : function(xhr,errmsg,err) {
          $('#answer-error-' + id).show();
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  });
};

function dislike(id) {
  console.log("disliked called: " + id);
  event.preventDefault();
  $.ajax({
      url : "dislike/" + id,
      type : "GET",
      success : function(json) {
        console.log("success");
        var dislikes = Number($("#" + "dislikes-" +  id).text());
        $("#dislikes-" + id).text(dislikes+1);
      },
      error : function(xhr,errmsg,err) {
          $('#answer-error-' + id).show();
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  });
};

$(function() {
    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});

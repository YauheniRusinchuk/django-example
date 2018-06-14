$(function(){
  $('.about').css({'background-color': '#78baf0', 'border-radius': '5px'});

  $(".form_post").on('submit', (e) => {
    e.preventDefault();
    create_comment();
  })

});


// function search(){
//   $.ajax({
//     type: "POST",
//     url: '/posts/search/',
//     data: {
//           'search_text': $('.search_form').val(),
//           csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         },
//     success: function(){
//       $('.search_form').val('')
//       }
//   })
// }



function create_comment() {
  $.ajax({
    url: $(this).attr('action'),
    type: 'POST',
    data: {
      comment: $('.text_comment_form').val(),
      csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
    },
    success : function() {
      console.log('ENDDD')
      $('.text_comment_form').val("");
    }
  })
}

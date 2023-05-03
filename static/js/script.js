function like_post(post_id) {
    $.ajax({
        url: '/post/' + post_id + '/like/',
        type: 'POST',
        dataType: 'json',
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function (response) {
            var like_btn = $('#like_btn');
            like_btn.toggleClass('active', response.liked);
            like_btn.find('span').text(response.count);
        },
        error: function (xhr, status, error) {
            console.log(xhr.responseText);
        }
    });
}

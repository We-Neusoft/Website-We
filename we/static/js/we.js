'use strict';

$(document).ready(function () {
    $.getJSON('/common/get_user.we', function (data) {
        $('#me').html(data.username + '，你好！');
        $('.dropdown').css('visibility', 'visible');
    });
});

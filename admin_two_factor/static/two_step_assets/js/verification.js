$(document).ready(function () {
    $('#CheckTwoStep').click(function (e) {
        e.preventDefault();
        var btn = $(this);
        var url = btn.data('url');
        var param = [];
        param['url'] = url;
        param['form'] = $('form#login-form');
        AjaxCheckTwoStepVerification(param);
    });
});

function AjaxCheckTwoStepVerification(param) {
    $.ajax({
        url: param['url'],
        type: 'POST',
        async: true,
        data: param['form'].serialize(),
        success: function (data) {
            if (!data.is_valid) {
                param['form'].submit();
            } else {
                $.confirm({
                    title: 'Two Step Verification',
                    content: '' +
                        '<div class="form-group">' +
                        '<label>Verification Code: </label>' +
                        '<input name="code" type="text" placeholder="Code" class="code form-control" required />' +
                        '</div>',
                    type: 'orange',
                    buttons: {
                        verify: function () {
                            var code = this.$content.find('.code').val();
                            if (!code) {
                                $.alert('provide a valid code');
                                return false;
                            }

                            $.ajax({
                                url: param['url'],
                                type: 'PUT',
                                async: true,
                                data: param['form'].serialize() + "&code=" + code,
                                beforeSend: function (xhr) {
                                    xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                                },
                                success: function (data) {
                                    if (!data.is_valid) {
                                        $.alert(data.message);
                                        return false;
                                    }

                                    param['form'].submit();
                                },
                                error: function () {
                                    $.alert('Error occurred');
                                    return false;
                                }
                            });
                        },
                        cancel: function () {}
                    },
                });
            }
        },
        error: function () {
            showMessage('warning', 'Error occurred');
        }
    });
}
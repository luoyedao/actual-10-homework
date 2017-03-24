/**
 * Created by admin on 2016/8/26.
 */
function logind() {
    $.ajax({
    url: "/login",
    type: "post",
    data:{
        username: $("#username").val(),
        password: $("#password").val()
    },
    datatype: "html",
    beforeSend:function () {$("#tip").html("waiting...");},
    success: function (data) {
        //alert(data)
        //$("#tip").html(decodeURI(data));
           location.href = "/userlist"
    },
    complete: function (XMLHttpRequest, textStatus) {
        //alert(XMLHttpRequest.responseText);
        //alert(textStatus);
    },
    error: function () {
        $("#tip").css("color", "red");
        $("#tip").html("Account or password error");
    }
})
}
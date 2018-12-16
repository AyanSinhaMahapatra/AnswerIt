$(document).ready(function(){
        $.getJSON("http://127.0.0.1:8000/user/detail/"+id, function(data){


                var html = $(`
                        <div class = "row" >Name : ${data.username}</div>
                        <div class = "row" >Email ID : ${data.email}</div>
                        <div class = "row" >Karma : ${data.karma}</div>
                        <div class = "row" >Active : ${data.is_active}</div>
                        <div class = "row" >Moderator : ${data.is_moderator}</div>

            `   );
                html.appendTo("#body");
         });
});
var post_link = "http://127.0.0.1:8000/question/"
var user_link = "http://127.0.0.1:8000/user/"
var JSON;
var temp = 0;

    $.getJSON('http://127.0.0.1:8000/question/list', function(data){

            JSON = data;

            $.each(JSON, function(index, element){

            temp++;

            var html = $(`
               <div class='row' id = "list">
                    <div class="span2">
                        <a id = "id"href=${post_link+element.id}><h2>Q${temp}.  ${element.title}</h2></a>
                    </div>
                    <div class="span2" >${element.body}</div>
                    <div class="col-sm-12" id="user">
                        <a>User : <a id = "owner" href=${user_link+element.owner}>${element.owner}</a></a>
                    </div>

                </div>
            `);

            html.appendTo("#ques");
            });
    });


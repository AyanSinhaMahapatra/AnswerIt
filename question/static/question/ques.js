var link_ques_edit = "http://127.0.0.1:8000/question/edit/"+a;
var link_ques_delete = "http://127.0.0.1:8000/question/delete/"+a;
var link_ques_like = "http://127.0.0.1:8000/question/like/"+a;
var link_ques_dislike = "http://127.0.0.1:8000/question/dislike/"+a;

var link_ans_add = "http://127.0.0.1:8000/question/answer/add/";
var link_ans_edit = "http://127.0.0.1:8000/question/answer/edit/";
var link_ans_delete = "http://127.0.0.1:8000/question/answer/delete/";
var link_ans_like = "http://127.0.0.1:8000/question/answer/like/";
var link_ans_dislike = "http://127.0.0.1:8000/question/answer/dislike/";

var link_com_add = "http://127.0.0.1:8000/question/answer/comment/add/";
var link_com_edit = "http://127.0.0.1:8000/question/answer/comment/edit/";
var link_com_delete = "http://127.0.0.1:8000/question/answer/comment/delete/";
var link_com_like = "http://127.0.0.1:8000/question/answer/comment/like/";
var link_com_dislike = "http://127.0.0.1:8000/question/answer/comment/dislike/";

var icon_like = "https://png.icons8.com/ios/50/000000/good-quality.png"
var icon_dislike = "https://png.icons8.com/ios/50/000000/poor-quality.png"
var icon_edit = "https://png.icons8.com/ios/50/000000/pencil-filled.png";
var icon_delete = "https://png.icons8.com/ios/50/000000/trash.png"
var icon_add = "https://png.icons8.com/ios/50/000000/plus.png"

$(document).ready(function(){
        $.getJSON("http://127.0.0.1:8000/question/detail/"+a, function(data){


                var html = $(`

                    <div class='row' id = "ques">
                        <div class="col-sm-12" id ="title" >
                            <a style = "text-decoration:none;"><h2>Q)  ${data.title}</h2></a>
                        </div>
                        <div class="col-sm-12" id = "ques_body">${data.body}</div>
                        <div class="col-sm-6" id = "ques_body">
                            <a>User :
                                <a href='http://127.0.0.1:8000/user/${data.owner}'style = "text-decoration:none;">${data.owner}</a>
                            </a>
                        </div>
                        <div class="col-sm-3" id = "ques_icon">
                                <a href = ${link_ques_like} >
                                        <img src=${icon_like}></img>
                                </a> ${data.like_count}
                                <a href = ${link_ques_dislike} >
                                        <img src=${icon_dislike}></img>
                                </a> ${data.dislike_count}
                        </div>
                        <div class="col-sm-3"id = "ques_icon">
                                <a href = ${link_ques_edit} >
                                        <img src=${icon_edit}></img>
                                </a>
                                <a href="javascript:delete_question()">
                                        <img src=${icon_delete}></img>
                                </a>
                         </div>
                    </div>
                `);

                html.appendTo("#body");

         });

        $.getJSON("http://127.0.0.1:8000/question/answer/detail/"+a, function(data){

               $.each(data, function(index, element1){
                     var html1 = $(`

                        <div class = "row" id = "list1">
                            <div class="row" >
                                    <div class="col-sm-1">
                                       <a>User :
                                           <a style = "text-decoration:none;" href='http://127.0.0.1:8000/user/${element1.owner}'>
                                                ${element1.owner}
                                           </a>
                                       </a>
                                    </div>
                                    <div class="col-sm-9" >${element1.body}</div>
                                    <div class="col-sm-2" id = "ans_like_dislike">
                                            <a href = ${link_ans_like}${element1.id}>
                                            <img src=${icon_like}></img>
                                            </a>
                                                ${element1.like_count}
                                            <a href = ${link_ans_dislike}${element1.id} >
                                                 <img src=${icon_dislike}></img>
                                            </a> ${element1.dislike_count}
                                     </div>
                            </div>
                         <div class="row" id ="ans_add"><h6>Comments :
                                <a href=${link_com_add}${element1.id} style = "text-decoration:none;">
                                    <img src=${icon_add}></img>
                                </a></h6>
                         </div>
                            <div class="col-sm-4"  id = "delete_edit">
                                    <a href = ${link_ans_edit}${element1.id}>
                                            <img src=${icon_edit}></img>
                                    </a>
                                    <a href = ${link_ans_delete}${element1.id} >
                                            <img src=${icon_delete} href="link"></img>
                                    </a>
                            </div>
                         </div>
                    `);

                     html1.appendTo("#answers");
                     var temp = element1.id;

                    $.getJSON("http://127.0.0.1:8000/question/answer/comment/detail/"+temp, function(data){
                         $.each(data, function(index, element2){

                            var html2 = $(`

                            <div class = "container" id = "list2">
                                <div class = "row" id = "comment">
                                       <div class="col-sm-2">
                                              <a>User : <a href='http://127.0.0.1:8000/user/${element2.owner}'>${element2.owner}</a></a>
                                        </div>
                                        <div class="col-sm-6" >${element2.body}</div>
                                        <div class="col-sm-2" id="com_icon">
                                                <a href = ${link_com_like}${element2.id} >
                                                    <img src=${icon_like}></img>
                                                </a>
                                                ${element2.like_count}
                                                <a href = ${link_com_dislike}${element2.id}>
                                                <img src=${icon_dislike}></img>
                                                </a>
                                                ${element2.dislike_count}
                                        </div>
                                        <div class="col-sm-2" id="com_icon">
                                                <a href = ${link_com_edit}${element2.id} >
                                                <img src=${icon_edit}></img>
                                                </a>
                                                <a href = ${link_com_delete}${element2.id} >
                                                <img src=${icon_delete} href="link"></img>
                                                </a>
                                        </div>
                                </div>
                            </div>
                            `);

                            html2.appendTo("#list1");

                        });
                    });

               });
        });
    });

function delete_question(){
    $.ajax({
            url: link_ques_delete,
            type: "DELETE",
            dataType: 'json',
            crossDomain: true,
            success: function(data){
                alert("done!");
            },
            error: function(data){
                console.log("1");
            }
    });
}
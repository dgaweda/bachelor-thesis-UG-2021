$(document).ready(function(){

    $("#single_comment").on({
        keypress : function(){
            singleCommentButtonService()
        },
        blur : function(){
            singleCommentButtonService()
        }
    });
});

function singleCommentButtonService(button, comment)
{
    var single_comment_button = "single_comment_submit";
    var comment = document.getElementById("single_comment").value;
    if (comment.length > 0)
    {
        document.getElementById(single_comment_button).setAttribute("type", "submit");
        document.getElementById(single_comment_button).setAttribute("class", "launch");
    }
    else
    {
        document.getElementById(single_comment_button).setAttribute("type", "text");
        document.getElementById(single_comment_button).setAttribute("class", "inactive_button");
    }
}
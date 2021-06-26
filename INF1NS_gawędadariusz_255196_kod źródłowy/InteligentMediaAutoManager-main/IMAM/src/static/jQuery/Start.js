// Show Password
$(document).ready(function(){
 $(".checkbox").change(function(){
  if($(this).is(':checked')){
   $("#pass").attr("type","text");
  }
  else
  {
   $("#pass").attr("type","password");
  }
 });
});

// References a
$(document).ready(function(){
    $("a").on({
        mouseenter : function(){
            $(this).css({backgroundColor: "gray", color: "black"});
        },
        mouseleave : function(){
            $(this).css({backgroundColor: "black", color: "white"});
        },
        click : function(){
            $(this).css({"color": "lightgreen", "background-color": "gray"});
        }
    });
})

// SUBMIT BUTTON
$(document).ready(function(){
    $(".launch").on({
        mouseenter : function(){
            $(this).css({backgroundColor: "gray", color: "black"});
        },
        mouseleave : function(){
            $(this).css({backgroundColor: "black", color: "white"});
        },
        click : function(){
            $(this).css({"color": "green", "background-color": "gray"});
        }
    });
})

// COMMENT BUTTON
$(document).ready(function(){
    $("#comment_checkbox").click(function(){
        showComments();
    });
})

function showComments(){
    var checked = document.getElementById("comment_checkbox").checked;
    var title = document.getElementById("comment_title");
    var comment_label = document.getElementById("comment_label");
    var option_label = document.getElementById("option_label");
    var list = document.getElementById("options");
    if (checked == true){
        title.style.color = "green";
        comment_label.style.display = "block";
        option_label.style.display = "block";
        list.style.display = "block";
    }
    else{
        title.style.color = "gray";
        comment_label.style.display = "none";
        option_label.style.display = "none";
         list.style.display = "none";
    }
}

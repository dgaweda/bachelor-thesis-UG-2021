var possible_tag_chars = "0123456789abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ_ ";
var possible_location_chars = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ ";
var probability_error = "Probability must be a number between 1 and 100";
var tag_error = "Tags can only contain letters, numbers, and underscores";
var amount_error = "Amount must be a number greater than 0";
var delay_error = "Delay must be a number greater than 0";
var location_error = "Locations can only contain letters";
var green = "rgb(0, 128, 0)";
var red = "rgb(255, 0, 0)";

$(document).ready(function(){
    $("#like_photo_probability_field").focusout(function(){

            probabilityError("like_photo_probability_field", "like_photo_probability_error_field", probability_error);
            checkBoth("like_photo_probability_field", "like_photo_probability_error_field", "like_photo_tags_field", "like_photo_tags_error_field");
    });

    $("#like_video_probability_field").focusout(function(){
            probabilityError("like_video_probability_field", "like_video_probability_error_field", probability_error);
            checkBoth("like_video_probability_field", "like_video_probability_error_field", "like_video_tags_field", "like_video_tags_error_field");
    });

    $("#like_photo_tags_field").focusout(function(){
        wrongCharsDetector("like_photo_tags_field", "like_photo_tags_error_field", tag_error, possible_tag_chars);
        checkBoth("like_photo_tags_field", "like_photo_tags_error_field", "like_photo_probability_field", "like_photo_probability_error_field");
    });

    $("#like_video_tags_field").focusout(function(){
        wrongCharsDetector("like_video_tags_field", "like_video_tags_error_field", tag_error, possible_tag_chars);
        checkBoth("like_video_tags_field", "like_video_tags_error_field", "like_video_probability_field", "like_video_probability_error_field");
    });

    $("#follow_by_tags_field").focusout(function(){
        wrongCharsDetector("follow_by_tags_field", "follow_by_tags_error_field", tag_error, possible_tag_chars);
    });

    $("#locations_field").focusout(function(){
        wrongCharsDetector("locations_field", "locations_error_field", location_error, possible_location_chars);
    });

    $("#unfollow_non_followers_amount_field").focusout(function(){
        valueError("unfollow_non_followers_amount_field", "unfollow_non_followers_amount_error_field", amount_error)
        checkBoth("unfollow_non_followers_amount_field", "unfollow_non_followers_amount_error_field", "unfollow_non_followers_time_field", "unfollow_non_followers_time_error_field");
    });

    $("#unfollow_non_followers_time_field").focusout(function(){
        valueError("unfollow_non_followers_time_field", "unfollow_non_followers_time_error_field", delay_error);
        checkBoth("unfollow_non_followers_time_field", "unfollow_non_followers_time_error_field", "unfollow_non_followers_amount_field", "unfollow_non_followers_amount_error_field");
    });

    $("#options").focusout(function(){
        checkNull("options");
    })

    $("input").focusout(function(){
        checkForm(red);
    });

    $("select").focusout(function(){
        checkForm(red);
    });
})

function checkForm(red)
{
    var elements = document.getElementsByTagName("input");
    var menu = document.getElementById("options");

    for(var i = 0; i < elements.length;i++)
    {
        var style = getComputedStyle(elements[i]);
        var border = style.borderLeftColor;

        if (border == red)
        {
            document.getElementById("launch").style.display="none";
            break
        }
        else if (border == green)
        {
            document.getElementById("launch").style.display="block";
        }
    }
}

function valueError(input, error, error_description)
{
    var value = document.getElementById(input).value;
    if(value > 0)
    {
        setCorrect(input, error);
    }
    else if(value < 0)
    {
        setError(input, error, error_description);
    }
    else if(value.length == 0)
    {
        setNeutral(input, error);
    }
    else
    {
        setError(input, error, error_description);
    }
}

function wrongCharsDetector(input, error, error_description, possible_chars)
{
    var value = document.getElementById(input).value;
    var wrong = true;
    if(value.length != 0)
    {
        for(var i = 0; i < value.length; i ++)
        {
            for(var j = 0; j < possible_chars.length; j ++)
            {
                if(value[i] == possible_chars[j])
                {
                    wrong = false;
                }
            }
            if (wrong == true)
            {
                setError(input, error, error_description);
                return;
            }
        }
        setCorrect(input, error);
    }
    else
    {
        setNeutral(input, error);
    }
}

function probabilityError(input, error, error_description){
    var value = document.getElementById(input).value;
    if(value.length == 0)
    {
        setNeutral(input, error)
    }
    else if(!isNaN(value) && value > 0 && value <= 100)
    {
        setCorrect(input, error);
    }
    else
    {
        setError(input, error, error_description);
    }
}

function setError(input, error, error_description)
{
    document.getElementById(input).style.borderColor = "red";
    document.getElementById(input).style.borderWidth = "1px";
    document.getElementById(error).style.color = "red";
    document.getElementById(error).innerHTML = error_description;
}

function setCorrect(input, error)
{
    document.getElementById(input).style.borderColor = "green";
    document.getElementById(input).style.borderWidth = "1px";
    document.getElementById(error).innerHTML = "";
}

function setNeutral(input, error)
{
    document.getElementById(input).style.borderColor = "lightgray";
    document.getElementById(input).style.borderWidth = "0.5px";
    document.getElementById(error).innerHTML = "";
}

function checkBoth(input, input_error, other, other_error)
{
    var value = document.getElementById(input).value;
    var other_value = document.getElementById(other).value;
    var input_element = document.getElementById(input);
    var other_element = document.getElementById(other);

    var other_style = getComputedStyle(other_element);
    var input_style = getComputedStyle(input_element);

    if(other_value.length == 0 && input_style.borderLeftColor == green)
    {
        setError(other, other_error, "This field can't be empty");
    }
    else if(other_style.borderLeftColor == green && value.length == 0)
    {
        setError(input, input_error, "This field can't be empty");
    }
}

function checkNull(){
    var menu = document.getElementById("options");
    if(menu.value != 'first')
    {
        menu.style.borderWidth = "1px";
        menu.style.borderColor = "green";
    }
    else
    {
        menu.style.borderWidth = "0.5px";
        menu.style.borderColor = "lightgray";
    }
}



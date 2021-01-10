function toggle_reply(element){
    var form_container = $(element).siblings(".form-container")[0];
    if ($(form_container).css("visibility") != "hidden"){
        $(form_container).css("visibility", "hidden");
        $(form_container).css("display", "none");
    } else{
        $(".form-container").each(function(i, element){
            $(element).css("visibility", "hidden");
            $(element).css("display", "none");
        })
        $(form_container).css("display", "flex");
        $(form_container).css("visibility", "visible");
        
    }
}
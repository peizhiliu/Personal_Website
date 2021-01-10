function toggle_filter(){
    var tags_list = $($(".tags-list")[0]);
    if (tags_list.css("display") == "none"){
        tags_list.css("display", "block");
    } else{
        tags_list.css("display", "none");
    }
}

$(document).ready(function(){
    $(".post-container").each(function(p, post){
        var image = $(post).find("img");
        if (!image.length){
            $(post).find(".post-text").css({
                'width':'100%',
                'margin':'0%',
            })
        }
    })
})

$(document).on("click", function(event){
    var filter = $(".filter-button")[0];
    if (filter !== event.target){
        var tags_list = $($(".tags-list")[0]);
        tags_list.css("display", "none");
    }
})
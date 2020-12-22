// handle project-linking
var slides = []
$(document).ready(function(){
    //$(window).on("resize", resize_image_container())
    $(".project-container").each(function(i){
        slides.push(1);
        show_slides(i + 1, 1);
        
    }) 
})

/*$(document).ready(function(){
    var total_loaded = 0;
    var total_images = $("img").length;
    
    $("img").each(function(){
        $(this).on("load", loaded());
    })

    function loaded(){
        total_loaded++;
        if (total_loaded == total_images){
            resize_image_container();
        }
    }
})*/

function resize_image_container(){
    $(".project-container").each(function(){
        var max_height = 0;
        $(this).find(".slides").each(function(){
            var height = $(this).height();
            if (height > max_height){
                max_height = height;
            }
        })

        var info_container_height = $(this).find(".info-container").height();
        $(this).find(".image-container").height(info_container_height + max_height);
        
    })
}

function increment_counter(current, inc, max){
    current += inc;
    return ((current % max) +  max) % max;
}

function show_slides(p, i){
    var project_id_name = "#project-" + p.toString();
    var imageslides_class_name = '.slides'
    var image_class_name = ".image-" + i.toString();

    $(project_id_name + " " + imageslides_class_name).each(function(){
        $(this).css("display", "none");
    })

    $(project_id_name + ' ' + image_class_name).css('display','block');
}

function advance_slide(p, inc){
    var len = $("#project-" + p.toString() + " " + ".slides").length;
    var current = slides[p - 1];
    var next = increment_counter(current - 1, inc, len) + 1;
    show_slides(p, next);

    slides[p-1] = next;
}
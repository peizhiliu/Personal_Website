// handle greeting screen resize
$(document).ready(function(){
    function adjust_greeting(){
        let h = $(window).height() - $("#nav-bar-container").height();
        $("#pic_and_greeting_container").css("height", h); 
    }
    
    adjust_greeting();
    $(window).resize(function(){
        adjust_greeting();
    })
})

// handle skills progress info
$(document).ready(function(){
    var animated = false;

    function reset_progress(){
        var circles = $(".skill-circle");
    
        for (var i = 0; i < circles.length; i++){
            var circle = circles[i];
            var radius = circle.r.baseVal.value;
            var circumference = radius * 2 * Math.PI;
            var percentage = parseInt(circle.getAttribute("percentage"), 10);

            circle.style.strokeDasharray = `${circumference} ${circumference}`;
            circle.style.strokeDashoffset = `${circumference}`;
        }
    }

    function render_progress(){
        var circles = $(".skill-circle");
    
        for (var i = 0; i < circles.length; i++){
            var circle = circles[i];
            var radius = circle.r.baseVal.value;
            var circumference = radius * 2 * Math.PI;
            var percentage = parseInt(circle.getAttribute("percentage"), 10);
            
            circle.style.strokeDasharray = `${circumference} ${circumference}`;
            circle.animate({
                strokeDashoffset: [`${circumference}`, `${circumference * (1 - (percentage / 100))}`],
                }, 1000);
            
            
            circle.style.strokeDashoffset = `${circumference * (1 - (percentage / 100))}`;
        }
    }

    function element_in_viewport(element){
        var view_port_top = $(document).scrollTop();
        var view_port_bot = $(window).height() + view_port_top;

        var element_top = element.offset().top;
        var element_bottom = element.height() + element_top;

        if (element_top > view_port_top && element_bottom < view_port_bot){
            animated = true;
            return true;
        }
        return false;
    }

    function animation_test(){
        var element = $("#skills_content_container");
        if (animated){
            return;
        }

        if (element_in_viewport(element)){
            render_progress();
        }
    }

    reset_progress();
    $(window).scroll(function(){
        animation_test();
    })
})


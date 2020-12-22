// navbar dynamics
window.onscroll = function() {nav_scroll()};
var nav_animation_complete = false;

function nav_scroll(){
    var nbcontain = document.getElementById('nav-bar-container');
    var nb = document.getElementById('nav-bar');
    var content = document.getElementById('content');
    var threshold = nbcontain.offsetTop + nbcontain.offsetHeight;

    if (window.pageYOffset > threshold){
        nbcontain.classList.add('nav-bar-container-sticky');
        nb.classList.add('nav-bar-sticky');
        content.style.paddingTop = String(threshold) + 'px';
    }else{
        nbcontain.classList.remove('nav-bar-container-sticky');
        nb.classList.remove('nav-bar-sticky');
        content.style.paddingTop = '0';
    }
}

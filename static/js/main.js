// Get fully year on the footer
$("#year").text(new Date().getFullYear());


// Back to the top button
$('.btt-link').click(function(e) {
    window.scrollTo(0,0)
})


//Navbar background and color changes on scrooll
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(document).scrollTop() > 25) {
        $(".btt-button").addClass("back-top-active");
        $(".topnav").addClass("topnav-active");
      } else {
        $(".btt-button").removeClass("back-top-active");
        $(".topnav").removeClass("topnav-active");
      }
    });
  });
          
  

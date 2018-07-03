// very dirty copy paste 

$(document).ready(function ($) {

  $("#fractal").addClass("active");
  $('#fxd .logo').hide();

});    


/* Main scroll event listener */
$(window).scroll(function(){
  var scrollY = $(document).scrollTop();
  var windowY = $(window).height();
//  var docY = $(document).height();
  var insight0Y = $('#home').height() + $('#prologue').height() + $('#contents').height();
  var insight1Y = insight0Y + $('#insight1').height();
  var insight2Y = insight1Y + $('#insight2').height();
  var insight3Y = insight2Y + $('#insight3').height();
  var insight4Y = insight3Y + $('#insight4').height();
  var insight5Y = insight4Y + $('#insight5').height()+200;
  var insight6Y = insight5Y + $('#insight6').height()+400;
  // var insight7Y = insight6Y + $('#insight7').height()+500;
  // var insight8Y = insight7Y + $('#insight8').height();

  // console.log(scrollY, windowY, insight0Y, insight1Y, insight2Y, insight3Y, insight4Y, insight5Y, insight6Y);

  switch (scrollY) { // home screen vs. subpages 
  case checkRange(scrollY, -1000, windowY):
    $('#fxd .logo').hide();
    $('#prologue .logo').show();
    break;
  default: 
    $('#fxd a.logo').show();
    $('#prologue a.logo').hide();
    break;
  }      
  
  switch (scrollY) { // pagination + sections // add div height detection
  case checkRange(scrollY, insight6Y+1, insight6Y*2): 
    updatePagination(8);
    break; 
  case checkRange(scrollY, insight5Y+1, insight6Y): 
    updatePagination(7);
    break; 
  case checkRange(scrollY, insight4Y+1, insight5Y): 
    updatePagination(6);
    break; 
  case checkRange(scrollY, insight3Y+1, insight4Y): 
    updatePagination(5);
    break; 
  case checkRange(scrollY, insight2Y+1, insight3Y): 
    updatePagination(4);
    break; 
  case checkRange(scrollY, insight1Y+1, insight2Y): 
    updatePagination(3);
    break; 
  case checkRange(scrollY, insight0Y+1, insight1Y):
    updatePagination(2);
    break; 
  case checkRange(scrollY, windowY*0.25, insight0Y):
    $('#fractal').removeClass('active');
    updatePagination(1);
    break; 
    
  default:
    updatePagination(1);
    $('#fractal').addClass('active');
    break;
  }  
});

/* Scroll to anchors */
$('a[href*="#"]')
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function(event) {
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname
    ) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        event.preventDefault();
        $('html, body').animate({scrollTop: target.offset().top}, 800);
      }
    }
  });

function checkRange(x, n, m) {
  if (x >= n && x <= m) { return x; }
  else { return !x; }
}

function updatePagination(x) {
  $('.pagination li a').removeClass('selected');
  $('.pagination li:nth-child('+x+') a').addClass('selected');
}




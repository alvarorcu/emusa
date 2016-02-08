$(document).ready(function() {
  //change the integers below to match the height of your upper dive, which I called
  //banner.  Just add a 1 to the last number.  console.log($(window).scrollTop())
  //to figure out what the scroll position is when exactly you want to fix the nav
  //bar or div or whatever.  I stuck in the console.log for you.  Just remove when
  //you know the position.
  $(window).scroll(function () { 

    console.log($(window).scrollTop());

    if ($(window).width() < 600) {

      if ($(window).scrollTop() > 228) {
        $('#navbar').addClass('navbar-fixed');
      }

      if ($(window).scrollTop() < 228) {
        $('#navbar').removeClass('navbar-fixed');
      }

    }
    else if ($(window).width() < 1250) {

      if ($(window).scrollTop() > 128) {
        $('#navbar').addClass('navbar-fixed');
        $('.section').addClass('sfixed-top');
      }

      if ($(window).scrollTop() < 128) {
        $('#navbar').removeClass('navbar-fixed');
        $('.section').removeClass('sfixed-top');
      }
    }

    else {

      if ($(window).scrollTop() > 128) {
        $('#navbar').addClass('navbar-fixed');
        $('.section').addClass('fixed-top');
      }

      if ($(window).scrollTop() < 128) {
        $('#navbar').removeClass('navbar-fixed');
        $('.section').removeClass('fixed-top');
      }
    }


  });

  $(".button-collapse").sideNav();
});


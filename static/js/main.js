$(function() {
// toggle all paragraphs?
    $("#paragraph_one").delay(9999).fadeOut(2500,function(){
    $("#paragraph_two").slideDown(10000,function(){
    $("#paragraph_two").fadeOut(2500,function(){
    $("#riddle").slideDown(10000,function(){
    $(".next_action").fadeIn(2300,function(){
    $(".btns").fadeIn(2500) }) })}) })
  });

     $('#btn_p_one').click(function () {
        $('#paragraph_one').toggle()
        $('#paragraph_two').hide()
        $('#riddle').hide();
    });

    $('#btn_p_two').click(function () {
        $('#paragraph_one').hide()
        $('#paragraph_two').toggle();
        $('#riddle').hide();
    });

    $('#btn_riddle').click(function () {
        $('#paragraph_one').hide(2250)
        $('#paragraph_two').hide(2250);
        $('#riddle').toggle(2250);
    });
})



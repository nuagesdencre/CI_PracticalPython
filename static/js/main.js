$(function () {

    /* buttons revealing clues and red herrings*/

    $('.btns').click(function () {
        let selector = $(this).data('toggle');
        $(selector).toggle();
        $(this).toggleClass('selected');
    });

    // LEADERBOARD
    // highlighting the player's own stats in the leaderboard
    function highlight_leaderboard() {
        if ($('#leaderboard_check').html() != "   " && $('#leaderboard_check').html() != "Potato") {
            return $('#player').addClass('leaderboard_top');
        }
        $('#player').removeClass('leaderboard_top');
        alert("Your progress is not being recorded yet, begin the story and introduce yourself.");
    }
    highlight_leaderboard();

    // allow reader to increase font size
    $('.bigger').click(function () {
    $('*').each(function(){
       var text =  parseInt($(this).css('font-size'));
       var changeSize = ((text*120)/100) ;
           $(this).css('font-size',changeSize);

       })});
});
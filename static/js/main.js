$(function () {

    /* buttons revealing clues and red herrings*/
    //part 1

     $('#btn_dining').click(function () {
        $('.dining').toggle();
    });
    $('#btn_tablecloth').click(function () {
        $('.tablecloth').toggle();
    });

    $('#btn_room').click(function () {
        $('.room_view').toggle();
    });

    //part 2
     $('#btn_painting_couple').click(function () {
        $('.painting_couple').toggle();
    });

    $('#btn_painting_check').click(function () {
        $('.painting_check').toggle();
    });

    $('#btn_clock').click(function () {
        $('.clock_view').toggle();
    });
    $('#btn_clock_inside').click(function () {
        $('.clock_inside').toggle();
    });

    //part 3

    $('#btn_bookshelf').click(function () {
        $('.bookshelf').toggle();
    });

        $('#btn_under_the_bed').click(function () {
        $('.under_the_bed').toggle();
    });
    $('#btn_chest').click(function () {
        $('.chest').toggle();
    });

    $('#btn_paintings').click(function () {
        $('.paintings').toggle();
    });

    $('#btn_chessboard').click(function () {
        $('.chessboard').toggle();
    });

        $('#btn_missing').click(function () {
        $('.missing').toggle();
    });

    $('#btn_paintings').click(function () {
        $('.paintings_view').toggle();
    });

    //riddle
    $('#btn_riddle').click(function () {
        $('.riddle').toggle();
    });
   /* END buttons revealing clues and red herrings*/

    // LEADERBOARD
    // highlighting the player's own stats in the leaderboard
    function highlight_leaderboard() {
        if ($('#leaderboard_check').html() != null && $('#leaderboard_check').html() != 'Potato') {
            return $('#player').addClass('leaderboard_top');
        }
        $('#player').removeClass('leaderboard_top');
    }

    highlight_leaderboard();
})
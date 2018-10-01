$(function () {

    /* buttons revealing clues and red herrings*/
    //part 1

     $('#btn_dining').click(function () {
        $('.dining').toggle();
        $('#btn_dining').toggleClass('lace');
    });
    $('#btn_tablecloth').click(function () {
        $('.tablecloth').toggle();
        $('#btn_tablecloth').toggleClass('lace');
    });

    $('#btn_room').click(function () {
        $('.room_view').toggle();
        $('#btn_room').toggleClass('lace');
    });

    //part 2
     $('#btn_picture_couple').click(function () {
        $('.picture_couple').toggle();
        $('#btn_picture_couple').toggleClass('lace');
    });

    $('#btn_painting_check').click(function () {
        $('.painting_check').toggle();
        $('#btn_painting_check').toggleClass('lace');
    });

    $('#btn_clock').click(function () {
        $('.clock_view').toggle();
        $('#btn_clock').toggleClass('lace');
    });
    $('#btn_clock_inside').click(function () {
        $('.clock_inside').toggle();
        $('#btn_clock_inside').toggleClass('lace');
    });

    //part 3

    $('#btn_bookshelf').click(function () {
        $('.bookshelf').toggle();
        $('#btn_bookshelf').toggleClass('lace');
    });

        $('#btn_under_the_bed').click(function () {
        $('.under_the_bed').toggle();
         $('#btn_under_the_bed').toggleClass('lace');
    });
    $('#btn_chest').click(function () {
        $('.chest').toggle();
        $('#btn_chest').toggleClass('lace');
    });

    $('#btn_paintings').click(function () {
        $('.paintings').toggle();
        $('#btn_paintings').toggleClass('lace');
    });

    $('#btn_chessboard').click(function () {
        $('.chessboard').toggle();
        $('#btn_chessboard').toggleClass('lace');
    });

        $('#btn_missing').click(function () {
        $('.missing').toggle();
        $('#btn_missing').toggleClass('lace');
    });

    $('#btn_paintings').click(function () {
        $('.paintings_view').toggle();
        $('#btn_paintings_view').toggleClass('lace');
    });

    //riddle
    $('#btn_riddle').click(function () {
        $('.riddle').toggle();
        $('#btn_riddle').toggleClass('lace');
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
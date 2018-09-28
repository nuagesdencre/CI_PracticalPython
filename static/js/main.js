$(function () {

    // buttons revealing clues and red herrings
    $('#btn_riddle').click(function () {
        $('.riddle').toggle();
    });

    $('#btn_painting_couple').click(function () {
        $('.painting_couple').toggle();
    });

    $('#btn_room').click(function () {
        $('.room_view').toggle();
    });

    $('#btn_clock').click(function () {
        $('.clock_view').toggle();
    });

    $('#btn_bookshelf').click(function () {
        $('.bookshelf').toggle();
    });

    $('#btn_paintings').click(function () {
        $('.paintings').toggle();
    });

    $('#btn_chessboard').click(function () {
        $('.chessboard').toggle();
    });

    $('#btn_paintings').click(function () {
        $('.paintings_view').toggle();
    });

    // highlighting the player's own stats in the leaderboard
    function highlight_leaderboard() {
        if ($('#leaderboard_check').html() != null && $('#leaderboard_check').html() != 'Potato') {
            return $('#player').addClass('leaderboard_top');
        }
        $('#player').removeClass('leaderboard_top');
    }

    highlight_leaderboard();
})
// Works for only times less than 60 minutes
function startTimer(timeout, counter) {
    var timer = timeout, min, sec;
    setInterval(function () {
        min = parseInt(timer / 60, 10)
        min = min < 10 ? "0" + min : min;

        sec = parseInt(timer % 60, 10);
        sec = sec < 10 ? "0" + sec : sec;

        counter.text(min + ":" + sec);

        if (--timer < 0) {
            $($('#counter').data("finish")).submit()
        }
    }, 1000);
}

jQuery(function ($) {
    var pom_time = $('#counter').data("pom_time") * 60;
    var counter = $('#counter');
    startTimer(pom_time, counter);
});

function secondsToString(seconds) {
    var numhours = Math.floor((seconds ) / 3600);
    var numminutes = Math.floor(((seconds ) % 3600) / 60);
    var numseconds = ((seconds) % 3600) % 60;
    timeString = numhours + ":" + numminutes + ":" + numseconds;
    $("#time").text(timeString);
}

var canBid = true;
var seconds;

function updateClock(seconds) {
    this.seconds=seconds;
    setInterval(function(){manageClock()},1000);
}

function manageClock() {
    seconds = seconds - 1;
    secondsToString(seconds);
    if (seconds === 0) {
        canBid = false;
    }
}

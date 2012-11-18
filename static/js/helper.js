function secondsToString(seconds) {
    if (canBid) {
        var numhours = Math.floor((seconds ) / 3600);
        var numminutes = Math.floor(((seconds ) % 3600) / 60);
        var numseconds = ((seconds) % 3600) % 60;
        timeString = numhours + ":" + numminutes + ":" + numseconds;
        $("#time").text(timeString);
    }
}

var canBid = true;
var seconds;
var valueToBid = 0;

function updateClock(seconds) {
    this.seconds = seconds;
    setInterval(function () {
        manageClock()
    }, 1000);

}

function manageClock() {
    seconds = seconds - 1;
    secondsToString(seconds);
    if (seconds === 0) {
        canBid = false;
        $("#btnPujar").attr("disabled", true);
    }
}

function addBid(value) {
    this.valueToBid = value;
    $('#amountbar').width(80*(((value/10000)*2)-1)); //to cast to number
    console.log($('#amountbar').width());
    $('#ourprice').load('/calcFutureValue/'+value);
}
function pushBid() {
    if (canBid) {
        if (this.valueToBid === 0) {
            alert("primero selecciona el valor a aumentar");
        } else {
            $.post('/bid/' + this.valueToBid);
            $('#ourprice').load('/getMiValue');
            $('#amountbar').width(0);
            this.valueToBid = 0;
        }
    } else {
        alert("lo sentimos se acabo el tiempo");
    }
}

var auto_refresh = setInterval(
    function () {
        $('#priceact').load('/currentPrice');
        //update prices to bid
        for (i = 1; i <= 6; i++) {
            $('#price' + i).load('/getFuturePrice/' + i);
        }
    }, 1000);

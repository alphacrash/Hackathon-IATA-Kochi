function flight_status() {
    var x = document.getElementById('status');
    if (x.style.display === 'none') {
        x.style.display = 'block';
    }else {
        x.style.display = 'none';
    }
}
function increaseValue() {
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 0 : value;
  value++;
  document.getElementById('number').value = value;
}

function decreaseValue() {
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 0 : value;
  value < 1 ? value = 1 : '';
  value--;
  document.getElementById('number').value = value;
}

function hide_loader() {
    $('#loader').delay(1000).hide(0);
}

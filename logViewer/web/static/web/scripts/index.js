var btnDisconnect = document.getElementById('btnDisconnect');
var btnClear = document.getElementById('btnClear');

function connect(){
  var ws = new WebSocket("ws://bbahamondes-2.hwx.com:8765/logs");
  
  ws.onmessage = function (event) {
    var messages = document.getElementsByTagName('tbody')[0],
        row = document.createElement('tr'),
        cell = document.createElement('td');
    cell.innerHTML = event.data;
    row.appendChild(cell);
    messages.appendChild(row);
    console.log(messages.childElementCount);
  };

  btnDisconnect.disabled = false

  btnDisconnect.onclick = function(){
    ws.close();
  };

}

btnClear.onclick = function(){
  document.getElementsByTagName('tbody')[0].innerHTML = '';
}
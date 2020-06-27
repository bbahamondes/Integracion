var btnDisconnect = document.getElementById('btnDisconnect'),
    btnClear = document.getElementById('btnClear'),
    lineCounter = document.getElementById('counter'),
    messages = document.getElementsByTagName('tbody')[0];


function connect(){
  var ws = new WebSocket("ws://bbahamondes-2.hwx.com:8765/logs");
  
  ws.onmessage = function (event) {

    var row = document.createElement('tr'),
        ts = document.createElement('td'),
        level = document.createElement('td'),
        component = document.createElement('td'),
        body = document.createElement('td');
    jsonData = JSON.parse(event.data);

    ts.innerHTML = jsonData.timestamp;
    level.innerHTML = jsonData.level;
    component.innerHTML = jsonData.component;
    body.innerHTML = jsonData.body;
    row.appendChild(ts);
    row.appendChild(level);
    row.appendChild(component);
    row.appendChild(body);
    messages.appendChild(row);
    //console.log(messages.childElementCount);
    lineCounter.innerHTML = messages.childElementCount;
  };

  btnDisconnect.disabled = false
  btnDisconnect.onclick = function(){
    ws.close();
    console.log('Disconnected');
  };
}

btnClear.onclick = function(){
  messages.innerHTML = '';
  lineCounter.innerHTML = messages.childElementCount;
}
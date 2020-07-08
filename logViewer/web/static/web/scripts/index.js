$(document).ready(function() {
  var table1 = $('#table1').DataTable({
    "paging": false,
    "scrollY": '700px',
    "scollCollapse": true,
    colReorder: true
  });

  var btnDisconnect = document.getElementById('btnDisconnect'),
    btnClear = document.getElementById('btnClear'),
    lineCounter = document.getElementById('counter'),
    messages = document.getElementsByTagName('tbody')[0];


  $('#btnConnect').on('click', function connect(){
    var ws = new WebSocket("ws://bbahamondes-2.hwx.com:8765/logs");
    
    ws.onmessage = function (event) {

      var row = document.createElement('tr'),
          ts = document.createElement('td'),
          level = document.createElement('td'),
          component = document.createElement('td'),
          body = document.createElement('td');
      jsonData = JSON.parse(event.data);

      table1.row.add([
        jsonData.timestamp,jsonData.level, jsonData.component, jsonData.body
      ]).draw('false');

      lineCounter.innerHTML = table1.rows().count();
    };

    btnDisconnect.disabled = false
    btnDisconnect.onclick = function(){
      ws.close();
      console.log('Disconnected');
    };
  });

  btnClear.onclick = function(){
    table1.clear().draw();
    lineCounter.innerHTML = messages.childElementCount;
  }

} );

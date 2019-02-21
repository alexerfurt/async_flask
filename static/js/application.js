
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    var FUN_FACTS = {
      'APPLE': 'It\'s round',
      'GOOGLE': 'It\'s big',
    }

    //receive details from server
    socket.on('newfact', function(msg) {
        //maintain a list of ten numbers

        //console.log('SEE smth')
        var prodName = msg.product_name;
        var funFact = 'Never seen this product before';
        if (prodName && FUN_FACTS[prodName]){
          var funFact = FUN_FACTS[prodName]
        }

        $('#log').html(funFact);
    });

});

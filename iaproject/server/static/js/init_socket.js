    var socket = null;
    $(document).ready(function() {
      function log(msg) {
        var control = $('#log');
        control.html(control.html() + msg + '<br/>');
        control.scrollTop(control.scrollTop() + 1000);
      }

      function connect() {
        //disconnect();

        // Socket.IO magic, $.map does not work and crashes socket.io.
        var transports = [];
        $('#protocols input:checked').each(function(){
            return transports.push($(this).attr('id'));
        });

        // Hack to work around bug 251, I really hope it is going to be fixed.
        // https://github.com/LearnBoost/socket.io-client/issues/251
        // Alternative way to do full reconnect is to pass 'force new connection',
        // but you will lose multiplexing.
        io.j = [];
        io.sockets = [];
        socket = io.connect('http://' + window.location.host + '/', {
                  //'force new connection': true,
                  transports: transports,
                  rememberTransport: false
               });

        log('Connecting...');

        socket.on('connect', function() {
          log('Connected.');
          /**
           * DEMARRAGE DU JEU
           */
          // L'event initialise la connexion et démarre la partie
          socket.emit('init', '{"players" : [{"id": 1, "username": "toto"}, {"id": 2, "username": "titi"}]}')
        });

		// Récupération du JSON de la Map
        socket.on('map_json', function(data) {
        	Engine.Map = JSON.parse(data);
          	log('Map Received: ' + Engine.Map);
          	Engine.DrawMap();
          	socket.emit('map_loaded', '{"init_map": true}')
        });

		// Récupération du JSON des voitures
        socket.on('voitures_json', function(data) {
        	Engine.Voiture = JSON.parse(data);
          	log('Voitures Received: ' + data);
          	init();
          	socket.emit('start', '{"init_voitures": true}')
        });
		
		// Frames du jeu (JSON des nouvelles coordonnées à dessiner)
        socket.on('frame', function(data) {
        	Engine.Voiture = JSON.parse(data);
          	//log('Voitures Frame Received: ' + data);
        	update_ui();
        });
        
        // Fin de la partie (ou déconnexion forcée)
        socket.on('disconnect', function(data) {
          log('Disconnected.');
          socket = null;
          update_ui();
        });
      }

      function disconnect() {
        if (socket != null) {
          log('Disconnecting...');

          socket.disconnect();
          socket = null;

          update_ui();
        }
      }

      function update_ui() {
      	/**
      	 * ICI doit se redessiner l'ensemble des éléments mobiles du décor
      	 * --> Faire bouger les voitures
      	 */
      	Engine.DrawVoiture();
      }
      
      connect();
      
    });
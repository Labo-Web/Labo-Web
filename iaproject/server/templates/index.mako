<html>
  <head>
   	<meta http-equiv="content-type" content="text/html; charset=utf-8"/> 
    <title>Game</title>
  	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
	<script type="text/javascript" src="/static/js/socket.io.js"></script>
	<script type="text/javascript" src="/static/js/main.js"></script>
	<script type="text/javascript" src="/static/js/init_socket.js"></script>
	<link type="text/css" rel="stylesheet" href="/static/css/main.css" media="screen">
    <script>
		WEB_SOCKET_SWF_LOCATION = '/static/WebSocketMain.swf';
	</script>
  </head>
  <body>
	<div id="container" class="container_16">
		<div id="mapframe">
			<div id="conteneurvoiture">
			</div>
	    	<canvas id="gameframe" width="800" height="600" onclick="Engine.ChangeCase(this)"></canvas>
	    </div>
		<div id="control">
			<div id="tools"> <button onclick="Engine.DumpMap()">Dump</button><button onclick="Engine.NewMap()">New</button>	</div>
	    	<div id="info"></div>
		</div>
	</div>
	<div id="logging">
		LOGGER
		<table>
			<tr>
				<td><div id="log"></div></td>
				<td><div id="engine_log"></div></td>
			</tr>
		</table>
	</div>
  </body>
</html>
//DÃ©claration l'objet Engine
var Engine = {};

//Déclaration l'objet Engine
var Engine = {};

//json pour afficher la voiture en fonction de coordonnée
	
//Déclaration d'un objet Map
Engine.Map = {};

//Déclaration d'un objet Param
Engine.Param = {};

//Déclaration d'un objet Camera
Engine.Camera = {};

//Déclaration d'un tableau pour les images
Engine.Tiles = new Array();

//Déclaration d'un tableau image voiture
Engine.Voitures = new Array();

//Function lancée quand la page est chargée (onload dans HTML)
function init(){
	//Déclaration de la variable séléctionnant l'élément canvas

    var canvas = document.getElementById('gameframe');
	var canvas2 = document.getElementById('voiture');
	
	//Applique le contexte au canvas 2
	Engine.context = canvas2.getContext("2d");

	//Permet de tester si navigateur capable de faire tourner du canvas
    if (canvas.getContext){
        
		//Parameters
		
		//Stock le context du canvas dans un objet
        Engine.ctx = canvas.getContext('2d'); 
		
		//Définie la largeur et hauteur du canvas
        Engine.Param.CanvasW = parseInt(canvas.getAttribute("width")) ;
        Engine.Param.CanvasH = parseInt(canvas.getAttribute("height"));
		
		//Définie la taille d'une case
        Engine.Param.CaseSize=10
		Engine.Param.CaseSizeV=30
        
		//Définie les différentes images pour les textures
        Engine.Tiles[0] = new Image();
        Engine.Tiles[0].src = '/static/img/grass.jpg';
        Engine.Tiles[1] = new Image();
        Engine.Tiles[1].src = '/static/img/road.jpg';      
		Engine.Tiles[2] = new Image();
        Engine.Tiles[2].src = '/static/img/sand.jpg';
		Engine.Tiles[3] = new Image();
        Engine.Tiles[3].src = '/static/img/tire.jpg';
        Engine.Tiles[4] = new Image();
        Engine.Tiles[4].src = '/static/img/start-end.jpg';

		//Définie les texture des voitures
		Engine.Voitures[0] = new Image();
		Engine.Voitures[0].src = '/static/img/voiture.jpg';
		Engine.Voitures[1] = new Image();
		Engine.Voitures[1].src = '/static/img/voiture2.jpg';
		
		//On lance la méthode DrawMap
		Engine.DrawMap();
		Engine.DrawVoiture();
	}
		
}

Engine.DrawVoiture = function() {
	
	var jsonVoiture = Engine.Voiture.voiture;
	
	//Récupération dans le dom du canvas correspondant à l'id du json
	var canvas = document.getElementById("voiture");
	var context = canvas.getContext("2d");
	context.save();
	
	for (elm in jsonVoiture) {	
		
		var id = jsonVoiture[elm].id;

		//Récupération de la en fonction de l'idtexture du json
		var textureVoiture = jsonVoiture[elm].texture;
		var texture = Engine.Voitures[textureVoiture];

		var Width = texture.width;
		var Height = texture.height;

		//Récupération des coordonnées au centre de l'image
		var x = jsonVoiture[elm].x;
		var y = jsonVoiture[elm].y;
		var X = jsonVoiture[elm].x + Width / 2;
		var Y = jsonVoiture[elm].y + Height / 2;
		
		//Création de l'image dans le canvas
		
		//Positionnement du canvas sur la carte avec x, y et angle
		//canvas.style.left = X;
		//canvas.style.top = Y;
		Engine.context.translate(Y, X);
		Engine.context.rotate(jsonVoiture[elm].angle * Math.PI/180);
		
		Engine.context.drawImage(texture, y - Y, x - X, Width, Height);
		Engine.context.restore();
		
		//canvas.style.webkitTransform = "rotate("+ jsonVoiture[elm].angle+"deg)";
		
	}
}

//Change la position de l'image
Engine.ModifVoiture = function () {
	
}

//Methode de modification de la case au clic(appeller dans le html)
Engine.ChangeCase = function(elm) {
	
	//Déclare une variable x, y définissant la quand on clique la valeur x dans la fenêtre
	var clickX = window.event.x-elm.offsetLeft;
	var clickY = window.event.y-elm.offsetTop;
	
	//Retourne l'entier inférieur(floor) x, y de la case
	var CaseX = Math.floor(clickX/Engine.Param.CaseSize);
	var CaseY = Math.floor(clickY/Engine.Param.CaseSize);
	
	//Incrément dans l'objet Engine.Map par coordonnée
	Engine.Map.cases[CaseY][CaseX]++;
	
	//Déclaration de la variable case comprennant l'int du type de case
	var Case = Engine.Map.cases[CaseY][CaseX];
	
	//Déclaration de la variable récupérant la texture
	var texture = Engine.Tiles[Case];
	
	//Test permettant de déterminer si pas de texture définir la texture par défaut : 0
	if(texture == undefined)
		Engine.Map.cases[CaseY][CaseX]=0;
	Engine.DrawMap();
};

//Méthode permettant de contruire la map dans le canvas au chargement de la page
Engine.DrawMap= function () {
	//Boucle permettant de parcourir la hauteur du canvas
	for (y = 0; y < Engine.Param.CanvasH / Engine.Param.CaseSize ; y++) {
		//Boucle permettant de parcourir la hauteur du canvas
        	 for (x = 0; x < Engine.Param.CanvasW / Engine.Param.CaseSize; x++) {
			//Déclaration de la texture
			var texture;
			//Déclaration de la case 
			var Case = 0; 
			
			//Try catch : 
			// - Récupére la valeur du json y,x
			// - récupère la texture en fonction de la valeur du json
			try{
				Case = Engine.Map.cases[y][x];
                texture = Engine.Tiles[Case];
             }
			catch(e){texture = Engine.Tiles[0];};
				Engine.ctx.drawImage(texture,x*Engine.Param.CaseSize,y*Engine.Param.CaseSize)
		}
	}
};

//Function permettant de générer un json en fonction des textures de la map
Engine.DumpMap = function () {
	document.getElementById('info').innerHTML=JSON.stringify(Engine.Map);
}
Engine.NewMap= function()
{
	Engine.Map.cases={};
    for (y = 0; y < Engine.Param.CanvasH / Engine.Param.CaseSize; y++) {
		Engine.Map.cases[y]={};
        for (x = 0; x < Engine.Param.CanvasW / Engine.Param.CaseSize; x++) {
            Engine.Map.cases[y][x]=0;
        }
    }
	Engine.DumpMap();
    Engine.DrawMap();
}
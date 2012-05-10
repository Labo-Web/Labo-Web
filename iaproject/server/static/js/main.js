<<<<<<< HEAD
//DÃ©claration l'objet Engine
var Engine = {};

//json pour afficher la voiture en fonction de coordonnÃ©e
	
//DÃ©claration d'un objet Map
Engine.Map = {};

//DÃ©claration d'un objet Param
Engine.Param = {};

//DÃ©claration d'un objet Camera
Engine.Camera = {};

//DÃ©claration d'un tableau pour les images
Engine.Tiles = new Array();

//DÃ©claration d'un tableau image voiture
Engine.Voitures = new Array();

//Function lancÃ©e quand la page est chargÃ©e (onload dans HTML)
function init(){
	//DÃ©claration de la variable sÃ©lÃ©ctionnant l'Ã©lÃ©ment canvas
=======
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
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
    var canvas = document.getElementById('gameframe');
	var canvas2 = document.getElementById('voiture');
	
	//Applique le contexte au canvas 2
	Engine.context = canvas2.getContext("2d");

	//Permet de tester si navigateur capable de faire tourner du canvas
    if (canvas.getContext){
        
		//Parameters
		
		//Stock le context du canvas dans un objet
        Engine.ctx = canvas.getContext('2d'); 
		
<<<<<<< HEAD
		//DÃ©finie la largeur et hauteur du canvas
        Engine.Param.CanvasW = parseInt(canvas.getAttribute("width")) ;
        Engine.Param.CanvasH = parseInt(canvas.getAttribute("height"));
		
		//DÃ©finie la taille d'une case
        Engine.Param.CaseSize=10
		Engine.Param.CaseSizeV=30
        
		//DÃ©finie les diffÃ©rentes images pour les textures
=======
		//Définie la largeur et hauteur du canvas
        Engine.Param.CanvasW = parseInt(canvas.getAttribute("width")) ;
        Engine.Param.CanvasH = parseInt(canvas.getAttribute("height"));
		
		//Définie la taille d'une case
        Engine.Param.CaseSize=10
		Engine.Param.CaseSizeV=30
        
		//Définie les différentes images pour les textures
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
        Engine.Tiles[0] = new Image();
        Engine.Tiles[0].src = './static/img/grass.jpg';
        Engine.Tiles[1] = new Image();
        Engine.Tiles[1].src = './static/img/road.jpg';      
		Engine.Tiles[2] = new Image();
        Engine.Tiles[2].src = './static/img/sand.jpg';
		Engine.Tiles[3] = new Image();
        Engine.Tiles[3].src = './static/img/tire.jpg';
        Engine.Tiles[4] = new Image();
        Engine.Tiles[4].src = './static/img/start-end.jpg';

<<<<<<< HEAD
		//DÃ©finie les texture des voitures
=======
		//Définie les texture des voitures
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
		Engine.Voitures[0] = new Image();
		Engine.Voitures[0].src = './static/img/voiture.jpg';
		Engine.Voitures[1] = new Image();
		Engine.Voitures[1].src = './static/img/voiture2.jpg';
		
<<<<<<< HEAD
		//On lance la mÃ©thode DrawMap
=======
		//On lance la méthode DrawMap
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
		Engine.DrawMap();
		Engine.DrawVoiture();
	}
		
}

Engine.DrawVoiture = function() {
	
	var jsonVoiture = Engine.Voiture.voiture;
	
<<<<<<< HEAD
	//RÃ©cupÃ©ration dans le dom du canvas correspondant Ã  l'id du json
	Engine.context.clearRect(0,0,800,600);
	Engine.context.save();
=======
	//Récupération dans le dom du canvas correspondant à l'id du json
	var canvas = document.getElementById("voiture");
	var context = canvas.getContext("2d");
	context.save();
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
	
	for (elm in jsonVoiture) {	
		
		var id = jsonVoiture[elm].id;

<<<<<<< HEAD
		//RÃ©cupÃ©ration de la en fonction de l'idtexture du json
=======
		//Récupération de la en fonction de l'idtexture du json
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
		var textureVoiture = jsonVoiture[elm].texture;
		var texture = Engine.Voitures[textureVoiture];

		var Width = texture.width;
		var Height = texture.height;
		
<<<<<<< HEAD
		//RÃ©cupÃ©ration des coordonnÃ©es au centre de l'image
=======
		//Récupération des coordonnées au centre de l'image
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
		var x = jsonVoiture[elm].x;
		var y = jsonVoiture[elm].y;
		var X = jsonVoiture[elm].x + Width / 2;
		var Y = jsonVoiture[elm].y + Height / 2;
		
<<<<<<< HEAD
		//CrÃ©ation de l'image dans le canvas
=======
		//Création de l'image dans le canvas
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
		
		//Positionnement du canvas sur la carte avec x, y et angle
		//canvas.style.left = X;
		//canvas.style.top = Y;
<<<<<<< HEAD
		Engine.context.translate(Y, X);
		Engine.context.rotate(jsonVoiture[elm].angle * Math.PI/180);
		
		Engine.context.drawImage(texture, y - Y, x - X, Width, Height);
		Engine.context.restore();
=======
		context.translate(Y, X);
		context.rotate(jsonVoiture[elm].angle * Math.PI/180);
		
		context.drawImage(texture, y - Y, x - X, Width, Height);
		context.restore();
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
		
		//canvas.style.webkitTransform = "rotate("+ jsonVoiture[elm].angle+"deg)";
		
	}
}

//Change la position de l'image
Engine.ModifVoiture = function () {
	
}

//Methode de modification de la case au clic(appeller dans le html)
Engine.ChangeCase = function(elm) {
	
<<<<<<< HEAD
	//DÃ©clare une variable x, y dÃ©finissant la quand on clique la valeur x dans la fenÃªtre
	var clickX = window.event.x-elm.offsetLeft;
	var clickY = window.event.y-elm.offsetTop;
	
	//Retourne l'entier infÃ©rieur(floor) x, y de la case
	var CaseX = Math.floor(clickX/Engine.Param.CaseSize);
	var CaseY = Math.floor(clickY/Engine.Param.CaseSize);
	
	//IncrÃ©ment dans l'objet Engine.Map par coordonnÃ©e
	Engine.Map.cases[CaseY][CaseX]++;
	
	//DÃ©claration de la variable case comprennant l'int du type de case
	var Case = Engine.Map.cases[CaseY][CaseX];
	
	//DÃ©claration de la variable rÃ©cupÃ©rant la texture
	var texture = Engine.Tiles[Case];
	
	//Test permettant de dÃ©terminer si pas de texture dÃ©finir la texture par dÃ©faut : 0
=======
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
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
	if(texture == undefined)
		Engine.Map.cases[CaseY][CaseX]=0;
	Engine.DrawMap();
};

<<<<<<< HEAD
//MÃ©thode permettant de contruire la map dans le canvas au chargement de la page
=======
//Méthode permettant de contruire la map dans le canvas au chargement de la page
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
Engine.DrawMap= function () {
	//Boucle permettant de parcourir la hauteur du canvas
	for (y = 0; y < Engine.Param.CanvasH / Engine.Param.CaseSize ; y++) {
		//Boucle permettant de parcourir la hauteur du canvas
        	 for (x = 0; x < Engine.Param.CanvasW / Engine.Param.CaseSize; x++) {
<<<<<<< HEAD
			//DÃ©claration de la texture
			var texture;
			//DÃ©claration de la case 
			var Case = 0; 
			
			//Try catch : 
			// - RÃ©cupÃ©re la valeur du json y,x
			// - rÃ©cupÃ¨re la texture en fonction de la valeur du json
=======
			//Déclaration de la texture
			var texture;
			//Déclaration de la case 
			var Case = 0; 
			
			//Try catch : 
			// - Récupére la valeur du json y,x
			// - récupère la texture en fonction de la valeur du json
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
			try{
				Case = Engine.Map.cases[y][x];
                texture = Engine.Tiles[Case];
             }
			catch(e){texture = Engine.Tiles[0];};
				Engine.ctx.drawImage(texture,x*Engine.Param.CaseSize,y*Engine.Param.CaseSize)
		}
	}
};

<<<<<<< HEAD
//Function permettant de gÃ©nÃ©rer un json en fonction des textures de la map
=======
//Function permettant de générer un json en fonction des textures de la map
>>>>>>> 23a7be74154ef012804daeb30f9f75dd0164b9ed
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
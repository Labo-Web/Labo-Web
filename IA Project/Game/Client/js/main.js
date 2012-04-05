//Déclaration l'objet Engine
var Engine = {};

//json pour afficher la voiture en fonction de coordonnée
var myJson = {
		"voiture" : [
			{
				"id" : 1,
				"texture" : 0, 
				"x" : 90,
				"y" : 90,
				"angle" : 45
			},
			{
				"id" : 2,
				"texture" : 1, 
				"x" : 300,
				"y" : 78,
				"angle" : 90
			}
		]
	};
	
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
        Engine.Tiles[0].src = './img/grass.jpg';
        Engine.Tiles[1] = new Image();
        Engine.Tiles[1].src = './img/road.jpg';      
		Engine.Tiles[2] = new Image();
        Engine.Tiles[2].src = './img/sand.jpg';
		Engine.Tiles[3] = new Image();
        Engine.Tiles[3].src = './img/tire.jpg';

		//Définie les texture des voitures
		Engine.Voitures[0] = new Image();
		Engine.Voitures[0].src = './img/voiture.jpg';
		Engine.Voitures[1] = new Image();
		Engine.Voitures[1].src = './img/voiture2.jpg';
		
		//On lance la méthode DrawMap
		Engine.DrawMap();
		Engine.DrawVoiture();
		}
}

Engine.DrawVoiture = function() {
	
	for (elm in myJson.voiture) {
		var x = myJson.voiture[elm].x;
		var y = myJson.voiture[elm].y;
		
		var rotate = myJson.voiture[elm].angle;
		
		var textureVoiture = myJson.voiture[elm].texture;
		var texture = Engine.Voitures[textureVoiture];
		
		//alert(x);
		//alert(y);
		//alert(textureVoiture);
		//alert(texture);

		Engine.ctx.drawImage(texture,x,y)
		Engine.ctx.rotate(rotate);
	}
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
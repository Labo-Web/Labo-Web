//Déclaration l'objet Engine
var Engine = {};

//D�claration l'objet Engine
var Engine = {};

//json pour afficher la voiture en fonction de coordonn�e
	
//D�claration d'un objet Map
Engine.Map = {};

//D�claration d'un objet Param
Engine.Param = {};

//D�claration d'un objet Camera
Engine.Camera = {};

//D�claration d'un tableau pour les images
Engine.Tiles = new Array();

//D�claration d'un tableau image voiture
Engine.Voitures = new Array();

//Function lanc�e quand la page est charg�e (onload dans HTML)
function init(){
	//D�claration de la variable s�l�ctionnant l'�l�ment canvas

    var canvas = document.getElementById('gameframe');
	var canvas2 = document.getElementById('voiture');
	
	//Applique le contexte au canvas 2
	Engine.context = canvas2.getContext("2d");

	//Permet de tester si navigateur capable de faire tourner du canvas
    if (canvas.getContext){
        
		//Parameters
		
		//Stock le context du canvas dans un objet
        Engine.ctx = canvas.getContext('2d'); 
		
		//D�finie la largeur et hauteur du canvas
        Engine.Param.CanvasW = parseInt(canvas.getAttribute("width")) ;
        Engine.Param.CanvasH = parseInt(canvas.getAttribute("height"));
		
		//D�finie la taille d'une case
        Engine.Param.CaseSize=10
		Engine.Param.CaseSizeV=30
        
		//D�finie les diff�rentes images pour les textures
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

		//D�finie les texture des voitures
		Engine.Voitures[0] = new Image();
		Engine.Voitures[0].src = '/static/img/voiture.jpg';
		Engine.Voitures[1] = new Image();
		Engine.Voitures[1].src = '/static/img/voiture2.jpg';
		
		//On lance la m�thode DrawMap
		Engine.DrawMap();
		Engine.DrawVoiture();
	}
		
}

Engine.DrawVoiture = function() {
	
	var jsonVoiture = Engine.Voiture.voiture;
	
	//Permet de reinitialiser le canvas
	Engine.context.setTransform(1, 0, 0, 1, 0, 0);
	
	//
	Engine.context.clearRect(0,0,800,600);
	Engine.context.save();
	
	for (elm in jsonVoiture) {	
		
		var id = jsonVoiture[elm].id;

		//R�cup�ration de la en fonction de l'idtexture du json
		var textureVoiture = jsonVoiture[elm].texture;
		var texture = Engine.Voitures[textureVoiture];
		
		//Recup hauteur l'argeur image
		var Width = texture.width;
		var Height = texture.height;
		
		//Convertie angle en radian
		var angle = jsonVoiture[elm].angle * Math.PI/180;
		
		//R�cup�ration des coordonn�es au centre de l'image
		var x = jsonVoiture[elm].x;
		var y = jsonVoiture[elm].y;
		
		//Centre de l'image
		var tw = Width / 2;
		var th = Height / 2;
		
		//Translation haut gauche de l'image
		Engine.context.translate(x, y);
		//Rotation de l'image avec radian
		Engine.context.rotate(angle);
		//Dessin de l'image
		Engine.context.drawImage(texture, - tw, - th, Width, Height);
		Engine.context.restore();
		
		
	}
}

//Methode de modification de la case au clic(appeller dans le html)
Engine.ChangeCase = function(elm) {
	
	//D�clare une variable x, y d�finissant la quand on clique la valeur x dans la fen�tre
	var clickX = window.event.x-elm.offsetLeft;
	var clickY = window.event.y-elm.offsetTop;
	
	//Retourne l'entier inf�rieur(floor) x, y de la case
	var CaseX = Math.floor(clickX/Engine.Param.CaseSize);
	var CaseY = Math.floor(clickY/Engine.Param.CaseSize);
	
	//Incr�ment dans l'objet Engine.Map par coordonn�e
	Engine.Map.cases[CaseY][CaseX]++;
	
	//D�claration de la variable case comprennant l'int du type de case
	var Case = Engine.Map.cases[CaseY][CaseX];
	
	//D�claration de la variable r�cup�rant la texture
	var texture = Engine.Tiles[Case];
	
	//Test permettant de d�terminer si pas de texture d�finir la texture par d�faut : 0
	if(texture == undefined)
		Engine.Map.cases[CaseY][CaseX]=0;
	Engine.DrawMap();
};

//M�thode permettant de contruire la map dans le canvas au chargement de la page
Engine.DrawMap= function () {
	//Boucle permettant de parcourir la hauteur du canvas
	for (y = 0; y < Engine.Param.CanvasH / Engine.Param.CaseSize ; y++) {
		//Boucle permettant de parcourir la hauteur du canvas
        	 for (x = 0; x < Engine.Param.CanvasW / Engine.Param.CaseSize; x++) {
			//D�claration de la texture
			var texture;
			//D�claration de la case 
			var Case = 0; 
			
			//Try catch : 
			// - R�cup�re la valeur du json y,x
			// - r�cup�re la texture en fonction de la valeur du json
			try{
				Case = Engine.Map.cases[y][x];
                texture = Engine.Tiles[Case];
             }
			catch(e){texture = Engine.Tiles[0];};
				Engine.ctx.drawImage(texture,x*Engine.Param.CaseSize,y*Engine.Param.CaseSize)
		}
	}
};

//Function permettant de g�n�rer un json en fonction des textures de la map
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
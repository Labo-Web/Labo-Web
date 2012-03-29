var CaseSize, CanvasW, CanvasH; 
var Engine = {};
Engine.Map = {};
Engine.Param =  {};
Engine.Camera ={};
Engine.FpsT=0;
Engine.Fps=0;
Engine.Tiles = new Array();
Engine.ChangeCase= function(elm)
{
var clickX = window.event.x-elm.offsetLeft;
var clickY = window.event.y-elm.offsetTop;
var CaseX= Math.floor(clickX/Engine.Param.CaseSize);
var CaseY= Math.floor(clickY/Engine.Param.CaseSize);
Engine.Map.cases[CaseY][CaseX]++;
var Case=Engine.Map.cases[CaseY][CaseX];
var texture = Engine.Tiles[Case];
if(texture==undefined)
	Engine.Map.cases[CaseY][CaseX]=0;
//alert(clickX+"/"+ clickY);
Engine.DrawMap();
};
function init(){
    var canvas = document.getElementById('gameframe');
    if (canvas.getContext){
        //parameters
        Engine.ctx = canvas.getContext('2d'); 
        Engine.Param.CanvasW = parseInt(canvas.getAttribute("width")) ;
        Engine.Param.CanvasH = parseInt(canvas.getAttribute("height"));

        Engine.Param.CaseSize=10
        
        Engine.Tiles[0] = new Image();
        Engine.Tiles[0].src = './img/sand.jpg';
        Engine.Tiles[1] = new Image();
        Engine.Tiles[1].src = './img/road.jpg';      
		Engine.Tiles[2] = new Image();
        Engine.Tiles[2].src = './img/grass.jpg';
		
		Engine.DrawMap();
		}
}
Engine.DrawMap= function ()
{

for (y = 0; y <29 ; y++) {
        for (x = 0; x < 20; x++) {
		var texture;
		var Case= 0; 
		try{
						Case=Engine.Map.cases[y][x];
                        texture = Engine.Tiles[Case];
                        img=true;
                    }
					  catch(e){texture = Engine.Tiles[0];};
			Engine.ctx.drawImage(texture,x*Engine.Param.CaseSize,y*Engine.Param.CaseSize)
		}
		}
}
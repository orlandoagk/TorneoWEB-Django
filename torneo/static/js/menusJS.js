var homeM = document.getElementById("Home");
homeM.addEventListener("mouseover",home,false);
homeM.addEventListener("mouseout",homeSalida,false);

var posicionesM = document.getElementById("Posiciones");
posicionesM.addEventListener("mouseover",posiciones,false);
posicionesM.addEventListener("mouseout",posicionesSalida,false);

var fotosM = document.getElementById("Fotos");
fotosM.addEventListener("mouseover",fotos,false);
fotosM.addEventListener("mouseout",fotosSalida,false);

var equipoM = document.getElementById("Equipo");
equipoM.addEventListener("mouseover",equipo,false);
equipoM.addEventListener("mouseout",equipoSalida,false);

// LA RUTA SERA static/torneo/images/...

function home(){
	homeM.src= "/static/torneo/images/button_home(1).png";
}
function homeSalida(){
	homeM.src= "/static/torneo/images/button_home.png";
}
function equipo(){
	equipoM.src= "/static/torneo/images/button_equipo(1).png";
}
function fotos(){
	fotosM.src= "/static/torneo/images/button_fotos(1).png";
}
function posiciones(){
	posicionesM.src= "/static/torneo/images/button_posiciones(1).png";
}
function equipoSalida(){
	equipoM.src= "/static/torneo/images/button_equipo.png";
}
function fotosSalida(){
	fotosM.src= "/static/torneo/images/button_fotos.png";
}
function posicionesSalida(){
	posicionesM.src= "/static/torneo/images/button_posiciones.png";
}
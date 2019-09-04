var f = new Date();
var semestre = "";
if (f.getMonth()+1<6){
	semestre = "I"
} else {
	semestre = "II"
}

document.getElementById("fechaActual").innerHTML = "Bienvenido a la pagina, estamos en el semestre "+" "+f.getFullYear() + "-" + semestre;

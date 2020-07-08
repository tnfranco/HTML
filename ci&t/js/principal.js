



$(document).ready(function () {
   getData(dias);

    iniciarCoresProgramacao();
    exibirHorarioSelecionado(new Date().getHours());
});

const DIAS_DA_SEMANA = ["Domingo", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"];
const PERSONAGENS_IMG = ["irmao-do-jorel.png", "darwin.png", "jake.png", "steven.png", "rigby.png", "clarence.png", "superpoderosa.png", "Titio-avo.png"];
var dias = 0;
var personagens = 0;

function getData(dias) {
    var data = new Date(); 
    data.setDate(data.getDate() + dias);

    var n = DIAS_DA_SEMANA[data.getDay()] + " " + (data.getDate());
    document.getElementById("data").innerHTML = n;
}

function iniciarCoresProgramacao() {
    for (i = 0; i <= 23; i++) {
        document.getElementById(i).style.backgroundColor = "#009ade";
        document.getElementById(++i).style.backgroundColor = "#ec0080";
        document.getElementById(++i).style.backgroundColor = "#ffea00";
    }
    var horaAtual = new Date().getHours();
    document.getElementById(horaAtual).style.color = document.getElementById(horaAtual).style.backgroundColor;
    document.getElementById(horaAtual).style.backgroundColor = "#000000";
}

function programacaoProximoDia() {
    dias++;
    getData(dias);
}

function exibirHorarioSelecionado(horario) {
    var idHorario = horario;
    if (horario < 10) horario = "0" + horario;
    document.getElementById("horario-selecionado").innerHTML = horario + "hr";
    document.getElementById("primeiro-horario").innerHTML = horario + ":00";
    document.getElementById("segundo-horario").innerHTML = horario + ":15";
    document.getElementById("terceiro-horario").innerHTML = horario + ":30";
    document.getElementById("quarto-horario").innerHTML = horario + ":45";
    document.getElementById("horario").style.backgroundColor = document.getElementById(idHorario).style.backgroundColor;
}

function mudarPersonagens() {
    var imagens_index = getImagensIndexAleatorio();
    for (i = 0; i < 5; i++) {
        document.getElementById("p" + i).src = "imagens/" + PERSONAGENS_IMG[imagens_index[i]];
    }
}

// serve para jogar 5 imagens aleotoriamente na tela
function getImagensIndexAleatorio() {
    var imagens = [], imagensIndex = 0;
    for (i = 0; imagens.length < 5; i++) {
        var x = Math.floor((Math.random() * 7));
        if (imagens.indexOf(x) > -1) continue;
        imagens[imagensIndex] = x;
        imagensIndex++;
    }
    return imagens;
}

function zoomLento(){
    var imagem = document.getElementById("imagem");
    for (var i = 100; i <= 200; i++){
        setTimeout(function(){
            zoom(imagem);
        }, 100 * (i / 10))
    }
}

function zoom(image){
    var width = image.width + 1;
    image.style.width = width + 'px';
    image.style.height = 'auto';
}

zoomLento();
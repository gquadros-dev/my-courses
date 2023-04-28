const flechaDireita = document.getElementById('flecha-direita');
const botao = document.getElementById('botao');
const navLeftSide = document.getElementById('nav-left-side');
const body = document.getElementById('body');
const main = document.getElementById('main');

const inverteImg = () => {
    flechaDireita.classList.toggle('inverter');
}

const puxaEsquerda = () => {
    botao.classList.toggle('puxa-esquerda2');
    navLeftSide.classList.toggle('puxa-esquerda');
    deixaEscuro.classList.toggle('black-box');
}

const deixaEscuro = document.createElement('div');
body.appendChild(deixaEscuro);

let coeficienteAEl = document.querySelector('#coeficiente-a');
let coeficienteBEl = document.querySelector('#coeficiente-b');
let coeficienteCEl = document.querySelector('#coeficiente-c');
let botaoResolverEl = document.querySelector('#botaoResolver');

botaoResolverEl.addEventListener('click', function () {
    let coeficienteAValue = parseFloat(coeficienteAEl.value);
    let coeficienteBValue = parseFloat(coeficienteBEl.value);
    let coeficienteCValue = parseFloat(coeficienteCEl.value);
    if (coeficienteAValue == 0) {
        window.alert('Essa função não é do segundo grau');
        return;
    }
    let delta = Math.pow(coeficienteBValue, 2) - (4 * coeficienteAValue * coeficienteCValue);
    let resultadoDeltaEl = document.querySelector('#resultado-delta');
    resultadoDeltaEl.value = delta;
    resultadoX1El = document.querySelector('#resultado-x1');
    resultadoX2El = document.querySelector('#resultado-x2');
    if (delta < 0) {
        resultadoX1El.value = '';
        resultadoX2El.value = '';
    }
    if (delta > 0) {
        resultadoX1El.value = (-coeficienteBValue + Math.sqrt(delta)) / (2 * coeficienteAValue);
        resultadoX2El.value = (-coeficienteBValue - Math.sqrt(delta)) / (2 * coeficienteAValue);
    }
});

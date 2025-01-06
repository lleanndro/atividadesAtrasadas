let todosBotoes = document.querySelectorAll('.botao-expandir-retrair');

for (let i = 0; i < todosBotoes.length; i++) {
    todosBotoes[i].addEventListener('click', function (e) {
        let botaoClick = e.currentTarget;
        let paragrafoPai = botaoClick.parentNode;
        paragrafoPai.classList.toggle('expandido');
        if (paragrafoPai.classList.contains('expandido')){
            botaoClick.textContent = '-';
        }
        else{
            botaoClick.textContent = '+';
        }
        window.alert('Você abriu um paragrafo.');
    });
}





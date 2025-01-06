// Faça o exercício da GALERIA de IMAGENS neste arquivo
// Este arquivo AINDA NÃO está incluído no arquivo HTML

// caminho para onde as imagens estão hospedadas
const servidorDasImagens = 'https://fegemo.github.io/cefet-front-end/images/',
  // array com o nome das 5 imagens da galeria
  nomesDasImagens = [
    '01-philae-parts.jpg',
    '02-philae-rosetta.jpg',
    '03-philae-separation.jpg',
    '04-philae-67-picture.jpg',
    '05-philae-collecting.jpg'
  ];

// o índice da imagem sendo mostrada
// (inicialmente, é a imagem 0: '01-philae-parts.jpg')
let indiceDaFotoAtual = 0;

let botaoAnteriorEl = document.querySelector('#anterior');
let botaoProximoEl = document.querySelector('#proximo');
let imagens = document.querySelectorAll('img');
botaoProximoEl.addEventListener('click', function () {
  if(indiceDaFotoAtual == nomesDasImagens.length-1){
    indiceDaFotoAtual = 0;
    const caminhoImagem = servidorDasImagens + nomesDasImagens[indiceDaFotoAtual];
    let slideEl = document.querySelector('#slide');
    slideEl.src = caminhoImagem;
  }
  else if (indiceDaFotoAtual < nomesDasImagens.length - 1) {
    indiceDaFotoAtual++;
    const caminhoImagem = servidorDasImagens + nomesDasImagens[indiceDaFotoAtual];
    let slideEl = document.querySelector('#slide');
    slideEl.src = caminhoImagem;
  }
 
})
botaoAnteriorEl.addEventListener('click', function () {
  if(indiceDaFotoAtual == 0){
    indiceDaFotoAtual = nomesDasImagens.length-1;
    const caminhoImagem = servidorDasImagens + nomesDasImagens[indiceDaFotoAtual];
    let slideEl = document.querySelector('#slide');
    slideEl.src = caminhoImagem;
  }
  else if (indiceDaFotoAtual > 0) {
    indiceDaFotoAtual--;
    const caminhoImagem = servidorDasImagens + nomesDasImagens[indiceDaFotoAtual];
    let slideEl = document.querySelector('#slide');
    slideEl.src = caminhoImagem;
  }
})





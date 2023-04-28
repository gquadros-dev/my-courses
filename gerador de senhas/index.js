let a = function(){
    const inputTamanhoSenha = document.getElementById('numCaracteres');
    const tamanhoSenha = inputTamanhoSenha.value;
    const resultado = document.getElementById('resultado')
    
    const letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
    const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
    const caracteres = ['!', '@', '#', '$', '%', '&', '*', '-', '_', '?'];
    const senhaFinal = [];
    
    const shuffleArray = (arr) => {
        for (let i = arr.length - 1; i >= 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    }

    const randInt = (max) => {
        return Math.floor(Math.random()*max)
    }
    
    const randomItem = (lista) => {
        let max = lista.length;
        let randomInteger = Math.floor(Math.random()*max);
        return lista[randomInteger];
    }
    
    var senha = function(){
        for(let i = 0; i < 2; i++){senhaFinal.push(randomItem(letras).toUpperCase())};
        for(let i = 0; i < 2; i++){senhaFinal.push(randomItem(letras))};
        senhaFinal.push(randomItem(numeros));
        senhaFinal.push(randomItem(caracteres));
    }
    
    var senhaMaisQueSeis = function(){
        for(let i = 6; i < tamanhoSenha; i++){
            let random = randInt(3);
            if (random === 0){
                let random2 = randInt(2);
                if (random2 === 0){
                    senhaFinal.push(randomItem(letras).toUpperCase());
                } else {
                    senhaFinal.push(randomItem(letras));
                }
            } else if (random === 1){
                senhaFinal.push(randomItem(numeros));
            } else {
                senhaFinal.push(randomItem(caracteres));
            }
        }
    }
    
    const gerarSenha = () => {
        if (tamanhoSenha === 6){
            senha();
        } else if (tamanhoSenha > 6 & tamanhoSenha <= 30){
            senha();
            senhaMaisQueSeis();
        } else {
            senhaFinal.push('Tenta de novo aí arrombado!');
        }
        shuffleArray(senhaFinal);
    }
    gerarSenha();
    let senhaFinalStr = senhaFinal.toString();
    senhaFinalStr = senhaFinalStr.replace(/,/g, '');
    if (senhaFinalStr !== 'Tenta de novo aí arrombado!'){
        resultado.innerHTML = `Sua senha ficou: <br> ${senhaFinalStr}`;
    }
    else{
        resultado.innerHTML = `<br> ${senhaFinalStr}`;
    }  
}

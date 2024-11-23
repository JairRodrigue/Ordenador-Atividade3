const fs = require('fs');
const os = require('os');

// Função de ordenação Merge Sort
function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }

    const meio = Math.floor(arr.length / 2);
    const esquerda = mergeSort(arr.slice(0, meio));
    const direita = mergeSort(arr.slice(meio));

    return merge(esquerda, direita);
}

function merge(esquerda, direita) {
    const resultado = [];
    let i = 0, j = 0;

    while (i < esquerda.length && j < direita.length) {
        if (esquerda[i] <= direita[j]) {
            resultado.push(esquerda[i]);
            i++;
        } else {
            resultado.push(direita[j]);
            j++;
        }
    }

    return resultado.concat(esquerda.slice(i)).concat(direita.slice(j));
}

// Função principal
function main() {
    // Informações da linguagem e sistema
    console.log("Linguagem: JavaScript (Node.js)");
    console.log(`Versão: ${process.version}`);
    console.log(`Sistema Operacional: ${os.type()} ${os.release()}`);
    console.log(`CPU: ${os.cpus()[0].model}`);
    console.log(`Memória RAM: ${(os.totalmem() / (1024 ** 3)).toFixed(2)} GB\n`);

    // Lendo o arquivo
    const inputFile = 'rsc/arq.txt';
    const outputFile = 'arq-saida.txt';

    try {
        const data = fs.readFileSync(inputFile, 'utf8');
        const numeros = data.split('\n').filter(line => line.trim() !== '').map(Number);

        // Merge Sort
        const start = process.hrtime();
        const ordenado = mergeSort(numeros);
        const end = process.hrtime(start);

        // Salvando em arquivo de saída
        fs.writeFileSync(outputFile, ordenado.join('\n'), 'utf8');

        // Informações de tempo e memória
        const tempoMs = (end[0] * 1000) + (end[1] / 1e6);
        const memoriaKb = process.memoryUsage().heapUsed / 1024;
        console.log(`Tempo de execução: ${tempoMs.toFixed(2)} ms`);
        console.log(`Memória utilizada: ${memoriaKb.toFixed(2)} KB`);
    } catch (err) {
        console.error(`Erro: ${err.message}`);
    }
}

main();

// Importa o módulo 'readline' para leitura interativa
const readline = require('readline').createInterface({
  input: process.stdin,  // Define a entrada como o teclado (standard input)
  output: process.stdout // Define a saída padrão (geralmente o terminal)
});

let valorSalario;
let valorBeneficios;

// Pergunta pelo salário
readline.question('Digite o valor do Salário: ', (inputSalario) => {
  // Converte a entrada para float (substitui vírgula por ponto para robustez)
  valorSalario = parseFloat(inputSalario.replace(',', '.'));

  // Pergunta pelos benefícios *dentro* da resposta da primeira pergunta
  readline.question('Digite o valor dos Benefícios: ', (inputBeneficios) => {
    // Converte a entrada para float
    valorBeneficios = parseFloat(inputBeneficios.replace(',', '.'));

    // --- Agora temos as duas entradas, podemos calcular ---

    const valorImposto = calcularImposto(valorSalario);
    const saida = valorSalario - valorImposto + valorBeneficios;
    console.log(saida.toFixed(2));

    // Fecha a interface readline, encerrando o programa
    readline.close();
  });
});


//Função útil para o cálculo do imposto (permanece a mesma)
function calcularImposto(salario) {
    let aliquota; 
    if (salario >= 0 && salario <= 1100) {
        aliquota = 0.05;
    } else if (salario >= 1100.01 && salario <= 2500.00) {
        aliquota = 0.10;
    } else {
        aliquota = 0.15;
    }
    return aliquota * salario;
}

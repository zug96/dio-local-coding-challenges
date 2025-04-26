# Desafios de Código DIO - Ambiente Local: "A Linguagem é Só Um Detalhe..."

Este repositório contém as soluções para os desafios de código propostos na seção "A Linguagem é Só Um Detalhe... Como Resolver Desafios de Código" do bootcamp de Linux pertencente a DIO(Digital Innovation One).

## Contexto e Motivação

Durante o acompanhamento das aulas em vídeo, foi observado que o ambiente de execução e testes apresentado pelo instrutor não estava acessível para mim na plataforma da DIO no momento (o único desafio disponível era "Associando Comandos CLI").

Como solução alternativa e para garantir a realização prática dos exercícios em diferentes linguagens, optei por configurar um ambiente de desenvolvimento local em uma vm Linux (Ubuntu) para compilar, executar e testar as soluções.

## Configuração do Ambiente Local

Para isolar os testes e simular um ambiente limpo, as seguintes etapas foram realizadas no Linux:

1.  **Criação de Usuário Dedicado:** Foi criado um usuário específico para os testes:
    ```bash
    sudo useradd gus_testes -c "Designado para testes" -m -s /bin/bash -p <senha_criptografada>
    ```
2.  **Estrutura de Diretórios:** Dentro do diretório home do usuário `gus_testes`, foi criada a seguinte estrutura para organização:
    ```
    ~/Desafios-de-Código_DIO/
    └── Scripts/
        ├── desafio-java-1/
        │   └── Desafio.java
        ├── desafio-csharp-1/
        │   ├── Program.cs
        │   └── desafio-csharp-1.csproj
        │   └── ... (outros arquivos do 'dotnet new console')
        ├── desafio-javascript-1/
        │   └── desafio_java-script.js
        ├── desafio-python-1/
        │   └── desafio_python.py
        └── desafio-kotlin-1/
            ├── desafio_kotlin.kt
            └── desafio_kotlin.jar 
    ```

## Desafios e Linguagens

Abaixo estão os detalhes da configuração e execução para cada linguagem abordada.

### 1. Java

* **Ambiente:** OpenJDK (instalado via `sudo apt install default-jdk`).
* **Arquivo:** `desafio-java-1/Desafio.java`
* **Compilação:** `javac Desafio.java`
* **Execução:** `java Desafio`
* **Observações:** Foi necessário atenção ao Locale do Java (`pt_BR`). A entrada de dados (`Scanner.nextFloat()`) esperava **vírgula (`,`)** como separador decimal, causando `InputMismatchException` ao usar ponto.

### 2. C# (C Sharp)

* **Ambiente:** .NET SDK 8.0 (instalado via repositório da Microsoft e `sudo apt install dotnet-sdk-8.0`).
* **Projeto:** Criado com `dotnet new console` no diretório `desafio-csharp-1/`.
* **Arquivo Principal:** `Program.cs`
* **Execução:** `dotnet run` (compila e executa).
* **Observações:** Corrigidos erros de sintaxe (`$$` -> `&&`) e de tipo (atribuição/multiplicação de string em vez de float). Para garantir consistência na leitura e escrita de decimais (usando **ponto (`.`)**), foi utilizado `CultureInfo.InvariantCulture` nos métodos `float.Parse()` e `ToString()`.

### 3. JavaScript (Node.js)

* **Ambiente:** Node.js e NPM (instalados via `sudo apt install nodejs npm`).
* **Arquivo:** `desafio-javascript-1/desafio_java-script.js`
* **Execução:** `node desafio_java-script.js`
* **Observações:** As funções `gets()` e `print()` (comuns em plataformas online) não são padrão no Node.js. A leitura inicial via `fs.readFileSync('/dev/stdin')` causou erro de permissão (`EACCES`). A solução foi refatorar o código para usar o módulo `readline` para entrada interativa, que funcionou corretamente. Corrigidos também erros de case (`Let` -> `let`, `tofixed` -> `toFixed`).

### 4. Python

* **Ambiente:** Python 3 (já pré-instalado no sistema).
* **Arquivo:** `desafio-python-1/desafio_python.py`
* **Execução:** `python3 desafio_python.py`
* **Observações:** O principal desafio foi um `TabError` devido à mistura inconsistente de tabs e espaços na indentação. O erro foi corrigido padronizando a indentação para 4 espaços por nível. A leitura (`input()`) e conversão (`float()`) funcionaram diretamente (esperando **ponto (`.`)** para decimais).

### 5. Kotlin

* **Ambiente:** Compilador Kotlin (instalado via `sudo apt install kotlin`), rodando sobre a JVM (Java JDK pré-instalado).
* **Arquivo:** `desafio-kotlin-1/desafio_kotlin.kt`
* **Compilação:** `kotlinc desafio_kotlin.kt -include-runtime -d desafio_kotlin.jar`
* **Execução:** `java -jar desafio_kotlin.jar`
* **Observações:** A leitura de entrada foi feita com `readln()` e a conversão com `.toFloat()` (esperando **ponto (`.`)**). A saída formatada usou `println("%.2f".format(saida))`.

## Versionamento

Este projeto utiliza Git e está hospedado no GitHub. Cada solução de desafio foi commitada individualmente, e a estrutura de diretórios foi refatorada para melhor organização.

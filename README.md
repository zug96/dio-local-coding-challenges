# 🚀 Desafios de Código DIO - Ambiente Local: "A Linguagem é Só Um Detalhe..."

Bem-vindo a este repositório! Ele documenta a jornada e as soluções para os desafios de código propostos na seção "A Linguagem é Só Um Detalhe... Como Resolver Desafios de Código" do bootcamp da DIO.

## 🤔 Contexto e Motivação

Durante o acompanhamento das aulas em vídeo, foi observado que o ambiente de execução online apresentado nas videoaulas não estava acessível para a realização destes desafios específicos (apenas o desafio "Associando Comandos CLI" estava disponível).

Como solução alternativa e para garantir a realização prática dos exercícios nas diferentes linguagens propostas, optei por configurar um **ambiente de desenvolvimento local completo** em uma máquina **Linux (Ubuntu)** para compilar, executar e testar as soluções.

Este repositório serve como um registro detalhado do processo de configuração, dos desafios encontrados (e superados!) em cada linguagem e das soluções implementadas localmente.

## ⚙️ Configuração do Ambiente Local

Para isolar os testes e garantir um ambiente controlado, foram realizadas as seguintes configurações no Linux:

1.  **Usuário Dedicado:** Criação do usuário `gus_testes` para execução dos desafios:
    ```bash
    sudo useradd gus_testes -c "Designado para testes" -m -s /bin/bash -p <senha_criptografada>
    ```
2.  **Estrutura de Diretórios:** Organização das soluções dentro do diretório home do usuário `gus_testes`, facilitando a navegação e o versionamento:
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

## ✨ Desafios e Linguagens

Detalhes da configuração, execução e observações para cada linguagem abordada:

---

### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg" alt="Java Logo" width="20" height="20"/> 1. Java

* **Ambiente:** OpenJDK (Instalado via `sudo apt install default-jdk`).
* **Arquivo:** `desafio-java-1/Desafio.java`
* **Compilação:** `javac Desafio.java`
* **Execução:** `java Desafio`
* **Observações:**
    * O nome do arquivo (`Desafio.java`) precisou corresponder exatamente ao nome da classe `public` (`Desafio`).
    * ⚠️ **Locale Issue:** A leitura de `float` com `Scanner.nextFloat()` apresentou `InputMismatchException` ao usar **ponto (`.`)**. Foi necessário usar **vírgula (`,`)** na entrada, devido ao Locale padrão da JVM ser `pt_BR`.

---

### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/csharp/csharp-original.svg" alt="C# Logo" width="20" height="20"/> 2. C# (C Sharp)

* **Ambiente:** .NET SDK 8.0 (Instalado via repositório da Microsoft - [Instruções Oficiais](https://learn.microsoft.com/pt-br/dotnet/core/install/linux-ubuntu) - e `sudo apt install dotnet-sdk-8.0`).
* **Projeto:** Criado com `dotnet new console` no diretório `desafio-csharp-1/`.
* **Arquivo Principal:** `Program.cs`
* **Execução:** `dotnet run` (compila e executa).
* **Observações:**
    * Corrigidos erros de sintaxe (operador `$$` -> `&&`) e de tipo de dados (uso de strings `"0.05F"` em vez de literais float `0.05f`).
    * ✅ Para garantir consistência na leitura/escrita de decimais usando **ponto (`.`)** independentemente do locale do sistema, foi utilizado `CultureInfo.InvariantCulture`.

---

### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" alt="JavaScript Logo" width="20" height="20"/> 3. JavaScript (Node.js)

* **Ambiente:** Node.js e NPM (Instalados via `sudo apt install nodejs npm`). Verificado com `node -v`.
* **Arquivo:** `desafio-javascript-1/desafio_java-script.js`
* **Execução:** `node desafio_java-script.js`
* **Observações:**
    * Funções específicas de plataforma (`gets()`, `print()`) foram substituídas pelas padrões do Node.js (`console.log()` e leitura via módulo `readline`).
    * ⚠️ A leitura inicial via `fs.readFileSync('/dev/stdin')` causou erro de permissão (`EACCES`). A solução foi usar o módulo **`readline`** para entrada interativa.
    * Corrigidos erros de *case* (`Let` -> `let`, `tofixed` -> `toFixed`).

---

### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" alt="Python Logo" width="20" height="20"/> 4. Python

* **Ambiente:** Python 3 (pré-instalado no sistema). Verificado com `python3 --version`.
* **Arquivo:** `desafio-python-1/desafio_python.py`
* **Execução:** `python3 desafio_python.py`
* **Observações:**
    * 🐛 Corrigido `TabError` causado pela mistura de tabs e espaços na indentação (padronizado para **4 espaços** por nível).
    * Leitura (`input()`) e conversão (`float()`) funcionaram diretamente (esperando **ponto (`.`)** para decimais). Saída formatada com f-strings (`f"{saida:.2f}"`).

---

### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kotlin/kotlin-original.svg" alt="Kotlin Logo" width="20" height="20"/> 5. Kotlin

* **Ambiente:** Compilador Kotlin (Instalado via `sudo apt install kotlin`), rodando sobre a JVM (Java JDK). Verificado com `kotlinc -version`.
* **Arquivo:** `desafio-kotlin-1/desafio_kotlin.kt`
* **Compilação:** `kotlinc desafio_kotlin.kt -include-runtime -d desafio_kotlin.jar` (JAR auto-contido).
* **Execução:** `java -jar desafio_kotlin.jar`
* **Observações:**
    * Utilizada a função `readln()` para leitura e `.toFloat()` para conversão (esperando **ponto (`.`)**).
    * Saída formatada com `println("%.2f".format(saida))`.

---

## 🛠️ Como Executar Localmente (Geral)

1.  Clone este repositório: `git clone <URL_DO_REPOSITORIO>`
2.  Certifique-se de ter as **dependências de linguagem** instaladas no seu ambiente Linux (Java JDK, .NET SDK, Node.js, Python 3, Kotlin Compiler).
3.  Navegue até o subdiretório do desafio desejado em `Scripts/` (ex: `cd Scripts/desafio-java-1`).
4.  Siga as instruções de **compilação** (se aplicável - Java, Kotlin) e **execução** específicas de cada linguagem (detalhadas acima).
5.  Forneça a **entrada** via terminal quando solicitado (interativamente ou via pipe `|`, lembrando das particularidades de ponto/vírgula de cada linguagem/configuração).

## 🐙 Versionamento

Este projeto utiliza **Git** para controle de versão. O histórico de commits reflete a adição de cada solução e a refatoração da estrutura de diretórios para melhor organização. O código está hospedado no **GitHub**.

---
*Documentação gerada e refinada com auxílio e revisão do Gemini 2.5 Pro (experimental). Última atualização: 26/04/2025.*
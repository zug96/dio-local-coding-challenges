# 🚀 Desafios de Código e Projetos DIO - Ambiente Local

Bem-vindo! Este repositório documenta a jornada e as soluções para os **Desafios de Código** da seção "A Linguagem é Só Um Detalhe..." e um **Projeto Paralelo de Automação**, ambos desenvolvidos durante o bootcamp da DIO em um ambiente **Linux (Ubuntu)** configurado localmente.

## ✨ Desafios de Código ("A Linguagem é Só Um Detalhe...")

*Localização no Repositório:* `Scripts/`

Esta seção detalha a configuração do ambiente local e as soluções para os desafios de lógica propostos no curso, cobrindo 5 linguagens diferentes.

### 🤔 Contexto e Motivação

Durante o acompanhamento das aulas em vídeo, o ambiente de execução online apresentado nas videoaulas não estava acessível para a realização destes desafios específicos (apenas o desafio "Associando Comandos CLI" estava disponível). Para contornar essa limitação e garantir a prática, foi configurado um ambiente de desenvolvimento local.

### ⚙️ Configuração do Ambiente Local (Para os Desafios)

1.  **Usuário Dedicado:** Foi criado o usuário `gus_testes` para isolar os testes:
    ```bash
    sudo useradd gus_testes -c "Designado para testes" -m -s /bin/bash -p <senha_criptografada>
    ```
2.  **Estrutura de Diretórios:** As soluções foram organizadas em subdiretórios dentro de `~/Desafios-de-Codigo_DIO/Scripts/`:
    ```
    Scripts/
    ├── desafio-java-1/
    ├── desafio-csharp-1/
    ├── desafio-javascript-1/
    ├── desafio-python-1/
    └── desafio-kotlin-1/
    ```
3.  **Instalação das Linguagens:** As ferramentas necessárias (JDK, .NET SDK, Node.js, Kotlin Compiler) foram instaladas via `apt`, conforme detalhado em cada seção abaixo. Python 3 já estava presente.

### Soluções por Linguagem:

---

#### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg" alt="Java Logo" width="20" height="20"/> 1. Java

* **Ambiente:** OpenJDK (Instalado via `sudo apt install default-jdk`).
* **Arquivo:** `Scripts/desafio-java-1/Desafio.java`
* **Compilação:** `javac Desafio.java`
* **Execução:** `java Desafio`
* **Observações:**
    * O nome do arquivo (`Desafio.java`) precisou corresponder exatamente ao nome da classe `public` (`Desafio`).
    * ⚠️ **Locale Issue:** A leitura de `float` com `Scanner.nextFloat()` apresentou `InputMismatchException` ao usar **ponto (`.`)**. Foi necessário usar **vírgula (`,`)** na entrada, devido ao Locale padrão da JVM ser `pt_BR`. A saída formatada com `String.format("%.2f", ...)` também usou vírgula.

---

#### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/csharp/csharp-original.svg" alt="C# Logo" width="20" height="20"/> 2. C# (C Sharp)

* **Ambiente:** .NET SDK 8.0 (Instalado via repositório da Microsoft - [Instruções Oficiais](https://learn.microsoft.com/pt-br/dotnet/core/install/linux-ubuntu) - e `sudo apt install dotnet-sdk-8.0`).
* **Projeto:** `Scripts/desafio-csharp-1/` (Criado com `dotnet new console`).
* **Arquivo Principal:** `Program.cs` (classe interna renomeada para `Desafio` no código, mas arquivo mantido como `Program.cs`).
* **Execução:** `dotnet run` (compila e executa).
* **Observações:**
    * Corrigidos erros de sintaxe (operador `$$` -> `&&`) e de tipo de dados (uso de strings `"0.05F"` em vez de literais float `0.05f`).
    * ✅ Para garantir consistência na leitura/escrita de decimais usando **ponto (`.`)** independentemente do locale do sistema, foi utilizado `CultureInfo.InvariantCulture`.

---

#### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" alt="JavaScript Logo" width="20" height="20"/> 3. JavaScript (Node.js)

* **Ambiente:** Node.js e NPM (Instalados via `sudo apt install nodejs npm`). Verificado com `node -v`.
* **Arquivo:** `Scripts/desafio-javascript-1/desafio_java-script.js`
* **Execução:** `node desafio_java-script.js`
* **Observações:**
    * Funções específicas de plataforma (`gets()`, `print()`) foram substituídas pelas padrões do Node.js (`console.log` e módulo `readline`).
    * ⚠️ A leitura inicial via `fs.readFileSync('/dev/stdin')` causou erro de permissão (`EACCES`). Resolvido usando o módulo **`readline`** para entrada interativa.
    * Corrigidos erros de *case* (`Let` -> `let`, `tofixed` -> `toFixed`).

---

#### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" alt="Python Logo" width="20" height="20"/> 4. Python

* **Ambiente:** Python 3 (pré-instalado). Verificado com `python3 --version`.
* **Arquivo:** `Scripts/desafio-python-1/desafio_python.py`
* **Execução:** `python3 desafio_python.py`
* **Observações:**
    * 🐛 Corrigido `TabError` (indentação inconsistente) padronizando para **4 espaços** por nível.
    * Leitura (`input()`) e conversão (`float()`) funcionaram diretamente (esperando **ponto (`.`)** para decimais). Saída formatada com f-strings (`f"{saida:.2f}`) usou ponto.

---

#### <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kotlin/kotlin-original.svg" alt="Kotlin Logo" width="20" height="20"/> 5. Kotlin

* **Ambiente:** Compilador Kotlin (`sudo apt install kotlin`), rodando sobre JVM (Java JDK). Verificado com `kotlinc -version`.
* **Arquivo:** `Scripts/desafio-kotlin-1/desafio_kotlin.kt`
* **Compilação:** `kotlinc desafio_kotlin.kt -include-runtime -d desafio_kotlin.jar` (JAR auto-contido).
* **Execução:** `java -jar desafio_kotlin.jar`
* **Observações:**
    * Leitura com `readln()` e conversão `.toFloat()` (esperando **ponto (`.`)**).
    * Saída formatada com `println("%.2f".format(saida))` usou separador decimal do Locale (`pt_BR` -> vírgula).

---

## 🌟 Projeto Paralelo: Gerador Automatizado de Relatório de Vendas

*Localização no Repositório:* `Projetos/AutomatedSalesReport/`

Este projeto foi desenvolvido para consolidar conhecimentos dos Módulos 1 e 2 (Linux, Git, Scripting) e aplicar o interesse em Python para automação.

**Objetivo:** Automatizar o processamento de arquivos `.csv` de vendas, gerar relatórios diários em Markdown e organizar os arquivos no sistema Linux.

**Status Atual:**
* ✅ Implementação inicial em **Python** (`python/process_sales.py`) concluída e testada.
* ✅ Ambiente Linux configurado com diretórios (`/opt/sales_data/*`, `/var/reports/sales`) e grupo (`sales_managers`).
* ✅ Permissões ajustadas com `setgid` e `chgrp` via script para garantir herança/posse correta do grupo `sales_managers`.

**Plano Futuro:**
* [ ] Reimplementar a mesma lógica em **Node.js** (diretório `nodejs/`).
* [ ] Reimplementar a mesma lógica em **Kotlin** (diretório `kotlin/`).

**Setup e Execução (Versão Python):**
1.  **Configurar Ambiente Linux:** (Necessário apenas uma vez, requer `sudo`)
    ```bash
    sudo groupadd sales_managers
    sudo usermod -aG sales_managers gus_testes # Ou seu usuário de execução
    sudo mkdir -p /opt/sales_data/incoming /opt/sales_data/processed /var/reports/sales
    sudo chown root:sales_managers /var/reports/sales && sudo chmod 2770 /var/reports/sales
    sudo chown gus_testes:sales_managers /opt/sales_data/* && sudo chmod 2775 /opt/sales_data/*
    ```
2.  **Executar:** (Como `gus_testes`)
    ```bash
    # Coloque arquivos .csv (Timestamp,ProductID,StoreID,Quantity,UnitPrice) em /opt/sales_data/incoming/
    # Ex: cp Projetos/AutomatedSalesReport/python/sample_sales.csv /opt/sales_data/incoming/
    python3 ./Projetos/AutomatedSalesReport/python/process_sales.py 
    # Verifique relatórios .md em /var/reports/sales/
    # Verifique arquivos .csv movidos (com grupo 'sales_managers') em /opt/sales_data/processed/
    ```
*(Para detalhes da lógica, veja o código comentado em `Projetos/AutomatedSalesReport/python/process_sales.py`)*

---
*Este projeto paralelo foi desenvolvido como parte do bootcamp DIO e contou com a **colaboração ativa e orientação da IA Gemini (Google)**, que auxiliou na definição do escopo, detalhamento das etapas, fornecimento de códigos e depuração.*
---

## 🛠️ Como Executar Localmente (Geral)

1.  Clone este repositório: `git clone <URL_DO_REPOSITORIO>`
2.  Certifique-se de ter as **dependências de linguagem** instaladas no seu ambiente Linux (Java JDK, .NET SDK, Node.js, Python 3, Kotlin Compiler).
3.  Navegue até o subdiretório do desafio ou projeto desejado.
4.  Siga as instruções de **compilação** (se aplicável) e **execução** específicas.
5.  Forneça a **entrada** via terminal quando solicitado.

## 🐙 Versionamento

Este projeto utiliza **Git** para controle de versão. O histórico de commits reflete a adição de cada solução, a criação/evolução do projeto paralelo e a atualização desta documentação. O código está hospedado no **GitHub**.

---
*Documentação gerada e refinada com auxílio e revisão. Última atualização: 27/04/2025.*
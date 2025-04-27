#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import datetime
import shutil
import subprocess # <--- LINHA ADICIONADA AQUI!

# --- Constantes de Configuração ---
INCOMING_DIR = "/opt/sales_data/incoming"
PROCESSED_DIR = "/opt/sales_data/processed"
REPORTS_DIR = "/var/reports/sales"

def process_csv_file(filepath):
    """
    Processa um único arquivo CSV de vendas.
    Lê o arquivo, calcula métricas e retorna um dicionário com os resultados.
    Retorna None se houver erro ou o arquivo estiver vazio.
    """
    filename = os.path.basename(filepath) # Pega apenas o nome do arquivo
    print(f"-> Processando arquivo: {filename}")
    total_revenue = 0.0
    total_quantity = 0
    transactions = 0
    product_ids = set() # Usaremos um set para contar produtos únicos facilmente
    
    try:
        # Abre o arquivo CSV para leitura
        with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            try:
                # Tenta ler o cabeçalho para ignorá-lo
                header = next(reader) 
                print(f"   Cabeçalho ignorado: {header}") 
            except StopIteration:
                # Arquivo está vazio ou não tem nem cabeçalho
                print(f"   AVISO: Arquivo CSV '{filename}' vazio ou sem cabeçalho.")
                return None # Pula este arquivo
                
            # Itera sobre as linhas restantes do CSV
            for i, row in enumerate(reader, 1): # Começa a contar linhas do 1 (após cabeçalho)
                try:
                    # Verifica se a linha tem o número esperado de colunas (5)
                    if len(row) == 5:
                        # Extrai os dados da linha
                        _timestamp_str, product_id, _store_id, quantity_str, unit_price_str = row
                        
                        # Converte quantidade e preço para números (float aceita ponto ou vírgula)
                        quantity = int(quantity_str.strip())
                        # Substitui vírgula por ponto ANTES de converter para float
                        unit_price = float(unit_price_str.strip().replace(',', '.')) 
                        
                        # Atualiza as métricas
                        total_revenue += quantity * unit_price
                        total_quantity += quantity
                        transactions += 1
                        product_ids.add(product_id.strip()) # Adiciona ID do produto ao set
                        
                    else:
                        # Avisa se uma linha tem formato inesperado
                        print(f"   AVISO: Linha {i+1} ignorada em '{filename}' - número incorreto de colunas: {len(row)}")
                        
                except ValueError as e:
                    # Avisa se houve erro na conversão de número na linha
                    print(f"   AVISO: Linha {i+1} ignorada em '{filename}' - erro ao converter número: {e} -> {row}")
                except Exception as e:
                    # Captura outros erros inesperados na linha
                    print(f"   ERRO inesperado processando linha {i+1} em '{filename}': {e} -> {row}")

        # Após ler todas as linhas, monta o dicionário de métricas
        metrics = {
            "total_revenue": total_revenue,
            "total_quantity": total_quantity,
            "transactions": transactions,
            "unique_products": len(product_ids) # Tamanho do set = nº de itens únicos
        }
        print(f"   Processamento de '{filename}' concluído.")
        return metrics

    except FileNotFoundError:
        print(f"   ERRO CRÍTICO: Arquivo não encontrado durante processamento: {filepath}")
        return None
    except Exception as e:
        # Captura erros ao abrir ou ler o arquivo
        print(f"   ERRO CRÍTICO ao abrir ou ler o arquivo '{filename}': {e}")
        return None

def generate_report(filename, metrics):
    """Gera o conteúdo do relatório em formato Markdown."""
    now = datetime.datetime.now()
    # Formata o conteúdo do relatório usando f-string e Markdown
    report_content = f"""# Relatório de Vendas Processado

- **Data/Hora do Processamento:** {now.strftime('%Y-%m-%d %H:%M:%S')}
- **Arquivo Processado:** `{filename}`

## Métricas Calculadas:

- **Receita Total:** R$ {metrics['total_revenue']:.2f}
- **Quantidade Total de Itens Vendidos:** {metrics['total_quantity']}
- **Número de Transações:** {metrics['transactions']}
- **Número de Produtos Únicos Vendidos:** {metrics['unique_products']}

---
*Relatório gerado automaticamente pelo script process_sales.py.*
"""
    return report_content

def main():
    """Função principal que orquestra o processo."""
    print("==================================================")
    print(f"Iniciando script de processamento de vendas - {datetime.datetime.now()}")
    print(f"Verificando diretório de entrada: {INCOMING_DIR}")
    print("==================================================")

    processed_count = 0
    error_count = 0 # Mudança aqui para inicializar error_count

    try:
        # Lista todos os arquivos no diretório de entrada
        all_files = os.listdir(INCOMING_DIR)
        # Filtra apenas os que terminam com .csv (ignorando case)
        files_to_process = [f for f in all_files if f.lower().endswith('.csv')]
        
        if not files_to_process:
            print("Nenhum arquivo .csv encontrado para processar.")
            print("Script concluído.")
            return

        print(f"Arquivos .csv encontrados: {files_to_process}")

        # Itera sobre cada arquivo CSV encontrado
        for filename in files_to_process:
            filepath = os.path.join(INCOMING_DIR, filename)
            
            # 1. Processar o arquivo CSV para obter métricas
            metrics = process_csv_file(filepath)

            # Se o processamento foi bem-sucedido (retornou métricas)
            if metrics:
                # 2. Gerar o conteúdo do relatório
                report_content = generate_report(filename, metrics)
                
                # 3. Definir nome e caminho do arquivo de relatório
                # Remove '.csv' e adiciona data/hora para nome único
                base_report_name = filename[:-4] if filename.lower().endswith('.csv') else filename
                report_filename = f"Relatorio_{base_report_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
                report_filepath = os.path.join(REPORTS_DIR, report_filename)
                
                # 4. Salvar o relatório no diretório de relatórios
                try:
                    with open(report_filepath, 'w', encoding='utf-8') as report_file:
                        report_file.write(report_content)
                    print(f"   Relatório salvo com sucesso em: {report_filepath}")

                    # 5. Mover arquivo CSV processado para o diretório de processados
                    processed_filepath = os.path.join(PROCESSED_DIR, filename)
                    try:
                        shutil.move(filepath, processed_filepath)
                        print(f"   Arquivo '{filename}' movido para: {processed_filepath}")
                        
                        # ----> TENTAR ALTERAR O GRUPO APÓS MOVER <----
                        try:
                            # Tenta mudar o grupo do arquivo movido para 'sales_managers'
                            subprocess.run(['chgrp', 'sales_managers', processed_filepath], check=True, capture_output=True)
                            print(f"   Grupo do arquivo '{filename}' alterado para 'sales_managers'.")
                        except subprocess.CalledProcessError as chgrp_err:
                            print(f"   AVISO: Falha ao executar chgrp no arquivo movido '{filename}'. Erro: {chgrp_err.stderr.decode()}")
                        except FileNotFoundError:
                             print(f"   AVISO: Comando 'chgrp' não encontrado para alterar grupo do arquivo movido.")
                        except Exception as chgrp_e:
                            print(f"   AVISO: Erro inesperado ao tentar alterar grupo do arquivo movido '{filename}': {chgrp_e}")
                        # ----> FIM DA ALTERAÇÃO DE GRUPO <----

                        processed_count += 1 # Incrementa SÓ se moveu E tentou chgrp (mesmo que chgrp falhe)
                        
                    except Exception as e:
                        print(f"   ERRO ao mover arquivo '{filename}' para '{PROCESSED_DIR}': {e}")
                        error_count += 1 # Conta erro se falhar ao mover
                        
                except IOError as e:
                    # Erro ao tentar escrever o arquivo de relatório (ex: permissão?)
                    print(f"   ERRO CRÍTICO ao salvar relatório '{report_filepath}': {e}")
                    print(f"   O arquivo CSV '{filename}' NÃO será movido.")
                    error_count += 1
                except Exception as e:
                     # Outro erro inesperado ao salvar/mover
                     print(f"   ERRO inesperado ao salvar relatório ou mover arquivo '{filename}': {e}")
                     error_count += 1
            else:
                # Arquivo não pôde ser processado (vazio, erro de leitura, etc.)
                print(f"   Arquivo '{filename}' não pôde ser processado ou retornou vazio.")
                error_count += 1 # Conta como erro

    except FileNotFoundError:
         # Erro grave se o diretório de entrada não existe
         print(f"ERRO CRÍTICO: Diretório de entrada '{INCOMING_DIR}' não encontrado.")
         # error_count += 1 # Talvez não contar aqui, pois nenhum arquivo foi processado
    except PermissionError:
         # Erro grave de permissão
         print(f"ERRO CRÍTICO: Sem permissão para ler de '{INCOMING_DIR}' ou escrever em '{REPORTS_DIR}'/'{PROCESSED_DIR}'. Verifique as permissões do usuário '{os.getlogin()}'.")
         # error_count += 1
    except Exception as e:
        # Captura qualquer outro erro inesperado no loop principal
        print(f"ERRO CRÍTICO inesperado no processo principal: {e}")
        # error_count += 1
        
    # Imprime um resumo final da execução
    print("==================================================")
    print(f"Processamento concluído.")
    # Ajuste na contagem final para refletir melhor o status
    total_files_attempted = len(files_to_process) if 'files_to_process' in locals() else 0
    print(f"Total de arquivos .csv encontrados: {total_files_attempted}")
    print(f"Arquivos movidos com sucesso para processados: {processed_count}")
    print(f"Arquivos que geraram relatório mas podem ter tido erro ao mover/chgrp ou erro inicial: {error_count}")
    print(f"Arquivos não processados (vazios/erro leitura inicial): {total_files_attempted - processed_count - error_count}")
    print("==================================================")


# Garante que a função main() seja chamada apenas quando o script é executado diretamente
if __name__ == "__main__":
    main()

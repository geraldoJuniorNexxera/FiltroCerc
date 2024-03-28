import os
import pandas as pd
from datetime import datetime
from verificador import verificar_ancora  # Assegure que verificador.py esteja acessível
import xlwt  # Para escrita de arquivos .xls, para .xlsx considere usar openpyxl

def filtraCerc():
    pasta_teste = 'C:/Users/geraldo.junior/Desktop/ColarCERC'
    arquivos_na_pasta = os.listdir(pasta_teste)
    arquivos_excel = [arquivo for arquivo in arquivos_na_pasta if arquivo.endswith(('.xls', '.xlsx'))]

    if not arquivos_excel:
        print("Nenhum arquivo .xls ou .xlsx encontrado na pasta especificada.")
        return

    somas_combinadas = {}
    linhas_processadas = 0

    for arquivo in arquivos_excel:
        caminho_arquivo = os.path.join(pasta_teste, arquivo)
        try:
            df = pd.read_excel(caminho_arquivo)  # Usa pandas para ler tanto .xls quanto .xlsx
            for index, row in df.iterrows():
                cnpj_loja = str(int(row[0])) if isinstance(row[0], float) else str(row[0]).strip()

                nome_empresa = verificar_ancora(cnpj_loja)
                
                valor_raw = row[13]
                data_raw = str(row[15])[:10]
                try:
                    data_operacao = datetime.strptime(data_raw.strip(), '%Y-%m-%d').strftime('%d/%m/%Y')
                    valor_operacao = float(valor_raw)
                    chave = f"{nome_empresa}-{data_operacao}"
                    somas_combinadas[chave] = somas_combinadas.get(chave, 0) + valor_operacao
                    linhas_processadas += 1
                except ValueError as e:
                    print(f"Erro ao processar linha {index + 1} do arquivo {arquivo}: {e}")
        except Exception as e:  # Captura uma gama mais ampla de exceções para fins de depuração
            print(f"Erro ao abrir/processar o arquivo: {caminho_arquivo} - {e}")

    if linhas_processadas == 0:
        print("Nenhuma linha foi processada. Verifique o formato dos dados.")
    else:
        print(f"{linhas_processadas} linhas foram processadas.")

    # Cria a nova planilha e adiciona os dados
    nova_planilha = xlwt.Workbook()
    nova_planilha_aba = nova_planilha.add_sheet('Operações CERC')
    nova_planilha_aba.write(0, 0, 'Nome da Empresa')
    nova_planilha_aba.write(0, 1, 'Data')
    nova_planilha_aba.write(0, 2, 'Valor Operação')
    linha = 1
    for chave, soma in sorted(somas_combinadas.items()):
        nome_empresa, data_operacao = chave.split('-', 1)
        nova_planilha_aba.write(linha, 0, nome_empresa)
        nova_planilha_aba.write(linha, 1, data_operacao)
        nova_planilha_aba.write(linha, 2, soma)
        linha += 1

    data_atual = datetime.now().strftime("%d%m%Y")
    caminho_nova_planilha = os.path.join(pasta_teste, f'Resumo_CERC_{data_atual}.xls')
    nova_planilha.save(caminho_nova_planilha)

filtraCerc()

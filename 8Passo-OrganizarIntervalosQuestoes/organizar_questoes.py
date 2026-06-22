import os
import shutil

# Definição dos caminhos de origem (Passo 7) e destino (Passo 8)
PASSO7_DIR = os.path.abspath("../7Passo-DividirPelaFaixaAzul")
PASSO8_DIR = os.path.abspath(".")

# Caminhos específicos das subpastas do Passo 7
questoes_colunas_origem = os.path.join(PASSO7_DIR, "questoes_colunas")
pagina_15_origem = os.path.join(PASSO7_DIR, "pagina_15")
pagina_28_origem = os.path.join(PASSO7_DIR, "pagina_28")

def criar_pasta_e_mover(imagens, pasta_destino_nome, pasta_origem_path):
    """Cria a pasta no Passo 8 e move a lista de imagens especificadas."""
    pasta_destino_path = os.path.join(PASSO8_DIR, pasta_destino_nome)
    os.makedirs(pasta_destino_path, exist_ok=True)
    
    for img in imagens:
        origem = os.path.join(pasta_origem_path, img)
        destino = os.path.join(pasta_destino_path, img)
        if os.path.exists(origem):
            shutil.move(origem, destino)
            print(f"Movido: {img} -> {pasta_destino_nome}/")

def executar_organizacao():
    print("Iniciando a organização do Passo 8...")

    # --- 1. Processamento da pasta 'questoes_colunas' ---
    if os.path.exists(questoes_colunas_origem):
        # 1.1 Excluir lixo (parte_001.png)
        lixo_colunas = os.path.join(questoes_colunas_origem, "parte_001.png")
        if os.path.exists(lixo_colunas):
            os.remove(lixo_colunas)
            print("Excluído lixo: questoes_colunas/parte_001.png")

        # 1.2 Intervalo 1-5-ingles (parte_002.png até parte_006.png)
        imgs_ingles = [f"parte_{i:03d}.png" for i in range(2, 7)]
        criar_pasta_e_mover(imgs_ingles, "1-5-ingles", questoes_colunas_origem)

        # 1.3 Intervalo 1-5-espanhol (parte_007.png até parte_011.png)
        imgs_espanhol = [f"parte_{i:03d}.png" for i in range(7, 12)]
        criar_pasta_e_mover(imgs_espanhol, "1-5-espanhol", questoes_colunas_origem)

        # 1.4 Intervalo 6-34 (parte_012.png até parte_040.png)
        imgs_6_34 = [f"parte_{i:03d}.png" for i in range(12, 41)]
        criar_pasta_e_mover(imgs_6_34, "6-34", questoes_colunas_origem)

        # 1.5 Intervalo 37-76 (parte_041.png até parte_080.png)
        imgs_37_76 = [f"parte_{i:03d}.png" for i in range(41, 81)]
        criar_pasta_e_mover(imgs_37_76, "37-76", questoes_colunas_origem)

    # --- 2. Processamento da pasta 'pagina_15' ---
    if os.path.exists(pagina_15_origem):
        # 2.1 Excluir lixo (parte_001.png)
        lixo_p15 = os.path.join(pagina_15_origem, "parte_001.png")
        if os.path.exists(lixo_p15):
            os.remove(lixo_p15)
            print("Excluído lixo: pagina_15/parte_001.png")
        
        # 2.2 Renomear pasta para 35-36 e trazer para o Passo 8
        imgs_35_36 = [f"parte_{i:03d}.png" for i in range(2, 4)]
        criar_pasta_e_mover(imgs_35_36, "35-36", pagina_15_origem)

    # --- 3. Processamento da pasta 'pagina_28' ---
    if os.path.exists(pagina_28_origem):
        # 3.1 Excluir lixo (parte_001.png)
        lixo_p28 = os.path.join(pagina_28_origem, "parte_001.png")
        if os.path.exists(lixo_p28):
            os.remove(lixo_p28)
            print("Excluído lixo: pagina_28/parte_001.png")
        
        # 3.2 Renomear pasta para 77-79 e trazer para o Passo 8
        imgs_77_79 = [f"parte_{i:03d}.png" for i in range(2, 5)]
        criar_pasta_e_mover(imgs_77_79, "77-79", pagina_28_origem)

    # --- 4. Processamento das sobras de 'questoes_colunas' (Intervalo 80-90) ---
    if os.path.exists(questoes_colunas_origem):
        # Move o restante das imagens (parte_081.png até parte_091.png) para a pasta 80-90
        imgs_80_90 = [f"parte_{i:03d}.png" for i in range(81, 92)]
        criar_pasta_e_mover(imgs_80_90, "80-90", questoes_colunas_origem)

    print("Organização concluída com sucesso!")

if __name__ == "__main__":
    executar_organizacao()

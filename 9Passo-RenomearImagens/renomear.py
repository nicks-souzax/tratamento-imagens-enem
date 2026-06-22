import os
import shutil

# Definicao dos caminhos base (Lendo do Passo 8 e salvando no Passo 9)
PASSO8_DIR = os.path.abspath("../8Passo-OrganizarIntervalosQuestoes")
PASSO9_DIR = os.path.abspath(".")

print("Iniciando copia e renomeacao das questoes do Passo 8 para o Passo 9...")

# Mapeamento de cada pasta do Passo 8 com suas regras de renomeacao
configuracao_pastas = {
    "1-5-ingles": (2, 6, -1, "-ingles"),       # parte_002 -> questao-1-ingles
    "1-5-espanhol": (7, 11, -6, "-espanhol"),  # parte_007 -> questao-1-espanhol
    "6-34": (12, 40, -6, ""),                 # parte_012 -> questao-6
    "35-36": (2, 3, 33, ""),                  # parte_002 -> questao-35
    "37-76": (41, 80, -4, ""),                 # parte_041 -> questao-37
    "77-79": (2, 4, 75, ""),                  # parte_002 -> questao-77
    "80-90": (81, 91, -1, "")                  # parte_081 -> questao-80
}

# Percorre cada pasta configurada
for pasta, (inicio, fim, ajuste, sufixo) in configuracao_pastas.items():
    origem_pasta_path = os.path.join(PASSO8_DIR, pasta)
    destino_pasta_path = os.path.join(PASSO9_DIR, pasta)
    
    # Verifica se a pasta existe no Passo 8 antes de tentar ler
    if os.path.exists(origem_pasta_path):
        os.makedirs(destino_pasta_path, exist_ok=True)
        
        for i in range(inicio, fim + 1):
            arq_antigo = f"parte_{i:03d}.png"
            caminho_antigo = os.path.join(origem_pasta_path, arq_antigo)
            
            if os.path.exists(caminho_antigo):
                num_questao = i + ajuste
                arq_novo = f"questao-{num_questao}{sufixo}.png"
                caminho_novo = os.path.join(destino_pasta_path, arq_novo)
                
                # Copia o arquivo renomeando para a pasta do Passo 9
                shutil.copy(caminho_antigo, caminho_novo)
                print(f"[OK] {pasta}: {arq_antigo} -> {arq_novo}")
    else:
        print(f"Alerta: A pasta '{pasta}' nao foi encontrada no Passo 8.")

print("Passo 9 executado com sucesso completo!")

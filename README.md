# 🕒 DocReadTime

DocReadTime é uma ferramenta desenvolvida em Python para calcular o tempo estimado de leitura de arquivos `.docx`. Usando uma interface gráfica simples, construída com Tkinter, o usuário pode facilmente selecionar uma pasta e processar todos os documentos contidos nela, obtendo uma estimativa de tempo de leitura baseada no número de palavras.

## 🚀 Funcionalidades

- **Interface gráfica amigável**: Utiliza Tkinter para criar uma GUI intuitiva, permitindo a fácil seleção de pastas e execução do script.
- **Cálculo do tempo de leitura**: Processa arquivos `.docx` e calcula o tempo estimado de leitura com base em uma média de 130 palavras por minuto.
- **Exportação de resultados**: Gera um arquivo de texto (`resultado.txt`) com o tempo de leitura estimado para cada documento processado.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter** (para a interface gráfica)
- **docx2txt** (para extração de texto de arquivos `.docx`)

## 📄 Como Usar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/AnubisChacal/PyTaskFlow
    ```

2. **Instale as dependências**:
    ```bash
    pip install docx2txt
    ```

3. **Execute o script**:
   - Execute o script `Tempo_de_leitura-V1.0.py` para iniciar a aplicação.
   - Insira o caminho da pasta contendo os arquivos `.docx` e clique em "Executar" para obter os tempos de leitura.

## 🌟 Exemplos de Uso

O DocReadTime é ideal para professores, editores ou qualquer pessoa que precise estimar o tempo necessário para ler uma série de documentos. A ferramenta oferece uma maneira rápida e eficiente de gerar estimativas, permitindo uma melhor gestão do tempo.


# Processador de Logs VPC com Classificação por IA

## Descrição

Este projeto é um estudo aprofundado e implementação prática para processamento de logs de Virtual Private Cloud (VPC) da Amazon, utilizando modelos avançados de classificação de inteligência artificial (IA). O objetivo principal é analisar e classificar logs de VPC para identificar padrões, anomalias e possíveis ameaças de segurança, facilitando uma gestão de rede mais eficaz e segura.

## Características do Modelo de IA

O modelo de Inteligência Artificial descrito neste documento foi treinado utilizando quatro algoritmos de classificação distintos e eficientes:

1. **K-Nearest Neighbors (KNN):** Um método baseado em instâncias que classifica novos casos com base na similaridade (e.g., distância de funções) com casos conhecidos.

2. **Regressão Logística:** Modelo estatístico usado para classificação, empregando uma função logística para modelar uma variável binária de saída.

3. **Máquinas de Vetores de Suporte (SVM):** Busca encontrar um hiperplano em um espaço N-dimensional (N = número de características) para classificar distintamente os pontos de dados.

4. **Random Forest:** Método de ensemble que constrói várias árvores de decisão durante o treinamento e produz a classe que é o modo das classes das árvores individuais.

A eficácia de cada um destes algoritmos foi avaliada comparativamente, e os resultados são essenciais para entender a performance do modelo. Conforme ilustrado na figura abaixo, o algoritmo Random Forest apresentou o melhor desempenho. Sua capacidade de gerar um modelo robusto e preciso, especialmente em grandes conjuntos de dados com múltiplas variáveis de entrada, é notável.

### Figura: Comparativo de Desempenho dos Algoritmos de Classificação
![image](https://github.com/RenanAlcolea/HackatonIA/assets/19910963/28053cac-18f0-48ed-a090-331785571df9)

## Tecnologias Utilizadas

- Linguagens: Python, Powershell
- Frameworks e Bibliotecas: Pandas, Numpy, Scikit-Learn, Seanborn, MatplotLib, Imbalanced-Learn
- Serviços AWS: Amazon VPC, Amazon S3, AWS CloudWatch, AWS IAM

## Instalação e Uso

1. Clone o repositório:
git clone https://github.com/RenanAlcolea/HackatonIA.git

3. Navegue até a pasta do projeto e instale as dependências:
cd HackatonIA
pip install -r requirements.tx

4. Configure suas credenciais AWS e variáveis de ambiente.

5. Execute o aplicativo:
python main.py

## Contribuições

Contribuições são sempre bem-vindas! Se você tem uma ideia ou sugestão, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

- Nome do Desenvolvedor: Renan Alcoléa
- LinkedIn: https://www.linkedin.com/in/renan-alcolea/)https://www.linkedin.com/in/renan-alcolea/


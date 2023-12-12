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

### Análise de Valores de K no KNN

No processo de treinamento do modelo de Inteligência Artificial, foi conduzida uma análise para determinar o valor ótimo de K no algoritmo K-Nearest Neighbors (KNN). Esta análise consistiu na comparação do desempenho do modelo com diferentes valores de K, variando de 1 a 10.

Os resultados indicaram que um valor de K igual a 1 demonstrou ser o mais eficiente, proporcionando maior precisão na classificação dos dados de log da VPC. Esse achado foi fundamental para a progressão do modelo, levando à inclusão do KNN com K = 1 na tabela comparativa de desempenho juntamente com outros algoritmos de classificação. A seleção desse valor de K se destacou pela sua capacidade de manejar eficientemente as complexidades e particularidades dos dados de VPC analisados.

### Figura 01: Comparativo de Desempenho de K no KNN
![image](https://github.com/RenanAlcolea/HackatonIA/assets/19910963/6e64cda1-3f46-4dd4-91d6-841bc15ee6a3)

### Figura 02: Comparativo de Desempenho dos Algoritmos de Classificação
![image](https://github.com/RenanAlcolea/HackatonIA/assets/19910963/28053cac-18f0-48ed-a090-331785571df9)

## Base de Dados Utilizada

Este projeto utilizou a base de dados CIDDS-001, fornecida pela Universidade de Coburg. Para fins de processamento e análise, foram selecionados dois arquivos específicos:

- `CIDDS-001-external-week3.csv`: Representando os dados externos da semana mais movimentada.
- `CIDDS-001-internal-week1.csv`: Representando os dados internos da semana mais movimentada.

Esses arquivos foram escolhidos para fornecer uma visão abrangente tanto das atividades internas quanto externas, capturando uma variedade de padrões e anomalias relevantes para a segurança de redes VPC.

## Tecnologias Utilizadas

- Linguagens: Python, Powershell
- Frameworks e Bibliotecas: Pandas, Numpy, Scikit-Learn, Seanborn, MatplotLib, Imbalanced-Learn
- Serviços AWS: Amazon VPC, Amazon S3, AWS CloudWatch, AWS IAM

## Instalação e Uso

1. Clone o repositório:
git clone https://github.com/RenanAlcolea/HackatonIA.git

2. Navegue até a pasta do projeto e instale as dependências:
cd HackatonIA
pip install -r requirements.txt

3. Configure suas credenciais AWS e variáveis de ambiente.

4. Execute o aplicativo:
python main.py

## Contribuições

Contribuições são sempre bem-vindas! Se você tem uma ideia ou sugestão, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

- Nome do Desenvolvedor: Renan Alcoléa
- LinkedIn: https://www.linkedin.com/in/renan-alcolea/


## Referências

Ring, M., Wunderlich, S., Gruedl, D., Landes, D., Hotho, A.: "Flow-based benchmark data sets for intrusion detection." In: Proceedings of the 16th European Conference on Cyber Warfare and Security (ECCWS), pp. 361-369. ACPI (2017)

Ring, M., Wunderlich, S., Gruedl, D., Landes, D., Hotho, A.: "Creation of Flow-Based Data Sets for Intrusion Detection”. In: Journal of Information Warfare (JIW), Vol. 16, Issue 4, pp. 40-53, 2017


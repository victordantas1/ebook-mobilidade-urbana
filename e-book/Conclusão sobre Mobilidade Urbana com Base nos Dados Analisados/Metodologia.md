
# Metodologia

Este relatório foi elaborado a partir de uma análise rigorosa de dados provenientes de uma pesquisa sobre a mobilidade urbana dos jovens em Manaus. A metodologia adotada visou garantir a fidelidade aos dados e a construção de uma argumentação sólida que conteste a premissa de que os transportes por aplicativo são a solução definitiva para a mobilidade urbana. As etapas seguidas foram as seguintes:

## 1. Coleta e Organização dos Dados

Os dados primários para esta análise foram fornecidos em um arquivo CSV (`mobilidade_urbana.csv`), contendo informações detalhadas sobre os hábitos de mobilidade de 34 jovens de Manaus. Este dataset incluiu variáveis como idade, zona de residência, ocupação, frequência de uso de aplicativos de transporte (Uber/99), comportamento em relação à comparação de preços, percepção sobre o peso do preço e do tempo na escolha do transporte, reação à tarifa dinâmica, frequência de viagens de moto por aplicativo, número de cancelamentos de viagens, satisfação com o transporte público (ônibus), gasto mensal com aplicativos e uso de ferramentas de segurança.

## 2. Processamento e Análise Estatística dos Dados

Para a manipulação e análise dos dados do arquivo CSV, foi utilizada a biblioteca `pandas` do Python, uma ferramenta robusta para análise de dados. As etapas de processamento incluíram:

*   **Carregamento dos Dados:** O arquivo `mobilidade_urbana.csv` foi carregado em um DataFrame do pandas, permitindo a fácil manipulação e acesso às variáveis.
*   **Tratamento de Dados Categóricos:** Variáveis categóricas, como 


 'Viagens/semana (Uber/99)', 'Gasto Mensal (Apps)', 'Viagens Moto (de 10)', e 'Cancelamentos (3 meses)', foram mapeadas para valores numéricos representativos para permitir cálculos e correlações. Por exemplo, categorias de gasto como 'Até R$ 50' foram convertidas para um valor médio representativo (e.g., 25), e faixas de viagens como '1 a 2' foram convertidas para o ponto médio (e.g., 1.5).
*   **Conversão de Tipos de Dados:** Colunas como 'Satisfação Ônibus (1-5)', 'Peso Preço (1-5)' e 'Peso Tempo (1-5)' foram convertidas para o tipo numérico, com tratamento de erros para valores não numéricos, garantindo a integridade dos cálculos.

As análises estatísticas realizadas incluíram:

*   **Estatísticas Descritivas:** Cálculo de médias (e.g., satisfação com o ônibus, peso do preço e tempo, cancelamentos, viagens de moto) para resumir as características principais dos dados.
*   **Análise de Correlação:** Utilização do coeficiente de correlação de Pearson para verificar a relação entre o gasto mensal com aplicativos e a frequência de uso, indicando a força e a direção dessa relação.
*   **Análise de Frequência e Distribuição:** Contagem da frequência de respostas para variáveis categóricas (e.g., 'Reação à Tarifa Dinâmica', 'Compara Preços?', 'Uso Ferramenta Segurança'), apresentadas em termos percentuais para facilitar a compreensão da distribuição das respostas.

## 3. Geração de Gráficos e Visualizações

Para complementar a análise estatística e proporcionar uma compreensão visual mais clara dos dados, foram gerados diversos gráficos utilizando as bibliotecas `matplotlib.pyplot` e `seaborn` do Python. Cada gráfico foi projetado para ilustrar um aspecto específico da análise, permitindo a identificação rápida de padrões e tendências. Os gráficos gerados incluem:

*   Gráfico de barras para a satisfação com o transporte público.
*   Gráfico de dispersão para a correlação entre gasto mensal e viagens por semana.
*   Gráficos de pizza para a reação à tarifa dinâmica e a frequência de comparação de preços.
*   Gráfico de barras para a importância do preço versus tempo.
*   Gráficos de barras para a média de cancelamentos e a média de viagens de moto.
*   Gráfico de pizza para o uso de ferramentas de segurança.

Todos os gráficos foram salvos em formato PNG no diretório `/home/ubuntu/` para serem incorporados ao relatório final.

## 4. Interpretação e Argumentação

Os resultados das análises estatísticas e as visualizações foram interpretados criticamente, com o objetivo de construir uma argumentação que refutasse a conclusão original do PDF e sustentasse a tese de que os transportes por aplicativo não são a solução para a mobilidade urbana. A interpretação focou em:

*   **Identificação de Discrepâncias:** Comparação dos dados com as afirmações do PDF para destacar inconsistências ou omissões.
*   **Contextualização dos Dados:** Análise dos números dentro do contexto socioeconômico e urbano de Manaus, considerando as implicações para a população jovem.
*   **Construção de Argumentos:** Desenvolvimento de argumentos baseados em evidências que demonstram as limitações dos aplicativos de transporte como solução abrangente, focando em aspectos como custo, confiabilidade, segurança e impacto no transporte público.

## 5. Elaboração do Relatório MD Book

Finalmente, todas as informações coletadas, processadas e interpretadas foram sintetizadas e organizadas em um relatório no formato MD Book. O relatório foi estruturado em arquivos `.md` separados para cada seção (Summary, Introdução, Análise dos Dados, Metodologia, Objetivos, Conclusão e Referências), facilitando a leitura e a navegação. A linguagem utilizada é técnica, mas clara e concisa, e a argumentação é sempre fundamentada nos dados empíricos e nas referências bibliográficas. As referências do slide original foram mantidas e adaptadas para o formato de citação.



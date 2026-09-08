# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Foram utilizados os seguintes datasets do repositório `Hugging Face`:
- [Snorkel AI - Agente Financeiro](https://huggingface.co/datasets/snorkelai/agent-finance-reasoning)
- [Sujet Ai - Instrutor Financeiro](https://huggingface.co/datasets/sujet-ai/Sujet-Finance-Instruct-177k)

Os datasets mesclam a capacidade de raciocínio e resolução de problemas com uma alta capacidade de entendimento contextual. Abaixo segue tabela comparativa dos datasets:

|Feature|`sujet-ai/Sujet-Finance-Instruct-177k`|`snorkelai/agent-finance-reasoning`|
|---------|---------|---------|
|Volume de dados|~177.000 amostras|Menor, altamente curado e focado em raciocínio|
|Objetivo Principal|Treinamento de instrução (Instruction Tuning) abrangente para tarefas financeiras diversas.|Treinamento de agentes autônomos e resolução de problemas financeiros complexos.|
|Foco Estrutural|Pares de instrução/resposta cobrindo análise de sentimento, classificação, extração de entidades e Q&A.|Cadeias de raciocínio passo a passo (Chain-of-Thought / CoT) e uso de ferramentas.|
|Caso de Uso Ideal|Ajustar LLMs para atuarem como assistentes financeiros gerais e analistas de texto.|Treinar agentes para solucionar cálculos multifacetados, chamadas de API e relatórios complexos.|

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

1. Os datasets são baixados através da lib `load_datasets` de `datasets`, armazenando em uma variável.
2. Após carregados os dados na variável, utilizamos a lib `sentence_transformer` para podermos criar os índices FAISS (*Facebook AI Similarity Search*) - criando tags para facilitar a contextualização do agente.
3. O passo final é a realização dos embutimentos (*embeddings*), finalizando a vetorização e deixando os dados disponíveis para serem contextualizados e enviados para a LLM.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

1. Após a apresentação inicial, um laço `for` verifica se existe histórico de prompts, caso seja a primeira interação, a mensagem *"Digite sua dúvida financeira..."* é exibida;
2. Quando a solicitação do usuário é enviada em markdown para o agente, que irá vetorizar o prompt e enviar para a LLM.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Os dados do prompt estão sendo arquivados em um log, logo conseguimos manter uma base para realizar melhorias no agente. Abaixo segue exemplo:

PERGUNTA ORIGINAL DO USUÁRIO:
Estou com R$ 5.000,00 para investir em títulos imobiliários, me indique quais as melhores opções atualmente e em quanto tempo eu consigo dobrar o valor investido.

⚙️ PROMPT INJETADO NO SYSTEM_INSTRUCTION:



Você é o BIO, um agente financeiro experiente, acolhedor e contemporâneo, que dá respostas diretas e de fácil assimilação, sempre utilizando analogias para facilitar o entendimento do usuário. Sua missão é ajudar o usuário desde dúdivas simples, como "como faço para aumentar o limite do meu cartão de crédito" ao "como posso começar a investir na bolsa de valores".

\#\#\# DIRETRIZES DE COMPORTAMENTO:
1. Saudação: Inicie a primeira interação do atendimento apresentando-se brevemente ("Olá! Sou o BIO, expert em finanças, como posso te ajudar hoje?"). Evite termos como "Bom dia" ou "Boa noite".
2. Linguagem Simples: Nunca use jargões financeiros sem explicação. Quando usar um termo técnico, explique-o usando analogias do dia a dia.
3. Tom de Voz: Empático, pedagógico, objetivo e encorajador.

\#\#\# EXEMPLOS DE ESTILOS DE RESPOSTA:
Usuário: Onde eu invisto 100 reais?
Agente: Com R$ 100, uma boa opção para dar o primeiro passo é o Tesouro Selic ou um CDB com liquidez diária de um banco sólido. Eles funcionam como uma "reserva de emergência": são tão seguros quanto a poupança, mas rendem mais e você pode resgatar quando precisar.

Usuário: O que é taxa Selic?
Agente: A taxa Selic é a taxa básica de juros da nossa economia. Pense nela como o "preço do dinheiro" no país. Quando ela sobe, o crédito fica mais caro para conter a inflação; quando cai, incentiva os empréstimos e o consumo.

\#\#\# REGRA DE OURO (SEGURANÇA, FATOS E GUARDRAILS):
- Responda APENAS com base em dados financeiros, sua base de dados e fatos reais confirmados. NUNCA invente dados ou informações econômicas.
- Você só faz recomendações de investimento se tiver o perfil financeiro completo do cliente. Sempre finalize recomendações com o texto: "Sou uma inteligência artificial e posso errar. Antes de investir, consulte um profissional."
- Se a pergunta for sobre FINANÇAS, mas você não tiver certeza absoluta sobre uma taxa ou dado específico, responda: "Desculpe, não tenho essa informação no momento."

\#\#\# DIRETRIZ DE ESCOPO (FORA DE FINANÇAS):
- Você é um agente estritamente financeiro. Se o usuário trouxer QUALQUER assunto fora desse ecossistema (como mecânica, medicina, culinária, etc.), você NÃO deve tentar resolver o problema técnico e NEM usar a frase de incerteza acima.
- Sua missão obrigatória nesses casos é recusar a resposta e DIRECIONAR o usuário de forma gentil para o profissional especialista daquela área.

\#\#\# EXEMPLOS DE DIRECIONAMENTO OBRIGATÓRIO:
Usuário: Meu carro parou de ligar, o motor foi consertado faz menos de um mês e está engasgando muito. O que pode ser?
Agente: Como eu sou um assistente focado estritamente em finanças, eu não tenho conhecimento técnico para avaliar o motor do seu veículo. Para resolver esse engasgo com segurança, o ideal é procurar um mecânico de confiança ou uma oficina automotiva!

Usuário: Estou tendo crises de ansiedade por conta dos meus problemas financeiros, como posso melhorar?
Agente: Sinto muito por isso. Embora eu possa te ajudar a organizar suas contas, para lidar com as crises de ansiedade o melhor a fazer é procurar um profissional de saúde mental (psicólogos ou psiquiatras).



\#\#\# CONTEXTO TEMPORAL ATUAL:
- Data e Hora: 07/09/2026 às 19:55
- Período do Dia: Noite (Boa noite)


\#\#\# CONTEXTO DA BASE DE DADOS HUGGING FACE (Sujet & Snorkel AI):
Use os dados abaixo como referência fundamentada para construir sua resposta:
Base de conhecimento padrão sobre finanças pessoais e investimentos de baixo risco.

💬 ESTRUTURA DO HISTÓRICO DE MENSAGENS (MESSAGES):
[{'role': 'model', 'parts': [{'text': 'Olá! Sou o BIO, expert em finanças. Como posso te ajudar hoje?'}]}, {'role': 'user', 'parts': [{'text': 'Estou com R$ 5.000,00 para investir em títulos imobiliários, me indique quais as melhores opções atualmente e em quanto tempo eu consigo dobrar o valor investido.'}]}, {'role': 'user', 'parts': [{'text': 'Estou com R$ 5.000,00 para investir em títulos imobiliários, me indique quais as melhores opções atualmente e em quanto tempo eu consigo dobrar o valor investido.'}]}]
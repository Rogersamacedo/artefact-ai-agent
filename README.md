# Empório da Música — Agente de Atendimento

## 1. Visão geral

Este projeto implementa um agente de atendimento ao cliente para o Empório da Música, uma loja fictícia de instrumentos musicais localizada em Campo Grande, Mato Grosso do Sul.

A solução foi desenvolvida em Python para responder a perguntas sobre produtos, preços, disponibilidade em estoque, promoções e políticas comerciais da loja.

O agente utiliza regras de identificação de intenções, consultas aos arquivos CSV fornecidos no desafio e informações extraídas do manual de políticas da loja.

**Objetivo:** fornecer respostas fundamentadas nos dados disponíveis, reduzir respostas sem evidências e preservar informações pessoais dos clientes.

## 2. Funcionalidades

- Busca de produtos por nome e descrição.
- Consulta de preços cadastrados no catálogo.
- Verificação do status comercial e da quantidade em estoque.
- Consulta de promoções cadastradas para os produtos.
- Respostas sobre horários, endereço, pagamentos, entregas, trocas, devoluções, garantias e privacidade.
- Tratamento de perguntas que não correspondam às informações disponíveis.
- Proteção básica contra exposição de dados de pedidos sem autenticação.

## 3. Tecnologias utilizadas

- Python 3.10 ou superior.
- Biblioteca padrão do Python, incluindo `csv`, `pathlib`, `unicodedata` e `re`.
- Arquivos CSV como fonte de dados estruturados.
- Arquivos PDF e texto como fontes das políticas comerciais.

A implementação inicial não depende de APIs externas, serviços pagos ou modelos de linguagem hospedados.

Essa decisão mantém a solução simples de executar, reduz dependências e permite rastrear a origem das informações apresentadas ao cliente.

## 4. Arquitetura

A aplicação foi organizada em módulos para separar o atendimento, o acesso aos dados e as regras comerciais.

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Interface interativa de atendimento pelo terminal. |
| `agent.py` | Identificação de intenções e composição das respostas. |
| `data_loader.py` | Carregamento centralizado dos arquivos CSV autorizados. |
| `catalog.py` | Consultas ao catálogo, preços, estoque e promoções. |
| `orders.py` | Consulta interna de pedidos e respectivos itens. |
| `policies.py` | Disponibilização das políticas comerciais da loja. |
| `requirements.txt` | Registro das dependências Python do projeto. |
| `data/` | Arquivos CSV fornecidos para o desafio. |
| `docs/` | Documentos de referência e políticas da loja. |

### Fluxo de atendimento

1. O cliente envia uma pergunta.
2. O agente normaliza o texto e identifica possíveis intenções.
3. Quando necessário, consulta o catálogo ou as políticas da loja.
4. Os dados retornados são utilizados para compor a resposta.
5. Se não houver informação suficiente, o agente informa a limitação em vez de inventar uma resposta.

## 5. Fontes de dados

A aplicação utiliza os seguintes conjuntos de dados:

- `products.csv`: catálogo, preços, descrições, status e estoque.
- `promotions.csv`: promoções associadas aos produtos.
- `categories.csv`: categorias do catálogo.
- `customers.csv`: dados cadastrais dos clientes.
- `orders.csv`: informações dos pedidos.
- `order_items.csv`: itens associados aos pedidos.

Os arquivos originais possuem prefixos no nome. O carregador identifica os arquivos esperados na pasta `data/`.

As políticas comerciais são consultadas a partir das informações organizadas no módulo `policies.py`, com referência ao manual fornecido no desafio.

**Fonte da verdade:** preços, estoque e promoções devem ser obtidos dos dados fornecidos, enquanto regras comerciais devem seguir o manual da loja.

## 6. Como executar

### Pré-requisitos

- Python 3.10 ou superior.
- Git, caso deseje clonar o repositório.

### Preparação do ambiente

Clone o repositório e entre na pasta do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd artefact-ai-agent
```

Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

A instalação de dependências externas não é necessária para a implementação inicial, que utiliza a biblioteca padrão do Python.

### Iniciar o atendimento

Execute:

```bash
python main.py
```

O atendimento será realizado pelo terminal. Digite uma pergunta e, para encerrar, utilize `sair`.

## 7. Exemplos de interação

Os exemplos abaixo ilustram os cenários de atendimento previstos. As respostas efetivas dependem dos dados presentes nos arquivos fornecidos e devem ser conferidas durante a validação final.

### Exemplo 1 — Consulta de produto

**Cliente:** Vocês têm violão Yamaha?

**Agente:** Consulta o catálogo e apresenta os produtos correspondentes encontrados, com os preços e as informações de disponibilidade registradas.

**Objetivo:** demonstrar a consulta de dados reais do catálogo.

### Exemplo 2 — Consulta de preço e promoção

**Cliente:** Esse instrumento está em promoção?

**Agente:** Consulta as promoções ativas associadas ao produto identificado e apresenta o desconto e o preço promocional calculado, quando houver uma promoção cadastrada.

**Objetivo:** evitar a apresentação de descontos que não estejam registrados nos dados.

### Exemplo 3 — Política comercial

**Cliente:** Como funciona o desconto no PIX?

**Agente:** Consulta a política de pagamento da loja e informa as condições registradas no manual, incluindo a regra de não acumulação do desconto com outras promoções.

**Objetivo:** responder com base nas regras comerciais documentadas.

### Exemplo 4 — Privacidade e pedidos

**Cliente:** Quero consultar meu pedido. O número é 1.

**Agente:** Informa que o protótipo não possui autenticação de clientes e que, por segurança, não consultará dados de pedidos nessa conversa.

**Objetivo:** demonstrar que conhecer o número de um pedido não é suficiente para autorizar a exposição de dados pessoais.

## 8. Decisões técnicas

### Separação de responsabilidades

O código foi dividido em módulos para facilitar a manutenção, a leitura e a evolução da aplicação.

### Uso de dados estruturados

Os arquivos CSV são consultados diretamente, evitando a necessidade de introduzir uma infraestrutura de banco de dados para o escopo do desafio.

### Respostas fundamentadas

O agente utiliza os dados disponíveis e as políticas documentadas. Quando não encontra informações correspondentes, deve informar a limitação.

### Simplicidade operacional

A solução utiliza Python e a biblioteca padrão, reduzindo a configuração necessária para executar o projeto.

### Segurança e privacidade

O módulo de pedidos está separado das consultas ao catálogo. A interface de atendimento não deve expor informações de pedidos sem um mecanismo apropriado de autenticação e autorização.

O protótipo não implementa autenticação real de clientes.

## 9. Limitações conhecidas

- A identificação de intenções utiliza regras e palavras-chave, podendo não compreender todas as formas de formular uma pergunta.
- A busca textual não equivale a uma busca semântica e pode não reconhecer sinônimos ou descrições muito diferentes das cadastradas.
- As respostas dependem da qualidade, da atualização e da consistência dos arquivos de origem.
- O agente não utiliza um modelo de linguagem para interpretar livremente perguntas complexas.
- Não há integração com sistemas externos de pedidos, pagamentos ou logística.
- Não existe autenticação de clientes ou autorização de acesso a pedidos.
- O cálculo de preços promocionais depende da correção dos dados de promoção e de suas regras de aplicação.
- A validação funcional realizada até o momento cobre a busca específica e ampla de produtos, a consulta de uma política comercial e a recusa de acessórios fora do escopo. Outros cenários ainda precisam ser verificados.

## 10. Testes e validação

### Testes executados

- Compilação sintática de `agent.py` com `python -m py_compile agent.py`.
- Consulta ao catálogo: busca por produtos Yamaha.
- Consulta específica de produto: Yamaha C40 Nylon Natural, ID 81, preço de R$ 599,90 e estoque de 12 unidades.
- Consulta à política de troca e devolução.
- Teste funcional de busca específica pelo Yamaha C40, retornando somente o modelo solicitado.
- Teste funcional de busca ampla por violões Yamaha, retornando cinco modelos.
- Teste de pergunta fora do escopo comercial, sobre venda de cordas para violão.

Os resultados acima foram observados durante a execução local do protótipo. Os exemplos de conversa correspondentes estão registrados em `examples.md`.

### Cenários ainda a verificar

- Busca por produtos inexistentes.
- Promoções ativas e produtos sem promoção.
- Perguntas vazias e encerramento da interface.
- Proteção de informações de pedidos.
- Outros cenários de erro e consistência das respostas.

Os testes descritos como pendentes não devem ser considerados aprovados.

## 11. Uso de assistentes de inteligência artificial

Assistentes de IA foram utilizados como apoio ao desenvolvimento, incluindo organização da arquitetura, elaboração de código, explicação de decisões técnicas e revisão de possíveis limitações.

As decisões finais de implementação e a validação do comportamento da aplicação devem ser realizadas pelo responsável pelo projeto.

O uso de assistentes não substitui a necessidade de executar testes, conferir os resultados e verificar a aderência aos requisitos do desafio.

## 12. Evoluções possíveis

Como próximos passos, a solução poderia receber:

- Testes automatizados com `unittest` ou `pytest`.
- Identificação de intenções mais robusta.
- Busca semântica no catálogo.
- Integração com um modelo de linguagem, mantendo consultas verificáveis aos dados.
- Autenticação e autorização para consultas de pedidos.
- Interface web e registro de métricas de atendimento.

Essas evoluções não fazem parte da implementação inicial e devem ser priorizadas de acordo com os requisitos e os resultados da avaliação.

## 13. Conclusão

O projeto apresenta uma solução modular de atendimento baseada em Python, dados estruturados e políticas comerciais documentadas.

A prioridade é oferecer respostas consistentes com as fontes disponíveis, manter o código simples de executar e reconhecer explicitamente os limites do protótipo.

A entrega documenta os testes funcionais já executados e identifica explicitamente os cenários que ainda precisam de verificação.

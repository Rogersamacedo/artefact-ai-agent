# Exemplos de atendimento

Os cenários abaixo descrevem as interações previstas para o agente do Empório da Música. As respostas efetivas deverão ser confirmadas na bateria de testes funcionais.

## 1. Consulta de produto e estoque

**Cliente:** Vocês têm violão Yamaha?

**Agente:** Consulta o catálogo e apresenta os instrumentos correspondentes encontrados, seus preços e a disponibilidade registrada.

**Dados consultados:** `products.csv`.

**Critério de avaliação:** não apresentar produtos, preços ou quantidades que não estejam nos dados de origem.

## 2. Consulta de promoção

**Cliente:** Esse violão está em promoção?

**Agente:** Verifica se há uma promoção ativa associada ao produto identificado. Caso exista, apresenta o percentual cadastrado e o preço promocional calculado. Caso contrário, informa que não encontrou uma promoção ativa para o produto.

**Dados consultados:** `products.csv` e `promotions.csv`.

**Critério de avaliação:** não inventar descontos e não apresentar promoções inativas como válidas.

## 3. Política de pagamento

**Cliente:** Qual é o desconto para pagamento via PIX?

**Agente:** Consulta a política de pagamento e apresenta as condições registradas no manual da loja, incluindo a regra de não acumulação com outras promoções.

**Fonte consultada:** política comercial da loja.

**Critério de avaliação:** manter a resposta alinhada às condições documentadas.

## 4. Consulta de pedido e privacidade

**Cliente:** Quero consultar o pedido número 1.

**Agente:** Informa que o protótipo não possui autenticação de clientes e que, por segurança, não consultará dados de pedidos nessa conversa.

**Dados envolvidos:** `orders.csv` e `order_items.csv`.

**Critério de avaliação:** não expor informações de pedidos sem um mecanismo apropriado de autenticação e autorização.

## 5. Produto fora do catálogo comercial

**Cliente:** Vocês vendem cabos para instrumentos?

**Agente:** Consulta a política de escopo comercial e informa se o item está entre os produtos comercializados pela loja.

**Fonte consultada:** política comercial da loja.

**Critério de avaliação:** respeitar o escopo definido no manual.

## Observação

Estes são cenários de referência, não registros de uma execução real. As respostas e o comportamento efetivo do agente serão verificados na bateria de testes final.

"""Respostas baseadas no manual de políticas da loja."""

POLICIES = {
    "horario": (
        "Nosso horário de atendimento é de segunda a sexta, "
        "das 9h às 18h, e aos sábados, das 9h às 13h. "
        "Fechamos aos domingos e feriados."
    ),
    "endereco": (
        "Estamos na Rua 14 de Maio, 3200, Centro, "
        "Campo Grande - MS, CEP 79202-333."
    ),
    "pagamento": (
        "Aceitamos PIX, cartão de débito, cartão de crédito "
        "e boleto bancário. O PIX à vista tem 5% de desconto "
        "sobre o preço de tabela, exceto quando houver uma "
        "promoção, pois os descontos não são cumulativos. "
        "O cartão de crédito permite parcelamento conforme "
        "as condições do manual."
    ),
    "troca_devolucao": (
        "Para compras online, o direito de arrependimento pode "
        "ser solicitado em até 7 dias corridos após o recebimento, "
        "observadas as condições do manual. Para defeitos de "
        "fabricação, a política prevê troca em até 30 dias corridos "
        "após a compra. Posso orientar você sobre a regra aplicável."
    ),
    "entrega": (
        "Na região metropolitana de Campo Grande, pedidos acima "
        "de R$ 500 têm frete grátis; abaixo desse valor, o frete "
        "é de R$ 35, com prazo estimado de 1 a 3 dias úteis. "
        "Para outras cidades, o prazo e o valor dependem da "
        "modalidade de envio e do destino."
    ),
    "garantia": (
        "O manual prevê garantia legal de 90 dias contra defeitos "
        "de fabricação, contados do recebimento. A garantia do "
        "fabricante pode variar conforme o produto e seu certificado."
    ),
    "escopo": (
        "Somos especializados em instrumentos musicais. "
        "Não comercializamos acessórios como cordas, palhetas, "
        "cabos, cases, pedais ou amplificadores."
    ),
    "privacidade": (
        "Os dados pessoais são utilizados para finalidades como "
        "processamento de pedidos, entregas e comunicações previstas "
        "no manual. Para solicitar exclusão de dados, entre em contato "
        "com a loja por um canal oficial."
    ),
}


def consultar_politica(tema: str) -> str | None:
    """Retorna uma política conhecida ou None se o tema não for reconhecido."""
    tema = tema.strip().casefold()
    return POLICIES.get(tema)

"""Agente de atendimento do Empório da Música."""

import re
import unicodedata

from catalog import buscar_produtos, consultar_promocoes
from policies import consultar_politica


def normalizar(texto: str) -> str:
    """Remove acentos e normaliza o texto para comparação."""
    texto = unicodedata.normalize("NFD", texto.casefold())
    return "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )


def formatar_moeda(valor: float) -> str:
    """Formata valores monetários no padrão brasileiro."""
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = (
        valor_formatado.replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )
    return f"R$ {valor_formatado}"


def buscar_produtos_na_mensagem(mensagem: str) -> list[dict]:
    """Busca produtos usando palavras relevantes da pergunta."""
    palavras_ignoradas = {
        "vocês", "voces", "tem", "têm", "vende", "vendem",
        "quero", "comprar", "procuro", "quanto", "custa",
        "preco", "produto", "produtos", "instrumento",
        "instrumentos", "me", "um", "uma", "uns", "umas",
        "de", "do", "da", "dos", "das", "o", "a", "os", "as",
        "e", "por", "favor", "qual", "quais", "no", "na",
        "nos", "nas", "com", "para", "temos", "estoque",
        "disponivel", "disponibilidade", "promocao",
        "promocoes", "desconto", "descontos", "valor",
        "gostaria", "saber", "existe", "existem", "hoje",
        "esse", "essa", "isso", "ele", "ela", "quanto",
    }

    palavras = re.findall(r"[A-Za-zÀ-ÿ0-9]+", mensagem)

    termos = []
    for palavra in palavras:
        termo_normalizado = normalizar(palavra)

        if (
            len(termo_normalizado) >= 3
            and termo_normalizado not in palavras_ignoradas
            and termo_normalizado not in termos
        ):
            termos.append(termo_normalizado)

    candidatos = {}

    for termo in termos:
        resultados = buscar_produtos(termo)

        # Se a busca sem acentos não encontrar resultados,
        # tenta novamente com a grafia original.
        if not resultados:
            palavra_original = next(
                (
                    palavra
                    for palavra in palavras
                    if normalizar(palavra) == termo
                ),
                termo,
            )
            resultados = buscar_produtos(palavra_original)

        for produto in resultados:
            product_id = produto["product_id"]

            nome = normalizar(produto["name"])
            descricao = normalizar(produto["description"])

            pontuacao = 3 if termo in nome else 1

            if product_id not in candidatos:
                candidatos[product_id] = {
                    "produto": produto,
                    "pontuacao": 0,
                }

            candidatos[product_id]["pontuacao"] += pontuacao

    ordenados = sorted(
        candidatos.values(),
        key=lambda item: item["pontuacao"],
        reverse=True,
    )

    return [item["produto"] for item in ordenados[:5]]


def responder(mensagem: str) -> str:
    """Responde a perguntas sobre produtos e políticas da loja."""
    texto = normalizar(mensagem.strip())

    if not texto:
        return "Pode me dizer como posso ajudar?"

    # Segurança: pedidos exigem autenticação do cliente.
    if any(palavra in texto for palavra in (
        "pedido", "rastreio", "rastreamento",
        "codigo de rastreio", "acompanhar entrega",
    )):
        return (
            "Posso ajudar com informações sobre pedidos, mas este "
            "protótipo não possui autenticação de clientes. "
            "Por segurança, não consultarei dados de pedidos "
            "nesta conversa."
        )

    # Produtos fora do escopo comercial da loja.
    if any(palavra in texto for palavra in (
        "corda", "cordas", "palheta", "palhetas",
        "cabo", "cabos", "case", "cases",
        "pedal", "pedais", "amplificador", "amplificadores",
    )):
        return consultar_politica("escopo") or (
            "Não encontrei essa informação no manual da loja."
        )

    # Horários de funcionamento.
    if any(palavra in texto for palavra in (
        "horario", "abre", "aberto", "funcionamento",
        "fecha", "fechado",
    )):
        return consultar_politica("horario") or (
            "Não encontrei essa informação no manual da loja."
        )

    # Endereço da loja.
    if any(palavra in texto for palavra in (
        "endereco", "localizacao", "onde fica",
    )):
        return consultar_politica("endereco") or (
            "Não encontrei essa informação no manual da loja."
        )

    # Formas de pagamento.
    if any(palavra in texto for palavra in (
        "pix", "pagamento", "parcelamento", "cartao",
        "boleto", "parcelar", "parcelas",
    )):
        return consultar_politica("pagamento") or (
            "Não encontrei essa informação no manual da loja."
        )

    # Trocas, devoluções e arrependimento de compra.
    if any(palavra in texto for palavra in (
        "troca", "devolucao", "arrependimento",
        "defeito", "devolver", "reembolso",
    )):
        return consultar_politica("troca_devolucao") or (
            "Não encontrei essa informação no manual da loja."
        )

    # Frete e entrega.
    if any(palavra in texto for palavra in (
        "frete", "entrega", "prazo de entrega",
        "correios", "sedex",
    )):
        return consultar_politica("entrega") or (
            "Não encontrei essa informação no manual da loja."
        )

    # Garantia.
    if "garantia" in texto:
        return consultar_politica("garantia") or (
            "Não encontrei essa informação no manual da loja."
        )

    # Privacidade e dados pessoais.
    if any(palavra in texto for palavra in (
        "privacidade", "dados pessoais", "lgpd",
        "excluir meus dados", "apagar meus dados",
    )):
        return consultar_politica("privacidade") or (
            "Não encontrei essa informação no manual da loja."
        )

    # Busca de produtos, preços, estoque e promoções.
    termos_catalogo = (
        "tem", "vende", "produto", "instrumento",
        "guitarra", "violao", "violão", "teclado",
        "bateria", "ukulele", "yamaha", "gibson",
        "fender", "preco", "preço", "quanto custa",
        "estoque", "disponivel", "disponível",
        "promocao", "promoção", "desconto", "valor",
        "baixo", "violino", "piano", "cavaco",
    )

    if any(termo in texto for termo in termos_catalogo):
        produtos = buscar_produtos_na_mensagem(mensagem)

        if not produtos:
            return (
                "Não encontrei produtos correspondentes no catálogo. "
                "Tente informar o nome ou o modelo do instrumento."
            )

        respostas = []

        for produto in produtos:
            preco = float(produto["price_brl"])
            estoque = int(produto["stock_quantity"])
            status = produto["status"]

            if status == "active" and estoque > 0:
                disponibilidade = (
                    f"Disponível em estoque: {estoque} unidade(s)."
                )
            elif status == "coming_soon":
                disponibilidade = (
                    "Produto ainda não disponível para venda."
                )
            elif status == "discontinued":
                disponibilidade = "Produto descontinuado."
            else:
                disponibilidade = "Produto sem estoque no momento."

            linha = (
                f'{produto["name"]} — {formatar_moeda(preco)}. '
                f"{disponibilidade}"
            )

            promocoes = consultar_promocoes(
                produto["product_id"]
            )

            if promocoes:
                detalhes = []

                for promocao in promocoes:
                    desconto = float(
                        promocao["discount_percent"]
                    )
                    preco_promocional = preco * (
                        1 - desconto / 100
                    )

                    detalhes.append(
                        f"{desconto:g}% de desconto; "
                        f"preço promocional: "
                        f"{formatar_moeda(preco_promocional)}"
                    )

                linha += " Promoção cadastrada: "
                linha += "; ".join(detalhes) + "."

            respostas.append(linha)

        return "\n".join(respostas)

    return (
        "Posso ajudar com produtos, preços, estoque, promoções "
        "e políticas da loja. Pode reformular sua pergunta?"
    )

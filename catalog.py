"""Consultas ao catálogo e às promoções do Empório da Música."""

from data_loader import load_csv


def buscar_produtos(termo: str) -> list[dict[str, str]]:
    """Busca produtos pelo nome ou pela descrição."""
    termo = termo.strip().casefold()

    if not termo:
        return []

    produtos = load_csv("products")

    return [
        produto
        for produto in produtos
        if termo in produto["name"].casefold()
        or termo in produto["description"].casefold()
    ]


def consultar_produto(product_id: str) -> dict[str, str] | None:
    """Localiza um produto pelo identificador."""
    for produto in load_csv("products"):
        if produto["product_id"] == str(product_id):
            return produto

    return None


def consultar_promocoes(product_id: str) -> list[dict[str, str]]:
    """Retorna somente as promoções ativas associadas ao produto."""
    return [
        promocao
        for promocao in load_csv("promotions")
        if promocao["product_id"] == str(product_id)
        and promocao["is_active"] == "1"
    ]


def consultar_disponibilidade(product_id: str) -> dict[str, object] | None:
    """Informa o estado comercial e o estoque de um produto."""
    produto = consultar_produto(product_id)

    if produto is None:
        return None

    estoque = int(produto["stock_quantity"])
    status = produto["status"]

    disponivel = status == "active" and estoque > 0

    return {
        "product_id": produto["product_id"],
        "nome": produto["name"],
        "status": status,
        "estoque": estoque,
        "disponivel": disponivel,
    }


def consultar_preco(product_id: str) -> dict[str, object] | None:
    """Retorna o preço de tabela e as promoções ativas."""
    produto = consultar_produto(product_id)

    if produto is None:
        return None

    return {
        "product_id": produto["product_id"],
        "nome": produto["name"],
        "preco_tabela": float(produto["price_brl"]),
        "promocoes": consultar_promocoes(product_id),
    }

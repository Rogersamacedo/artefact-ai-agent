"""Consultas de pedidos do Empório da Música."""

from data_loader import load_csv
from catalog import consultar_produto


def consultar_pedido(order_id: str) -> dict[str, object] | None:
    """Consulta os dados básicos de um pedido e seus itens."""
    pedidos = load_csv("orders")
    pedido = next(
        (p for p in pedidos if p["order_id"] == str(order_id)),
        None,
    )

    if pedido is None:
        return None

    itens_pedido = [
        item
        for item in load_csv("order_items")
        if item["order_id"] == str(order_id)
    ]

    itens = []

    for item in itens_pedido:
        produto = consultar_produto(item["product_id"])

        itens.append({
            "product_id": item["product_id"],
            "nome": produto["name"] if produto else "Produto não identificado",
            "quantidade": int(item["quantity"]),
        })

    return {
        "order_id": pedido["order_id"],
        "status": pedido["status"],
        "data_pedido": pedido["order_date"],
        "previsao_entrega": pedido["estimated_delivery"],
        "codigo_rastreamento": pedido["tracking_code"],
        "itens": itens,
    }

"""Interface de atendimento do Empório da Música."""

from agent import responder


def main():
    """Executa o atendimento interativo pelo terminal."""

    print("=" * 55)
    print("       EMPÓRIO DA MÚSICA")
    print("       Atendimento Virtual")
    print("=" * 55)
    print("Olá! Como posso ajudar você hoje?")
    print("Pergunte sobre produtos, preços, estoque ou políticas.")
    print("Digite 'sair' para encerrar o atendimento.")
    print("-" * 55)

    while True:
        try:
            mensagem = input("\nVocê: ").strip()

            if mensagem.casefold() in {"sair", "encerrar", "tchau"}:
                print(
                    "\nAtendente: Obrigado pelo contato! "
                    "O Empório da Música agradece sua visita."
                )
                break

            resposta = responder(mensagem)
            print(f"\nAtendente: {resposta}")

        except (KeyboardInterrupt, EOFError):
            print("\n\nAtendimento encerrado.")
            break


if __name__ == "__main__":
    main()

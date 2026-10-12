from decimal import Decimal


def ask(
    prompt: str,
    parse_func=str,
    valid_cond=lambda _: True,
    error="Invalid input",
    allow_blank=False,
):
    while True:
        raw = input(prompt).strip()
        if allow_blank and not raw:
            return None

        try:
            value = parse_func(raw)
        except (
            ValueError,
            ArithmeticError,
        ):  # Decimal returns InvalidOperaton which is an ArithmeticError
            print(error)
            continue

        if valid_cond(value):
            return value

        print(error)


def parse_price(raw: str):
    return Decimal(raw.removeprefix("£"))


def ask_price(prompt, allow_blank=False):
    return ask(prompt, parse_price, lambda p: p > 0, "Invalid price", allow_blank)


def ask_stock(prompt, allow_blank=False):
    return ask(prompt, int, lambda n: n >= 0, "Invalid stock level", allow_blank)


def ask_existing(prompt, repo, error):
    return ask(
        prompt,
        lambda id: repo.get(int(id)),
        lambda response: response is not None,
        error,
    )

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    for i in range(3,0, -1):
        if len(text) - i <= 0:
            pass
        else:
            print(text[-i:])
    return (".")


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))

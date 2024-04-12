def get_upper_line(text: str) -> str:
    """Приводит текст, к верхнему регистру"""
    return text.upper()


def get_title_line(text: str) -> str:
    """Делает заглавными первые буквы каждого слова"""
    return text.title()


def main():
    print(get_upper_line("correct text"))
    print(get_title_line("correct text"))


if __name__ == "__main__":
    main()

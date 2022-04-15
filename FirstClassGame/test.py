import unicodedata;


def remove_accents(string: str) -> str:
    normalized = unicodedata.normalize('NFKD', string)
    return ''.join([c for c in normalized if not unicodedata.combining(c)])


palavra = "MAÇÃ"

corrigido = remove_accents(palavra)

print(palavra)
print(corrigido)
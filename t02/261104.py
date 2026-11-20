def main():
    name = input("wie heißt duuu?").lower()
    tag = input("was ist heute für ein tag?").lower()
    adjektiv = input(f"guten morgen, {name}. wie du weißt, fängt {tag} fängt mit {tag[0]} an: sag mir dein lieblingsadjektiv, das mit {tag[0]} anfängt:").lower()
    while adjektiv[0] != tag[0]:
            adjektiv = input(f"ne ne ne, so nicht - das versuchst du nochmal! mit {tag[0]} soll dit"
                  f" anfagen:")
    print(f"ich wünsche dir, liebe {name}, einen {adjektiv}en {tag}! byeeee")


main()


def add_surname(names):
    words_with_k = [word + " Kardashian" for word in names if word.startswith("k") or word.startswith("K")]
    return words_with_k

#print(add_surname(["Karl", "John", "Kim", "Fjiwadksa", "kdksaKKdksa"]))
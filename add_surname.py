def add_surname(names):
    """
    Adds the surname "Kardashian" to the end of every name starting with K.

    Arguments: 
        names (list of strings): A list of names, each of which that start with a K will have Kardashian added to it.

    Returns:
        words_with_k (list of strings): A list of the K names, each with Kardashian added to the end.
    """
    words_with_k = [word + " Kardashian" for word in names if word.startswith("k") or word.startswith("K")]
    return words_with_k

#print(add_surname(["Karl", "John", "Kim", "Fjiwadksa", "kdksaKKdksa"]))
def word_score(word):
    """returns Scrabble score of input word
    
    Arguments:
        word {str} -- The input word
    
    Returns:
        int -- The score of the word
    """
    letter_scores = {
        1: "aeioulnrst",
        2: "dg",
        3: "bcmp",
        4: "fhvwy",
        5: "k",
        8: "jx",
        10: "qz"
    }

    total = 0
    for i in word.lower():
        for k,v in letter_scores.items():
            for letter in v:
                if i == letter:
                    total+=k

    return total

word_score()
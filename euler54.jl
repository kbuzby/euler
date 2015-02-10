function handScore(hand)
    ##extract suits
    suits = map(card -> card[2], hand)
    ##extract values
    vals = map(card -> card[1], hand)

    ## determine highcard

    ##if statment ranking hands
    if (sort(vals) == [10,'A','J','K','Q'] && length(Set(suits)) == 1)
        #Royal Flush
        return (9, value, highcard)
    else if
        #Straight Flush
        return (8, value, highcard)
    else if 
        #Four of a Kind
        return (7, value, highcard)
    else if
        #Full House
        return (6, value, highcard)
    else if
        #Flush
        return (5, value, highcard)
    else if
        #Straight
        return (4, value, highcard)
    else if
        #Three of a Kind
        return (3, value, highcard)
    else if
        #Two Pairs
        return (2, value, highcard)
    else if
        #One Pair
        return (1, value, highcard)
    else
        #High Card
        return (0, value, highcard)
    ##return (hand rank, hand value, high card)
end

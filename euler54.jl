function isStraight(vals)
    if vals == [9,10,'J','K','Q'] || vals == [8,9,10,'J','Q'] || vals == [7,8,9,10,'J']
        return true
    else if vals[1]+1 == vals[2] && vals[2]+1 == vals[3] && vals[3]+1 == vals[4] && vals[4]+1 == vals[5]
        return true
    else
        return false
    end
end

function repeats(vals)
    return map(y -> length(find(x->isqual(y,x),vals)),Set(vals))
end

function handScore(hand)
    ##extract suits
    suits = map(card -> card[2], hand)
    ##extract values
    vals = sort(map(card -> card[1], hand))

    ## determine highcard

    ##if statment ranking hands
    if vals == [10,'A','J','K','Q'] && length(Set(suits)) == 1
        #Royal Flush
        return (9, value, highcard)
    else if length(Set(suits)) == 1 && isStraight(vals)
        #Straight Flush
        return (8, value, highcard)
    else if maximum(repeats(vals)) == 4
        #Four of a Kind
        return (7, value, highcard)
    else if repeats(vals) == [2,3]
        #Full House
        return (6, value, highcard)
    else if length(Set(suits)) == 1
        #Flush
        return (5, value, highcard)
    else if isStraight(vals)
        #Straight
        return (4, value, highcard)
    else if repeats(vals) == [1,1,3]
        #Three of a Kind
        return (3, value, highcard)
    else if repeats(vals) == [1,2,2]
        #Two Pairs
        return (2, value, highcard)
    else if repeats(vals) == [1,1,1,2]
        #One Pair
        return (1, value, highcard)
    else
        #High Card
        return (0, value, highcard)
    ##return (hand rank, hand value, high card)
end

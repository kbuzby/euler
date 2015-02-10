
f = open("p098_words.txt")
words = readdlm(f,',')
wordlengths = collect(map(x -> length(x), words))
for i = minimum(wordlengths):maximum(wordlengths)
    samelengths = []
    for j = 1:length(words)
        if wordlengths[j] == i
            push!(samelengths, words[j])
        end
    end
    println(samelengths)
end
println(minimum(wordlengths),",",maximum(wordlengths))

function result = calculateFactorial(n)
    result = 1;
    i = 1;
    while i <= n
        result = result * i;
        i = i + 1;
    end
end
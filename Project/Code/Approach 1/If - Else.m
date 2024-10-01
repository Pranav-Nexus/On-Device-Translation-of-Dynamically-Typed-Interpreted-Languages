function result = checkNumber(num)
    if num > 0
        result = 'The number is positive.';
    elseif num < 0
        result = 'The number is negative.';
    else
        result = 'The number is zero.';
    end
end
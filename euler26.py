def repeating(numerator, denominator):
	decimal_found = False
	
	v = numerator // denominator
	numerator = 10 * (numerator - v * denominator)
	answer = str(v)
	
	if numerator == 0:
		return answer

	answer += '.'

	states = {}

	while numerator > 0:
		prev_state = states.get(numerator, None)
		if prev_state != None:
			start_repeat_index = prev_state
			non_repeating = answer[:start_repeat_index]
			repeating = answer[start_repeat_index:]
			return non_repeating + '[' + repeating + ']'
		states[numerator] = len(answer)
	
		v = numerator // denominator
		answer += str(v)
		numerator -= v * denominator
		numerator *= 10
	
	if numerator > 0:
		return answer + '...'
	return answer

max = 0
for x in range(2,1000):
	num = repeating(1,x)
	if len(str(num)) > max:
		max = x
		print max	

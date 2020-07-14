# taeget amount n and a lost of valie 

def coins(target,list):

	min_value = min(list)
	min_coins = 100
	temp_coin = 0

	if target < min_value:
		return 0

	if target in list:
		return 1


	for i in list:
		temp_coin = 0
		value = target - i
		temp_coin += 1 + coins(value,list)
		value = target
		if temp_coin < min_coins:
			min_coins = temp_coin

	return min_coins

print coins(10,(1,5))
print coins(10,(1,5,10))
print coins(11,(1,5,6,8))
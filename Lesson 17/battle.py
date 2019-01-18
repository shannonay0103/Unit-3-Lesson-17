import time
import random

print('A wild Wartortle appears!')
time.sleep(.6)
print()
print('...the music changes...')
time.sleep(.6)
print()
print('You only have one Pokemon, Leekbird!')
time.sleep(.6)
print()
print('I choose you Leekbird!!!')
time.sleep(.6)
print()

# set the starting health values
leekbird_hp = 250
wartortle_hp = 600

#disply the current HP
print('Updated HP:')
time.sleep(0.3)	
print('Leekbird HP: ' + str(leekbird_hp))
time.sleep(0.3)
print('Wartortle HP: ' + str(wartortle_hp))
time.sleep(0.3)
print()

while leekbird_hp > 0 and wartortle_hp > 0:
	print('Choose your battle move:')
	time.sleep(1)
	print('- [1] Tackle')
	time.sleep(0.3)
	print('- [2] Super Screech')
	time.sleep(0.3)
	print('- [3] Eat Leek')
	time.sleep(0.3)
	print('- [4] Punch')
	time.sleep(0.3)
	print('- [5] Capture')
	print()

	player_move = input('Pick a move using the corresponding number: ')
	player_move = int(player_move)
	print()

	if player_move == 1:
		wartortle_hp = wartortle_hp - 25
		print('Leekbird uses Tackle and deals 25 HP of damage ')

	elif player_move == 2:
		damage = random.randint(5,40)
		wartortle_hp = wartortle_hp - damage
		print('Leekbird uses Super Screech and deals ' + str(damage) + ' HP of damage ')

	elif player_move == 3:
		leekbird_hp = leekbird_hp + 100
		print('Leekbird uses Eat Leek and recovers by 100 HP')

	elif player_move == 4:
		wartortle_hp = wartortle_hp - 45
		print('Leekbird uses Punch and deals 45 HP of damage ')

	elif player_move == 5:
		capture_roll = random.randint(0,600)
		if capture_roll > wartortle_hp:
			time.sleep(0.3)
			print('Capturing....')
			time.sleep(0.3)
			print('Capturing....')
			time.sleep(0.3)
			print('Capturing....')
			time.sleep(0.3)
			print('You got that boi')
			break
		else:
			time.sleep(0.3)
			print('Capturing....')
			time.sleep(0.3)
			print('Capturing....')
			time.sleep(0.3)
			print('Capturing....')
			time.sleep(0.3)
			print('Wartortle escaped.')
			time.sleep(0.3)



	# enemy battle choices
	enemy_move = random.randint(1,2)
	if enemy_move == 1:
		leekbird_hp = leekbird_hp - 30
		print('Wartortle uses Water Blast and deals 30 HP of damage.')

	elif enemy_move == 2:
		leekbird_hp = leekbird_hp - 20
		wartortle_hp = wartortle_hp + 20
		print('Wartortle uses Blood Drain and deals 20 HP of damage while also recovering 20 HP of health.')

	time.sleep(0.3)
	print()

	#disply the current HP
	print('Updated HP:')
	time.sleep(0.3)
	print('Leekbird HP: ' + str(leekbird_hp))
	time.sleep(0.3)
	print('Wartortle HP: ' + str(wartortle_hp))
	time.sleep(0.3)

#check who wins
if leekbird_hp > 0 and wartortle_hp == 0:
	print('Wild Wartortle has deadass died. You win!')
elif wartortle_hp > 0 and leekbird_hp==0:
	print('Wild Leekybird has deadass died. You win!')



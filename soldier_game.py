class soldier(object):
	
	
	def input_():
		bullets = 25
		soldiers = 0
		foes = 0
		ammo = 0
		floor = 0
		input_str = raw_input()
		floor_def = ['c','e','e','c','n','n','e','n','n','c'] #given
		dir = 1 #to maintain the direction in which the soldier is moving
		for i in range(0, len(input_str)):
			if input_str[i] == '0':
				floor += dir

			elif input_str[i] == '1':
				if floor_def[floor] == 'e' and bullets >= 3:
					bullets -= 3
					foes += 1
					floor += dir
					ammo += 3
				elif floor_def[floor] == 'e' and bullets < 3:
					soldiers += 1
					bullets = 25

					continue

				elif floor_def[floor] == 'c':
					#bullets -= 3
					foes += 1
					floor += dir
				elif floor_def[floor] == 'n' and bullets >= 5:
					foes += 1
					floor += dir
					bullets -= 5
					ammo += 5
				elif floor_def[floor] == 'n' and bullets < 5:
					soldiers += 1
					bullets = 25
					continue
			elif input_str[i] == '2':
				if dir == 1:
					dir = -1
				elif dir == -1:
					dir = 1

				floor += dir
				
			elif input_str[i] == 'U':
				
				dir = 1
				floor += dir

			elif input_str[i] == 'D':
				
				dir = -1
				floor += dir

			#debug print stmts

			'''print "Iteration %s" %i
			print "Current Floor - %s" %floor
			print "Ammo Consumed - %s" %ammo
			print "Foes Eliminated - %s" %foes
			print "Soldiers Dead - %s" %soldiers'''
		print "Current Floor - %s" %floor
		print "Ammo Consumed - %s" %ammo
		print "Foes Eliminated - %s" %foes
		print "Soldiers Dead - %s" %soldiers
		

		
	input_()


				




				





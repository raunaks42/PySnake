# Game Screen

import Control as f

import Intro



win = f.init_scr(50, 100, 1)

win = f.game_scr(win)



key = f.KEY_RIGHT 						                                                # Initializing values

score = 0

c = 0

b = 0

snake = [[1,3], [1,2], [1,1]]															# Initial snake co-ordinates

food=[]



f.calc_food(food)                         												# First food co-ordinates

win = f.print_food(food, win)



while key != 27:																		# While Esc key is not pressed

	win = f.print_score(score, win)

	win = f.inc_speed(snake, win)



	prevKey = key    						                                        	# Previous key pressed

	event, win = f.ip(win)																		# Input, if no input,event=-1

	key = key if event == -1 else event



	key, prevKey, c, win = f.pause(key, prevKey, win)
	
	if c:

		continue

		c = 0



	key, prevKey = f.invalid_check(key, prevKey, snake)
	


	# Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases regardless

	f.snk_inc(snake, key)



	# Stop if snake heads straight towards boundaries

	key, c, win = f.boundary(snake, key, win)
	
	if c:
	
		continue

		c = 0



	# If snake runs over itself

	b = f.death(snake)
	
	if b:

		break

		b = 0



	win, score,food = f.eat(snake, food, win, score)



	win = f.print_snake(snake, win)



f.cl_scr()



f.print_fscore(score)

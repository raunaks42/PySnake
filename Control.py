#Functions for both Intro and Game

import curses

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

from random import randint



def init_scr(h, b, border = 0):

	curses.initscr()												# Initialise the window

	win = curses.newwin(h, b, 0, 0)									# New window of (height,width,begin-y,begin-x)

	win.keypad(1)													# Keypad mode	

	curses.noecho()													# Turns off automatic display of keys pressed

	curses.curs_set(0)												# Invisible cursor

	if border:

		win.border(0)												# Border around window

	win.nodelay(1)													# No delay in input using getch

	return win



def game_scr(win):

	win.addstr(0, 47, ' SNAKE ')															# Display 'snake'

	win.addstr(49, 2, 'Esc to quit, Space to pause/play, Arrows for control')				# and rules

	return win



def intro_scr(win):

	win.addstr(1, 50, 'SNAKE')

	win.addstr(3, 1, "This is a game inspired by the 'retro' game Snake on most keypad phones")

	win.addstr(5, 1, 'For the n00bs, here are the r00ls:')

	win.addstr(6, 2, '1. Use the arrow keys to control your snake to eat food (displayed as *) on the arena')

	win.addstr(7, 2 ,'2. Eat food to grow')

	win.addstr(8, 2, '3. Grow and get faster')

	win.addstr(9, 2, '4. Eat yourself and you die')

	win.addstr(10, 2, '5. Hitting the boundary makes you dazed till you move away')

	win.addstr(11, 2, '6. Use the Space bar to pause/play the game')

	win.addstr(12, 2, '7. Use the Esc key to quit')

	win.addstr(14, 1, "It's that simple :)")

	win.addstr(16, 1, 'Team 13 (Raunak Sengupta, Disha Srinivas and Shreyas Kulkarni of Section H) worked pretty hard on this thx')

	win.addstr(17, 1, 'For crash reports, pls contact us')

	win.addstr(18, 1, 'We hope you love it ^_^')

	win.addstr(21, 1, 'PRESS THE SPACE BAR TO PLAY!')

	return win



def calc_food(food):

	food += [randint(2, 47), randint(2, 97)]



def print_food(food, win):

	win.addch(food[0], food[1], '*')

	return win



def print_score(score, win):

	win.addstr(0, 2, 'Score : ' + str(score) + ' ')            						# Printing 'Score'
	
	return win



def inc_speed(snake, win):

	win.timeout(130 - (len(snake)/2))				          						# Increases the speed of Snake as its length increases

	return win



def ip(win):

	i = win.getch()

	return i, win



def pause(key, prevKey, win):

	c = 0
	
	if key == ord(' '):                 						                    # If SPACE BAR is pressed, wait for another

		key = -1                                              						# one (Pause/Resume)

		while key != ord(' '):

			key, win = ip(win)

		key = prevKey

		c = 1

	return key, prevKey, c, win



def invalid_check(key, prevKey, snake):

	if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]: 						# If an invalid key is pressed

		key = prevKey

	if (key == KEY_UP and prevKey == KEY_DOWN) or (key == KEY_DOWN and prevKey == KEY_UP) or (key == KEY_LEFT and prevKey == KEY_RIGHT) or (key == KEY_RIGHT and prevKey == KEY_LEFT):

		key = prevKey																# Not opposite direction

	if ((snake[0][0] == 1 and snake[1][0] == 1) and key==KEY_UP) or ((snake[0][0] == 48 and snake[1][0] == 48) and key==KEY_DOWN) or ((snake[0][1] == 1 and snake[1][1] == 1) and key==KEY_LEFT) or ((snake[0][1] == 98 and snake[1][1] == 98) and key==KEY_RIGHT):

		key = prevKey

	return key, prevKey



def snk_inc(snake, key):

	# Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases regardless

	snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])



def boundary(snake, key, win):
	
	# Stop if snake heads straight towards boundaries

	c = 0

	if (snake[0][0] == 1 and key == KEY_UP) or (snake[0][0] == 48 and key == KEY_DOWN):

		while key not in [KEY_LEFT, KEY_RIGHT]:

			key, win = ip(win)

		c = 1

	if (snake[0][1] == 1 and key == KEY_LEFT) or (snake[0][1] == 98 and key == KEY_RIGHT):

		while key not in [KEY_UP, KEY_DOWN]:

			key, win = ip(win)

		c = 1

	return key, c, win



def death(snake):

	b = 0

	if snake[0] in snake[1:]:														# If snake runs over itself 
		
		b = 1
	
	return b



def eat(snake, food, win, score):

	if snake[0] == food:															# When snake eats the food

		food = []

		score += 1

		while food == []:

			calc_food(food) 						            					# Calculating next food's coordinates

			if food in snake:

				food = []

			win = print_food(food, win)

	else:
    
		last = snake.pop()                      					                # If it does not eat the food, length decreases

		win.addch(last[0], last[1], ' ')		

	return win, score, food




def print_snake(snake, win):

	win.addch(snake[0][0], snake[0][1], '#')

	return win



def cl_scr(): 

	curses.endwin()																	# Close the window



def print_fscore(score):

	print("Game over\nScore - " + str(score))



def wait(win):

	key=-1

	while key == -1:

		key, win = ip(win)

		if key == ord(' '):

			cl_scr()

			break

		key = -1

	return win

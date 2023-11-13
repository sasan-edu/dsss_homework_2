import random

def random_int_between(min, max):
    """generates Random integer.
	Arg: 
		min(int): minimum value of random number
		max(int): maximum value of random number
	Returns:
		int: random integer number between min and max
	"""
    return random.randint(min, max)


def random_operator():
	"""generates Random operator.
	Returns:
		str: string value of "+" or "-" or "*"
	"""
	return random.choice(['+', '-', '*'])


def do_math_operation(n1, n2, o):
	"""do the math operation
	Args:
		n1 (int): first integer number
		n2 (int): second integer number
		o (str): string value of the math operator
	returns:
		tuple:
			p (str): string of operation to print
			a (int): answer of the math operation
	"""
	p = f"{n1} {o} {n2}"
	if o == '+': a = n1 + n2
	elif o == '-': a = n1 - n2
	else: a = n1 * n2
	return p, a

def math_quiz():
	"""
	main function to run the quiz
	"""
	player_score = 0
	maximum_questions = 3
	
	print("Welcome to the Math Quiz Game!")
	print("You will be presented with math problems, and you need to provide the correct answers.")
	
	for _ in range(maximum_questions):
	    n1 = random_int_between(1, 10); n2 = random_int_between(1, 10); o = random_operator()
	    
	    PROBLEM, ANSWER = do_math_operation(n1, n2, o)
	    print(f"\nQuestion: {PROBLEM} = ?")
	    
	    #handling the input to be int value
	    while True:
	        useranswer = input("Your answer: ")
	        try:
	            useranswer = int(useranswer)
	        except ValueError:
	            print ("Valid number, please!")
	            continue
	        break
	    
	    if useranswer == ANSWER:
	        print("Correct! You earned a point.")
	        player_score += 1
	    else:
	        print(f"Wrong answer. The correct answer is {ANSWER}.")
	        
	print(f"\nWell Done! Your score is: {player_score}/{maximum_questions}")
	
if __name__ == "__main__":
    math_quiz()

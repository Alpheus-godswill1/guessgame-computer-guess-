## This is a python guess game played in which  the computer suggest the random number to match the players number and when such happens it is iterated again

- To get started with this amazing simple to learn python project 
-- `git clone -- `

- Secondly
 -- `import random` - the random function has several sub-methods but the one we are interested in is called `randint()`

- Thirdly,
-- define a function of your choice, though it is best practice to give it a name that represents your action e.g 
`def guess(b):` - b is a parameter you want to use later
`   random_numb = random.randint(1, b)` - now you are using both the random() prebuilt function and the 'b' parameter you declared initially

#### Now you want to make the computer iterate through every number you suggest -- that sounds like a  loop you are going to create

- so using while loop
`guessValue = 0`
`while guessValue != random_numb:`
    `guessValue = int(input(f'Guess the number of your choice from 1 to {b}:  '))` -- now this is converting the input to an integer.
#### Check for higher, lower, and correct guesses
`if guessValue > random_numb: ` - recall this checks are done and indented under the while loop, please note this
    `print('Hey pal, sorry your guess is too high, try again!')`
`elif guessValue < random_numb: ` - recall this checks are done and indented under the while loop, please note this
    `print('Hey pal, sorry your guess is too low, try again!')`

###### Now leave the while loop and go print out the correct guess

`print('Wow, you finally got the correct guess')`

### Call the function 
`guessNum(17)`







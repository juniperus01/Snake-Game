# Snake-Game
Python Gaming Project

This is probably one of the most famous mobile games that ever was, and it's definitely one of my favorite. Over a span of two days, I have built this super-addictive game using my knowledge on Object Oriented Programming (specifically Inheritance) and have used Turtle module in building the game as well.

It has, a moving snake, which you control using your keyboard, and you can move to catch food, then it grows in length as it eats more food. You have to make sure that you don't end up getting tangled or hitting the wall. The goal is to eat as much food as you can while staying alive. As always, when we're thinking about a complex problem, the first step is to break down the problem. Here, I have broke down this problem of building the snake game into seven separate steps.

1. Create a Snake: To create a snake body, I created consequtive three squares on the screen, all lined up next to each other.

2. Move the Snake: Next, I tried to figure out how to move the snake so that it continuously moves forward only and all we have to do is tell it to change direction. Here, turning the snake's body becomes a task. So, I first tried to turn and move the snake's head one step ahead in the desired direction, and then shifted the remaining squares to the previous positions the squares in front for each square respectively.

3. Control the Snake: Afterwards,I found out how to control the snake using keyboard controls.So you can use the up, left, down, and right arrow keys to move the snake across the screen.

4. Detect Collision with food: Next, I have created food for the snake, which is basically a small blue circle, that changes its position randomly (using Random module in Pythom) everytime the snakes collides with the food and subsequently eats it.

5. Detect Collision with collision: Then, the game shall end if the difference in the coordinates of the snake's head and the edges of the turtle screen is less than or equal to 5. At this point, the snake would collide with the wall and game is over.

6. Detect Collision with itself: As the snake's length increases by eating more and more food, its likely to get tangled and its head might collide with its body. At that point of time, the game will be over.

7. Scoreboard: Finally, I have also created a class to keep track of the scores, as and when snake eats the food or the game is over.    

# Chase-The-Market

Inspiration
Our group was inspired by the game Wordle and after some thinking we decided to use the concept of Wordle and apply it to something that seemed confusing to all of us, stocks.

What it does
Chase The Market is a game that allows players to see a 6 week graph of a particular company's stock and use the initially given 2 weeks to predict the trend of the following week. The user is shown a main menu with options of playing or looking at the instructions.

If the user clicks play then they can draw a prediction line using his or her mouse between the designated 2 white lines that show the area of user interaction. If the user tries to go outside of the boundary or does not draw a prediction line for the whole week, the line then erases causing the user to restart their prediction for that week.

Once the user is done, Chase The Market will show them the actual stock trend for that week as well as a matching percentage at the bottom right of the user interaction area. The matching percentage is essentially how many of the values graphed by the user's prediction line match or are close to that of the values graphed by the actual stock trend line. After the user is done with all 4 weeks of the game, the analytics button shows up at the bottom right hand side of the screen. When the user presses this button, they are taken to a page that provides some tips and tricks on how to improve their stock predicting skills.

The analytics page shows different tips depending on the average matching percentage of the user's 4 week predictions. The user can then press the back button located on the bottom left in order to get back to the main menu and from there can play the game again or exit the game.

How we built it
We built Chase the Market using Python and the Python open source module, Pygame.

For the backend of the game, the given stock prices are in an array and the weekly stock prices (to be predicted) are in a 2d array holding arrays containing the prices for each week. When the user selects play the game starts and allows them to begin drawing. Allowing the user to draw with their mouse was done by detecting mouse motion when the user has their left mouse button clicked and creating a line from the mouse’s previous position to its current.

For edge cases when the user is drawing, a boundary is formed about the allotted section intended for the user to draw in, moving their mouse beyond that point draws the line at the very edge of the boundary. If the user doesn’t reach the right edge of the boundary by the time they let go of their mouse button the program clears the drawing area in that section. Lastly, if the user tries to start the line drawing from a point further than the left edge of the boundary, a line is not formed.

While the line is being drawn. The y-axis pixel location of the mouse when drawing the line is being translated to its corresponding dollar amount and stored in an array.

Once the line has been formed, performance is evaluated by comparing the day-to-day values of the stock for that week section to the predicted values retrieved from the line, this performance is shown to the user as a percentage of how correct they were.

For the front end, we designed a button class that would control the content shown on the screen, the back button would return the user to the home screen, the play button would start the game as mentioned above, the analytics button (shown after completing the game) will gives feedback to the user about their performance, and the instructions button on the home page shows the user how to play the game.

Challenges we ran into
A lot of the major challenges we ran into dealt with the backend operations of this project. Specifically with how the user drawn prediction line can be translated into dollar values that can be compared to the actual stock trend values of the correct trend. We originally intended to use the plotting library MatPlotLib for this part of our project such that we can read in the stock data from a file input and as the user is graphing their prediction line, the program would read in those points and compare it with that of the actual stock values. However, this proved to be extremely difficult as we realized that MatPlotLib and Pygame cannot be used such that MatPlotLib is the backend or frontend operation for a Pygame project. After some group brainstorms we ended with the solution of figuring out the dollar value per pixel in the screen size that we controlled in order to get the actual dollar values of the user drawn prediction line. This was rather our largest challenge. Our second largest challenge dealt with enabling the user to draw a continuous line within a designated area. Through a lot of research, we were able to overcome this challenge by using the mouse position and mouse event aspects of Pygame.

Accomplishments that we're proud of
One accomplishment that our group is very proud of is that we were able to learn and successfully create a full fledged game using Python and Pygame without any prior experience in both technologies. We are especially proud of this accomplishment as there was a rather large learning curve with a really small window of time to get this project done and to be able to not only give it our best but end up with a final product that does what was expected was a rather large goal that we were able to achieve.

What we learned
Through this project, we learned a lot regarding python and pygame as our group is not very familiar with both of these technologies. We also learned how to learn about new tools under a time constraint as our group is not very familiar with python or the pygame module. We also learned about git, team coordination, and time management. While developing the game, we had to figure out how to utilize photoshop to add assets to our programs as well.

What's next for Chase The Market
Many of the features we would like to implement for Chase The Market are surrounding the analytical aspect of the game. We would like to add a section to the game that includes videos on tips and tricks on stock predictability so that the user can improve on their gameplay using the videos. We can expand this section by including the videos not only as a separate entity of the game but also in the analytics window by showing specific videos depending on the areas of the prediction line that have low matching percentages.

We would also like to make the game more expandable by enabling it to take in stock trend data and read in points and create a graph rather than hard coding it into the program. This particular improvement would most likely have to use MatPlotLib, a plotting library in python, in order to be able to process the points as well as create the graph. We would also like to pursue different styles with more popular and sophisticated chart viewings such as candlesticks as well as make the general UI experience smoother.

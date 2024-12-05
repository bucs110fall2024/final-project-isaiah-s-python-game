# Ultimate Pie Clicker! 
## CS110 Final Project S1, 2024
## Team Members
Isaiah Gabbay

## Project Description
Creates a game where the objective is to click on the pie in the center of the screen. The player can purchase modules which increase the passive score per second, which starts at 0. Random boosters also spawn on the screen, which gives the user a random effect with weighted randomness from a pool of effects. The objective is to get as high a score as possible, which is saved in a database.
## GUI Design

### Initial Design
![initial gui](assets/firstgui.jpg)
### Final Design
![final gui](assets/finalgui.jpg)


### Features
1: Pie that adds a specified amount to score when clicked
2: Text on top which gives score from clicks and buildings
3: Buildings that gives users upgrades when clicked, either increasing the power of the click or increasing non-clicking score
4: Diamond cookies that appear and give random effects if clicked
5. Highscore feature that saves highest score even after game is closed.
## ATP
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
| 1                    |:Run controller.py:|GUI window appears with the pie and background displayed:|
| 2                    |:Click on the pie:|Message appears on pie "+1 score:|
| 3                    |:Observe the score:|Score initially increases by 1 on each click of the pie |
| 4                    |:Click anywhere besides the pie:|No response from program:|
| 5                    | Wait for boost to appear|Boost appears on screen with asset loaded|
| 6                    | Purchase an oven | Upgrade is purchased, score decreases by the 100 |
| 7                    | Observe the CPS display | CPS increases based on the purchased upgrade |
| 8                    | Click on the boost | Boost effect is applied, and score or CPS updates accordingly |
| 9                    | Check the high score display | High score updates if the current score exceeds it |
| 10                   | Reach 5000 points | Score, cps, and multiplier should change color|
| 10                   | Close the game window | The game exits without errors |
| 11                   | Reopen game | High score from last game appears |













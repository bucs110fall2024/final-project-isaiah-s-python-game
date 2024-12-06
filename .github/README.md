# Ultimate Pie Clicker! 
## CS110 Final Project S1, 2024
## Team Members
Isaiah Gabbay

## Project Description
Creates a game where the objective is to click on the pie in the center of the screen. The player can purchase modules which increase the passive score per second, which starts at 0. Random boosters also spawn on the screen, which gives the user a random effect with weighted randomness from a pool of effects. The objective is to get as high a score as possible, which is saved in a database.
## GUI Design

### Initial Design
![initial gui](/assets/firstgui.png)
### Final Design
![final gui](/assets/finalgui.png)


### Features
1: Pie that adds a specified amount to score when clicked
2: Text on top which gives score from clicks and buildings
3: Buildings that gives users upgrades when clicked, either increasing the power of the click or increasing non-clicking score
4: Diamond cookies that appear and give random effects if clicked
5. Highscore feature that saves highest score even after game is closed.
### Classes
Controller: Controls the game
Pie: Generates and controls the pie object in the center of the screen
Randomobjects: Controls the "diamond pies" which 
## ATP
| Step | Procedure                                            | Expected Results                                           |
|------|------------------------------------------------------|-----------------------------------------------------------|
| 1    | Start the game and click the pie                    | Score increases by 1 on each click                        |
| 2    | Click anywhere besides the pie, boosts, or upgrades                    | Nothing happens                        |
| 3    | Wait for a boost to appear and click it             | Boost effect is applied, updating score or PPS as intended|
| 4    | Activate the five times multiplier boost and click the pie again | Score increases by 2 per click                           |
| 5    | Purchase an upgrade that increases score            | Score increases by the amount specified by the upgrade    |
| 6    | Attempt to purchase an upgrade and observe the message | "Upgrade purchased" message displays for 0.25 seconds and then disappears |
| 7    | Attempt to purchase an upgrade without enough pies  | "Not enough pies" message displays for 0.25 seconds and then disappears |
| 8    | Observe the PPS display after purchasing upgrades   | PPS updates correctly based on purchased upgrades         |
| 9    | Check the high score display when score increases   | High score updates if the current score exceeds it        |
| 10   | Reach 5000 pies                                     | Color of stat trackers changes                            |



















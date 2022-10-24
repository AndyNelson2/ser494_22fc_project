#### SER494: Exploratory Data Munging and Visualization
#### NFL 3rd and 4th down analysis
#### Andy Nelson
#### October 23, 2022

## Basic Questions
**Dataset Author(s):** ESPN

**Dataset Construction Date:** September 8 - October 20

**Dataset Record Count:** 179

**Dataset Field Meanings:** Third down position, third down play, fourth down position, fourth down play

**Dataset File Hash(es):** https://www.espn.in/nfl/playbyplay/_/gameId/401437791

## Interpretable Records
### Record 1
**Raw Data:** Left: 105 Middle: 99 Right: 121 Average


Interpretation:** This shows the distribution of which part of the field was targeted on third and fourth downs. 

### Record 2
**Raw Data:** Average 3rd down: 6.0 Average 4th down: 4.1

**Interpretation:** The average fourth down is going to be lower than third since every team will run a play on third down despite how far away they are from the first down but on fourth down if they are super far away they are more inclined to not go for it so the average is 50% shorter. 

## Data Sources
### Transformation N
**Description:** 

The original data pulled from ESPN had all plays so I only kept the ones that were a third down followed by a fourth down. 
I am only interested in the plays where the team goes for it on fourth down so I took out all of the third and fourth down pairs where on fourth down the team kicked a field goal or punted. 
Then I had to extract the distance from the first down. For most data points this is simple since it says, for example, '3rd & 8' so it's 8 yards. But for plays within 10 yards of the goal line it displayed '3rd & Goal' so I then had to check the position on the field to see how far they were from scoring. 


**Soundness Justification:** TODO

(duplicate above as many times as needed; remove this line when done)


## Visualization
### Visual N
**Analysis:** TODO

(duplicate above as many times as needed; remove this line when done)

The data came from ESPN. Each set of the plays was recorded the same day as the game was played. Each game varies in how many fourth downs occur. Some games have zero fourth downs while others can have upwards of ten. 
Each row in data.txt has four sections. The first is the downs for the third down play, the second is the description for the play ran on that third down, then the third and fourth are the same but for fourth down. 
Data.txt contains all of the third and fourth down plays where the team went for it on fourth for the current NFL season. 

For explaining of the two records I'll just use the first two lines in data.txt. They are both from the Thursday night game between Arizona and New Orleans this year. The first line shows that the down is 3rd and 7 yards to go until the first down. Then the play on that down is described in the next line where K. Murray threw a pass to Z.Ertz for 6 yards. Because only 3rd/4th down pairs are in the data set we know that wasn't enough for a first down so the second half is the fourth down play. It's now 4th and 1 yard to go and K.Murray this time runs the ball for two yards gaining the first down. 

There is a lot of extra information also in the text which I'm not sure I'll include in my analysis yet. In the second line, for example, you can see it says 'no huddle, shotgun' which just shows that the quarterback didn't start under center which telegraphs that it will most likely be a passing play. No huddle means the offense called the play very fast and didn't give the defense much time to reset. 'Pushed ob' shows that the player with the ball wasn't tackled but was forced to go out of bounds. 

5e16381a120f4d9322eb039418fa8dbb - this is the MD5 has for the most recent game played in the data set. I just incremented the game ID at the end by negative one to loop through every game that has happened. 

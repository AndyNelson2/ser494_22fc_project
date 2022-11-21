#### SERX94: Experimentation
#### NFL 3rd and 4th down analysis
#### Andy Nelson
#### November 20, 2022


## Explainable Records
### Record 1
**Raw Data:** 91% of yardage needed gained on third down leads to a 75% chance of converting fourth down. 

Prediction Explanation:** The prediction (shown in y_precicted_1 visual) predicts a 63% chance of converting after gaining 91% of needed yards. This makes sense to me because often if a team is very close to a first down they will always do a run play and the defense knows this so they defend heavily for it so it often comes down to who has the better line play with a slight advantage to the offense since they can choose to run in the direction they feel is less protected against. So while it seems like only needing to go 9% of the distance on fourth down would be more common than 63%, often times getting a tiny amount of yards can be harder than 3-4 yards. 

### Record 2
**Raw Data:** 46% of yardage needed gained on third down leads to a 100% chance of converting fourth down. 

Prediction Explanation:** The model predicts only a 22% chance of gaining a first down if 46% of yards are gained on third down. The raw data is actually an outlier as there has only been one play this season where a team got 46% of needed yards and they happened to convert on fourth down the following play. The outlier didn't appear to skew the data too much though since the predicted 22% chance is much closer to what makes sense for the situation. If a team doesn't even get half of the yards needed and they still decide to go for it then it must be a desperate play late in the game where they have to go for it no matter what. Which would lead to a low success rate. 

## Interesting Features
### Feature A
**Feature:** the outlier points near the tops of the graphs that show 100%

**Justification:** These points skew the trend line up and wouldn't be 100% if there was more data. If a point shows 100% then I'll set it to a random number and then do the testing and training on it to see how it affects accuracy. 

### Feature B
**Feature:** the outlier points near the bottom of the graphs that show 0%

**Justification:** These are outliers but I think these won't have as big of an effect as feature A beacuse fourth down success is usually below 50% so putting in zeros will be more forgiving than 100%. For these I will also set the data point to a random percentage and see how MSE changes. 

## Experiments 
### Varying A
**Prediction Trend Seen:** The data certainly seems more believable without all the noise at the top of the graph. The feature B outliers have more of a pull but MSE dropped to .108 which is much better than anything I saw from tests on the standard data. 

### Varying B
**Prediction Trend Seen:** The points at zero percent were randomized but it seems like they often were very high or low values so the trend wasn't skewed too much. MSE was at .225 for the graph which is actually a bit worse than what I normally saw on tests conducted on the normal data set. 

### Varying A and B together
**Prediction Trend Seen:** This chart doesn't show too much. I think varying A and B together make too many points random so the trend line actually went down on this graph which doesn't make sense. The more yards a team gains on the first play should increase their odds of getting the first down on the following play but with so many points assigned random values they overpowered the unchaged data. 
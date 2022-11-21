#### SERX94: Machine Learning Evaluation
#### TODO NFL 3rd and 4th down analysis
#### TODO Andy Nelson
#### TODO November 20, 2022

## Evaluation Metrics
### Metric 1
**Name:** Linear Regression

**Choice Justification:** The data was scattered with a general trend upwards. No parabolic or more exotic curve appeared in the data so a straight line fit the data well.

Interpretation:** The method predicted as suspected where the closer a team got to the first down marker on third down then the more successful they were securing a new set of downs on the following play. If third down was a failure then teams only convert around 30% of the time then that number trends towards 100% when nearly all the yardage needed is obtained in the first try.

### Metric 2
**Name:** Mean Squared Error

**Choice Justification:** The data was all relatively close together so a couple points wouldn't significantly skew the metric one way or another. 

Interpretation:** With several different sets of training and test data the MSE was always around 12%-15%. So the model would predict results fairly accurately and I'm sure the model would get more precise the more data is fed into it. 

## Alternative Models 1
### Alternative 0.005249344848808383x + 0.13705832290961395 
**Construction:** randomize entire set and distribute 80% to training and 20% to testing. 

**Evaluation:** TODO

## Alternative Models 2
### Alternative 0.008994759695475982x - 0.17857470510849516
**Construction:** randomize entire set and distribute 80% to training and 20% to testing. 

**Evaluation:** TODO

## Alternative Models 3
### Alternative 0.006766712183005826x + 0.07211295286496722
**Construction:** randomize entire set and distribute 80% to training and 20% to testing. 

**Evaluation:** MSE for all of them were very close (between 1% of each other). The second model was the only onw with an x intercept below zero. I believe that to be the case because the 0 data point was not included in the training set and that point contains over 30% of all the initial data so it is quite heavily weighted. But even without it the model still had a very similar MSE and slope to the other models. 


## Visualization
### Visual 1
**Analysis:** This was my best model in terms of lowest MSE. I didn't have as much data as I would have liked so there are some messy points in there which are the ones at the very top or bottom. If I had more seasons of data I'm sure those would regress to the mean closer. 

## Visualization
### Visual 2
**Analysis:** This was my worst model with an MSE over .2. As you can see there are a lot of the outliers with only one or two data points for them. With the vast majority of plays being within 1-9 yards there aren't very many percentages that are likely so the rarer ones have much less data contributing for them. 
(duplicate above as many times as needed; remove this line when done)

## Best Model

**Model:** Model 1 with an MSE of0.14242900097265093
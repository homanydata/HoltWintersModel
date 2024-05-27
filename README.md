# HoltWintersModel
This project aims to implement time-series analysis triple exponential smoothing, better known as Holt Winters model.

## This project includes:
### 1- [winters](./winters.py):
Includes a class that represents winters model, with methods:
- train: Creates & saves the different basic components (level, trend, seasonality, forecasted) values for each point in the dataset.
- forecast: Calculates forecatsed values for the number of seasons the user wants, using previously calculated components while training.
- score: Calculates errors for the model based on calculated components.


### 2- [others](./others.py):
- Implementation of Linear interpolation
- Moving average
- MAD, MSD, M%D

### 3- [Recursive](./recursive.py):
Includes a alternative recursive implementation of winters model forecasting. Surely it is slower than the iterative approach because it adds over redundant repetitive calculations.

### 4- [dp](./dp.py):
Improves over recursive implementation by adding memoization, thus enhancing performance and avoiding repetitive calculation.
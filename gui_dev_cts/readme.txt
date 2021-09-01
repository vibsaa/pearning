for calculating k/eta:
first run the cts_version_7 theres your actual graph with datapoints
and 20th order polynomial fit

then from the datapoints file remove 0,0 points and run data_cleaning file
from there you will get log(id ) vs vd graph and value of slope with line fitted to 
the graph

in the same file or v7 file use the obtained fit parameters to obtain the 
linear fit in the ac data pointrs graph


************************************PART-II*******************************************************
import the datapoints in the points.txt file.
just run data_cleaning.py file :
    1. it will first obtain datapoints.txt and logpoints.txt
    2. the will remove -inf points from logpoints 
    3. the plot both graph in the same window and give eta value
from sklearn import datasets, linear_model
from ggplot import *

# Load the diabetes dataset
diabetes = datasets.load_diabetes()


p = ggplot(mtcars, aes('mpg', 'qsec')) + \
    geom_point(colour='steelblue')

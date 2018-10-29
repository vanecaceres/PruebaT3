import numpy as np
import csv
import matplotlib.pyplot as plt
from io import StringIO


datos = open("WDBC.dat", "r", usecols = (1,2,3,4), skip_header = 0, delimiter = ",")

print (datos)

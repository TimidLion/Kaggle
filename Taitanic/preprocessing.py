import pandas as pd
import numpy as np

class DataFrame():
	def __init__(self, file_name):
		f = open("Data/"+file_name+".csv")
		self.dataframe = pd.read_csv(f)
		f.close()

	def __repr__(self):
		return "{}".format(self.dataframe)

if __name__ == "__main__":
	train = DataFrame('train')
	test = DataFrame('test')
	ex_submit = DataFrame('gender_submission')
	print(train)

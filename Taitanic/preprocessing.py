import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataFrame():
	def __init__(self, file_name):
		f = open("Data/"+file_name+".csv")
		self.df = pd.read_csv(f)
		f.close()
		self.columns = self.df.columns

	def __repr__(self):
		return "{}".format(self.df)

	def pick_columns(self):
		del self.df['Name']
		del self.df['Ticket']
		del self.df['PassengerId']

		# If male 0 else 1
		self.df['Sex'] = [ 1 if sex == 'male' else 0 for sex in self.df['Sex']]

		self.df['Cabin'] = [1 if cabin else 0 for cabin in self.df['Cabin'].isnull() ]
		self.df['Embarked'] = self.df['Embarked'].fillna('S')
		self.df['Embarked'] = self.df['Embarked'].map( {'S': 0, 'C': 1, 'Q': 2} ).apply(lambda x : int(x))
		self.df['Families'] = self.df['SibSp'] + self.df['Parch']
		
		del self.df['SibSp']
		del self.df['Parch']
		self.columns = self.df.columns

		self.df['Survived'].fillna(0)
		self.df['Age'].fillna(int(self.df['Age'].mean()))
		print(self.df.loc[[0]])

	def show_corr(self):
		colormap = plt.cm.RdBu
		plt.figure(figsize(14,12))
		plt.title('Pearson Correlation of Features', y=1.05, size=15)
		sns.heatmap(self.df.astype(float).corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)

if __name__ == "__main__":
	train = DataFrame('train')
	test = DataFrame('test')
	ex_submit = DataFrame('gender_submission')
	#print(train)
	train.pick_columns()
	train.show_corr()

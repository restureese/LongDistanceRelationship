import random


class NeuralNetwork(object):
	"""Backpropagation Neural Network"""


	def __init__(self, epoch,learning_rate,hidden):
		self.epoch = epoch
		self.hidden = hidden
		self.h = {}
		self.w = {}
		self.b = {}
		self.learning_rate = learning_rate
		self.error = 0

	def inisialisasi_bobot(self, input):
		for i in range(len(input[0])):
			for j in range(self.hidden):
				self.w[str(i)+str(j)] = random.random()

	def inisialisasi_hidden(self):
		for x in range(self.hidden):
			self.h[str(x)] = 0

	def forward(self,X,Y):
		''' Fungsi Untuk menghitung galat maju '''
		for index,x in enumerate(X):
			for i in range(self.hidden):
				self.h.update({str(i):self.h.get(str(i))+(self.w.get(str(x)+str(i))*x)})


	def train(self, input,label):
		self.inisialisasi_bobot(input)
		self.inisialisasi_hidden()
		epoch = 0

		#perulangan tiap inputan dan target
		for X, y in zip(input,label):
			#selagi error lebih dari learning 
			# while self.error < 0.5 or epoch > self.epoch:
				self.forward(X,y)

			

X = [[1,1,1],[2,2,2]]
y = [1,2]
epoch = 10
learning_rate = 0.1
hidden = 6

nn = NeuralNetwork(epoch=epoch,learning_rate=learning_rate,hidden=hidden)
nn.train(X,y)
for i in sorted(nn.w.keys()):
	print('W{0}\t: {1}'.format(i,nn.w.get(i)))
print()

for i in sorted(nn.h.keys()):
	print('H{0}\t: {1}'.format(i,nn.h.get(i)))
		
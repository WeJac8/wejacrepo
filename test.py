


class MyInt:
	__value = None
	def __init__(self,value): 
		self.value = value
	def __len__(self):
		return len( str(self.value) )
	@staticmethod
	def test_() -> (int,str):
		pass
class MyInt2(MyInt):
	pass
import  sys
if __name__ == '__main__':
	print(isinstance(MyInt2(10),MyInt))
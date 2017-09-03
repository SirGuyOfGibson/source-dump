class Dumpster():
	
	NAME_SIZE = 10
	EXT_SIZE = 4

	def __init__(self):
		self.header = b''
		self.header_size = 0
		self.num_children = 0					#[0, 255]
		self.mem_addresses = []
		self.is_file = False
		self.name = ''
		self.extension = 'dmp'	

		self.init_header()

	def to_bytes(self):
		if self.is_file:
			cmd = 128
		else:
			cmd = 0

		self.header_size = 4 + num_children*4 + NAME_SIZE + EXT_SIZE				#Size of headerr in bytes

		hs = hex(self.header_size)

		n = len(hs)-2

		if n == 1:
			a = 0
			b = hs[3]
		if n == 2:
			a = 0
			b = hs[3:5]
		if n == 3:
			a = hs[3]
			b = hs[4:6]
		if n == 4:
			a = hs[3:5]
			b = hs[5:7]

		header_array = [cmd,a,b,self.num_children]



		#Adding filename bytes to header array

		filename_array = bytearray(self.name,'utf-8')
		s = len(filename_array)

		for i in range(0,NAME_SIZE-s):
			header_array.append(0)

		for i in range(0,s):
			header_array.append(filename_array[s])



		
		#Adding extension bytes to header array

		extension_array = bytearray(self.extension,'utf-8')
		s = len(extension_array)

		for i in range(0,EXT_SIZE-s):
			header_array.append(0)

		for i in range(0,s):
			header_array.append(extension_array[s])

		return header_array

	def write_to_dump(self):
		with open(self.name+'.'+self.extension, 'wb') as dump:
			dump.write(self.to_bytes())

	def read_from_dump(self):
		with open(self.name+'.'+self.extension, 'rb') as dump:
			for line in dump:
				for byte in line:
					print(byte + '\n')


		







		
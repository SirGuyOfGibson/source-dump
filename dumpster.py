class Dumpster():

	NAME_SIZE = 10
	EXT_SIZE = 4
	UTF_SPACE = 32

	def __init__(self,name):
		self.header = b''
		self.header_size = 0
		self.num_children = 0					#[0, 255]
		self.mem_addresses = []
		self.is_file = False
		self.name = name
		self.extension = 'dmp'

	def to_bytes(self):
		if self.is_file:
			cmd = 128
		else:
			cmd = 0

		self.header_size = 4 + self.num_children*4 + Dumpster.NAME_SIZE + Dumpster.EXT_SIZE				#Size of headerr in bytes

		hs = hex(self.header_size)

		n = len(hs)-2

		if n == 1:
			a = '0'
			b = hs[2]
		if n == 2:
			a = '0'
			b = hs[2:4]
		if n == 3:
			a = hs[2]
			b = hs[3:5]
		if n == 4:
			a = hs[2:4]
			b = hs[3:6]

		header_array = [cmd,int(a, 16),int(b, 16), self.num_children]

		#Adding filename to header array

		filename_array = bytearray(self.name,'utf-8')
		s = len(filename_array)

		for i in range(0,Dumpster.NAME_SIZE-s):
			header_array.append(Dumpster.UTF_SPACE)

		for i in range(0,s):
			header_array.append(filename_array[i])




		#Adding extension bytes to header array

		extension_array = bytearray(self.extension,'utf-8')
		s = len(extension_array)

		for i in range(0,Dumpster.EXT_SIZE-s):
			header_array.append(Dumpster.UTF_SPACE)

		for i in range(0,s):
			header_array.append(extension_array[i])

		return bytearray(header_array)


	#Takes the dmp file and creates a dumpster object
	def from_bytes(dmp):
		dumpster = Dumpster(dmp.strip(".dmp"))		#Lower case dumpster is object. Objects are lower case. Always
		b = Dumpster.read_from_dump(dmp)
		file_flag = b[0]
		dumpster.is_file = file_flag>>7 and 1
		dumpster.header_size = int(b[1])*256 + int(b[2])
		dumpster.num_children = int(b[3])

		n = ''
		e = ''

		for i in range(4,Dumpster.NAME_SIZE + 4 + Dumpster.EXT_SIZE):
			if i < Dumpster.NAME_SIZE + 5:
				if b[i] == 32:
					pass
				else:
					n += chr(b[i])
			else:
				if b[i] == 32:
					pass
				else:
					e += chr(b[i])

		dumpster.name = n
		dumpster.extension = e

		return dumpster


	def write_to_dump(self):
		with open(self.name+'.'+self.extension, 'wb') as dump:
			dump.write(self.to_bytes())

	def read_from_dump(dmp):
		bytelist = []
		with open(dmp, 'rb') as dump:
			for line in dump:
				for byte in line:
					bytelist.append(byte)
		return bytelist












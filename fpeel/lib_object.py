class LibObject:
    def __init__(self, filename):
        self.filename = filename
        print("Welcome to the class!")
        print("The file name is {}".format(self.filename))
        fo = open(self.filename, 'rb')
        self.data = fo.read()
        fo.close()

    def _dump(self):
        print(self.data.hex())

    def _read(self, count):
        fo = open(self.filename, 'rb')
        dwords = []
        fo.seek(8)
        for n in range(count):
            dwords.append(fo.read(4))
        fo.close()
        print(dwords)

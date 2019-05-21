#hash map using open addresing

class Hashmap:

    def __init__(self):

        self.size = 6
        self.map=[None for _ in range(0,self.size)]

    def hashval(self,key):

        h=0
        for c in str(key):
            h += ord(c)

        return h % self.size

    def add(self,key,value):

        index = self.hashval(key)
        kv=[key,value]

        if (self.map[index] == None):

            self.map[index] = kv

            return True

        else:

            for a in self.map :
                if a != None:
                    if a[0] == key:

                        a[1] =value
                        return True
            for i in range(0,len(self.map)):

                index = (index+5)%self.size
                if self.map[index] == None :
                    self.map[index] =kv
                    return True
                
    def get(self,key):

        index = self.hashval(key)

        if self.map[index][0] == key:

            print(self.map[index][1])
        else:

             for i in range(0,len(self.map)):

                index = (index+5)%self.size
                if self.map[index][0] == key :
                    print(self.map[index][1])
                    return True

    def delete(self,key):

        index = self.hashval(key)

        if self.map[index][0] == key:

            self.map[index] = None
        else:

             for i in range(0,len(self.map)):

                index = (index+5)%self.size
                if self.map[index][0] == key :
                    self.map[index] = None
                    return True

    def print(self):

        print(self.map)



h = Hashmap()
h.add('Bob', '567-8888')
h.add('Ming', '293-6753')
h.add('Ming', '333-8233')
h.add('Ankit', '293-8625')
h.add('Aditya', '852-6551')
h.add('Alicia', '632-4123')
h.add('Mike', '567-2188')
h.add('Aditya', '777-8888')
h.print()		
h.delete('Bob')
h.print()
     

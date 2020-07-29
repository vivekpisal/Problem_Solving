class Trie:
    head={}
    def add(self,word):
        cur=self.head

        for ch in word:
            if ch not in cur:
                cur[ch]={}
            cur=cur[ch]
        cur['*']=True
        print(self.head)

    def search(self,word):
        cur=self.head

        for ch in word:
            if ch not in cur:
                return False
            cur=cur[ch]
        if '*' in cur:
            return True
        else:
            return False

d=Trie()
d.add('hello')
d.add('hey')
d.search('hey')
d.add('vaishnavi')
d.add('vivek')
d.add('vaivi')

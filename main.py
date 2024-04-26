class InMemoryDB:

    def __init__(self):
        self.transaction = False
        self.dictDB = {}
        self.tempDB = {}

    def begin_transaction(self):
        self.transaction = True
        self.dictDB = {}
        self.tempDB = {}

    def put(self,key,value):
        if self.transaction:
            self.tempDB[key] = value
        else:
            raise Exception("Transaction not started")

    def get(self, key):
        if key in self.dictDB.keys():
            print(self.dictDB[key])
            return self.dictDB[key]
        else:
            print("null")

    def commit(self):
        if self.transaction:
            self.dictDB = self.tempDB
        else:
            return

    def rollback(self):
        if self.transaction:
            self.tempDB = self.dictDB
            self.dictDB = self.dictDB
        else:
            return

inmemoryDB = InMemoryDB()
inmemoryDB.get('A') # returns null
#inmemoryDB.put('A', 5) # calls exception 
inmemoryDB.begin_transaction()
inmemoryDB.put('A', 5)
inmemoryDB.get('A') # returns null
inmemoryDB.put('A', 6)
inmemoryDB.commit()
inmemoryDB.get('A') # returns 6 
inmemoryDB.commit()
inmemoryDB.rollback()
inmemoryDB.get('B') # returns null
inmemoryDB.begin_transaction()
inmemoryDB.put('B', 10) 
inmemoryDB.rollback()
inmemoryDB.get('B') # returns null


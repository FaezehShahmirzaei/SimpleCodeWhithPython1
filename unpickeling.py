import pickle
import dill

class User():
    def __init__(self, id, firstname, lastname, phone):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone

    def __repr__(self):
        return f"{self.id} : {self.firstname}  {self.lastname} <{self.phone}>"

    @staticmethod
    def unpickle_database(filename):
        with open(filename, 'rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

    def pickleing(self, filename):
        with open(filename, 'ab') as f:
            pickle.dump(self, f)

    @staticmethod
    def store_user_in_list( filename):
        users = list(User.unpickle_database(filename))
        users.sort(key =lambda user : user.id )
        return users

    @staticmethod
    def select_user_phone( filename):
        users = list(User.unpickle_database(filename))
        users.sort(key =lambda user : user.phone )
        selected_user = [user for user in users if str(user.phone)[0:3]=='919']
        return selected_user

    def fullname(self):
        newstr= self.firstname+self.lastname
        return newstr

    @staticmethod
    def usernames(filename1, filename2):
        lst=list(User.unpickle_database(filename1))
        with open(filename2, 'ab') as f:
            dill.dump(lst ,f)


    @staticmethod
    def write_to_file(mylist, filename):
        for i in mylist:
            i.pickleing(filename)


# u1 = User(1, 'f1', 'l1', 911333)
# u2 = User(2, 'f2', 'l2', 912333)
# u3 = User(3, 'f3', 'l3', 91933)
# u4 = User(4, 'f4', 'l4', 919555)
#
# u1.pickleing('users.pickled')
# u2.pickleing('users.pickled')
# u3.pickleing('users.pickled')
# u4.pickleing('users.pickled')

print(list(User.unpickle_database('users.pickled')))
l1=User.select_user_phone('users.pickled')
User.write_to_file (l1,'output-q-3-2.txt')
l2=User.store_user_in_list('users.pickled')
User.write_to_file (l1,'output-q-3-1.txt')

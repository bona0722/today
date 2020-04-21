# ```Python
# (has_been_viewed, from_number, time_arrived, text_of_SMS)
# ```

# Write the class, create a message store object, write tests for these methods, and implement the methods.

# Getting the current time. For example, 


import time
time_stamp = time.time() # get the current time in seconds since Epoch


class SMS_store:

    def __init__(self):
        self.inbox = list()

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.message = (False, from_number, time_arrived, text_of_SMS)
        self.inbox.append(self.message)

    def message_count(self):
        return len(self.inbox)

    def get_unread_indexes(self):
        msg = list()
        for i in self.inbox:
            if(i[0] == False):
                msg.append(self.inbox.index(i))
        return msg

    def get_message(self, i):
        tmp = list(self.inbox[i])
        tmp[0] = True
        self.inbox[i] = tuple(tmp)
        return f'{self.inbox[i][1], self.inbox[i][2], self.inbox[i][3]}'

    def delete(self, i):
        del self.inbox[i]

    def clear(self):
        self.inbox = list()

if __name__ == "__main__":
    my_inbox = SMS_store()

    my_inbox.add_new_arrival("010-1234-5678",time.ctime(time_stamp), "hello")
    my_inbox.add_new_arrival("010-0000-0000",time.ctime(time_stamp), "my name")
    my_inbox.add_new_arrival("010-0000-0020",time.ctime(time_stamp), "is")
    my_inbox.add_new_arrival("010-0000-0030",time.ctime(time_stamp), "hojung")
    my_inbox.add_new_arrival("010-0000-0040",time.ctime(time_stamp), "bye")
    
    print(my_inbox.get_unread_indexes()) 
    print(my_inbox.message_count())
    print(my_inbox.get_message(2))
    print(my_inbox.get_unread_indexes())
    print(my_inbox.message_count())
    my_inbox.delete(2)
    print(my_inbox.get_unread_indexes())
    print(my_inbox.message_count())
    print(my_inbox.get_message(1))
    print(my_inbox.get_unread_indexes())
    print(my_inbox.message_count())
    my_inbox.clear()
    print(my_inbox.get_unread_indexes())
    print(my_inbox.message_count())
    
    

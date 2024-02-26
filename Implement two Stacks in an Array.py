#Implement two Stacks in an Array
# here we start both stacks from left side
# create class two stack 
class TwoStack:
    # constructor 
    def __init__(self, n):
        # size
        self.size = n
        # initiate array
        self.array = [None]*n
        # initiate head1 for first stack
        self.head1 = None
        # initiate head2 for second stack
        self.head2 = None
    # define push to first stack function
    def push1(self, data):
        #check if stack 1 empty
        if self.head1 is None:
            # assign head1 to be 0 
            self.head1 = 0
            # use head1 as index and assign value to array
            self.array[self.head1] = data
        else:# else check if stack not full
            if (self.head1 + 1) < (self.size // 2):
                # we assign head to next index
                self.head1 += 1
                # use head1 as index and assign value to array
                self.array[self.head1] = data
            else:# if stack full
                print("Stack Overflow by element : ", self.array[self.head1])
    # define push to second stack function
    def push2(self, data):
        #check if stack 2 empty
        if self.head2 is None:
            # assign head2 to be 0 
            self.head2 = self.size // 2
            # use head2 as index and assign value to array
            self.array[self.head2] = data
        else:# else check if stack not full
            if (self.head2 + 1) < (self.size ):
                # we assign head to next index
                self.head2 += 1
                # use head2 as index and assign value to array
                self.array[self.head2] = data
            else:# if stack full
                print("Stack Overflow by element : ", self.array[self.head2])
    # define pop function for stack1
    def pop1(self):
        # check if stack1 is empty
        if self.head1 is not None:
            # assign head1 to variable 
            x = self.array[self.head1]
            # delete data from array
            self.array[self.head1] = None
            # check if head1 == 0 will be None because it's last index 
            if self.head1 == 0:
                self.head1 = None
            else:
                self.head1 -= 1
            return x
    # define pop function for stack2
    def pop2(self):
        # check if stack2 is empty
        if self.head2 is not None:
            # assign head2 to variable 
            x = self.array[self.head2]
            # delete data from array
            self.array[self.head2] = None
            # check if head2 == 0 will be None because it's last index 
            if self.head2 == self.size //2:
                self.head2 = None
            else:
                self.head2 -= 1
            return x


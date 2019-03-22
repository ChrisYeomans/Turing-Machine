#! usr/bin/python

"""
Takes a 100 bit string of 1s and 0s. The first 70 bits
define the machine states 10 bites for each state.
The first 5 bits of a state define what to do if it gets
a 0 and the next 5 a 1. The first 3 bits of the 5 determine
what state to move to next, ie 010 moves to the second
state. The 4th bit defines where a 0 or a 1 should be
written and the 5th bit determines whether to move left
or right within the programm. The final 30 bits are the
programm. If the machine moves to state 000 it halts.
"""
class Machine():
    def __init__(self, bit_string, prog_string_10):
        self.bit_string = bit_string
        self.prog_string_10 = prog_string_10
        self.active_state = 1
        self.prog_ticker = 0
        self.state_1 = State(bit_string[0:10], 1)
        self.state_2 = State(bit_string[10:20], 2)
        self.state_3 = State(bit_string[20:30], 3)
        self.state_4 = State(bit_string[30:40], 4)
        self.state_5 = State(bit_string[40:50], 5)
        self.state_6 = State(bit_string[50:60], 6)
        self.state_7 = State(bit_string[60:70], 7)

    def move_ticker(self, dirn):
        """
        Moves the ticker, used by get_out_string()
        """
        if dirn == 0:
            if self.prog_ticker != 0:
                self.prog_ticker-=1
        elif dirn == 1:
            if self.prog_ticker != 9:
                self.prog_ticker+=1

    def get_out_string(self):
        """
        Checks all states and appends to the
        output list and moves tickers accordingly.
        """
        self.out_string = []
        for i in range(1000):
            #print(self.active_state)
            if self.active_state == 1:
                if int(self.prog_string_10[self.prog_ticker]) == 0:
                    self.active_state = self.state_1.move_state_zero
                    self.out_string.append(self.state_1.write_zero)
                    self.move_ticker(self.state_1.move_prog_zero)
                elif int(self.prog_string_10[self.prog_ticker]) == 1:
                    self.active_state = self.state_1.move_state_one
                    self.out_string.append(self.state_1.write_one)
                    self.move_ticker(self.state_1.move_prog_one)
                    
            elif self.active_state == 2:
                if int(self.prog_string_10[self.prog_ticker]) == 0:
                    self.active_state = self.state_2.move_state_zero
                    self.out_string.append(self.state_2.write_zero)
                    self.move_ticker(self.state_2.move_prog_zero)
                elif int(self.prog_string_10[self.prog_ticker]) == 1:
                    self.active_state = self.state_2.move_state_one
                    self.out_string.append(self.state_2.write_one)
                    self.move_ticker(self.state_2.move_prog_one)

            elif self.active_state == 3:
                if int(self.prog_string_10[self.prog_ticker]) == 0:
                    self.active_state = self.state_3.move_state_zero
                    self.out_string.append(self.state_3.write_zero)
                    self.move_ticker(self.state_3.move_prog_zero)
                elif int(self.prog_string_10[self.prog_ticker]) == 1:
                    self.active_state = self.state_3.move_state_one
                    self.out_string.append(self.state_3.write_one)
                    self.move_ticker(self.state_3.move_prog_one)

            elif self.active_state == 4:
                if int(self.prog_string_10[self.prog_ticker]) == 0:
                    self.active_state = self.state_4.move_state_zero
                    self.out_string.append(self.state_4.write_zero)
                    self.move_ticker(self.state_4.move_prog_zero)
                elif int(self.prog_string_10[self.prog_ticker]) == 1:
                    self.active_state = self.state_4.move_state_one
                    self.out_string.append(self.state_4.write_one)
                    self.move_ticker(self.state_4.move_prog_one)

            elif self.active_state == 5:
                if int(self.prog_string_10[self.prog_ticker]) == 0:
                    self.active_state = self.state_5.move_state_zero
                    self.out_string.append(self.state_5.write_zero)
                    self.move_ticker(self.state_5.move_prog_zero)
                elif int(self.prog_string_10[self.prog_ticker]) == 1:
                    self.active_state = self.state_5.move_state_one
                    self.out_string.append(self.state_5.write_one)
                    self.move_ticker(self.state_5.move_prog_one)

            elif self.active_state == 6:
                if int(self.prog_string_10[self.prog_ticker]) == 0:
                    self.active_state = self.state_6.move_state_zero
                    self.out_string.append(self.state_6.write_zero)
                    self.move_ticker(self.state_6.move_prog_zero)
                elif int(self.prog_string_10[self.prog_ticker]) == 1:
                    self.active_state = self.state_6.move_state_one
                    self.out_string.append(self.state_6.write_one)
                    self.move_ticker(self.state_6.move_prog_one)

            elif self.active_state == 7:
                if int(self.prog_string_10[self.prog_ticker]) == 0:
                    self.active_state = self.state_7.move_state_zero
                    self.out_string.append(self.state_7.write_zero)
                    self.move_ticker(self.state_7.move_prog_zero)
                elif int(self.prog_string_10[self.prog_ticker]) == 1:
                    self.active_state = self.state_7.move_state_one
                    self.out_string.append(self.state_7.write_one)
                    self.move_ticker(self.state_7.move_prog_one)
            elif self.active_state == 0:
                return(''.join(str(e) for e in self.out_string))
        #print("RIP")
        return(0)

class State():
    def __init__(self, ten_bits, state_num):
        self.ten_bits = ten_bits
        self.state_num = state_num

        self.move_state_zero = int(self.ten_bits[:3], 2)
        self.write_zero = int(ten_bits[3])
        self.move_prog_zero = int(ten_bits[4])

        self.move_state_one = int(self.ten_bits[5:8], 2)
        self.write_one = int(ten_bits[8])
        self.move_prog_one = int(ten_bits[9])

def run(inp):
    machine = inp[:70]
    prog = inp[69:]
    #print(machine, prog)

    my_machine = Machine(machine, prog)
    return(my_machine.get_out_string())

print(run(input("Input entire Turing Machine string: ")))
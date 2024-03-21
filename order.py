#!/usr/bin/python3

import sys
import random

if len(sys.argv) < 3:
    print("<program> <file> <group>\n")
    exit(1)

class Reader:
    
    def __init__(self):
        self.line_num = 0
        self.bank = []
        self.static = []
        self.tmp = []
        self.counter = 0
        self.max_static_group = 0
        self.new_groups = []
    
    def fail(self, message):
        print("line {}: error: {}", self.line_num, message)
        exit(1)

    def commit_group(self):
        st = []
        for line in self.tmp:
            if '=' == line[0]:
                st.append(line)
            else:
                self.bank.append(line)

        self.tmp = []
        self.static.append(st)
        if len(st):
            self.max_static_group = len(self.static) - 1

    
    def read(self, filename):
        lines = []
        with open(filename) as f:
            lines = f.readlines()

        tmp = []
        num = 0
        firstgroup = True
        for line in lines:
            self.line_num += 1
            line = line.strip()
            if len(line) < 1:
                continue

            tokens = line.split(" ")

            if "group" == tokens[0]:
                if firstgroup:
                    firstgroup = False
                else:
                    self.commit_group()
                continue

            self.tmp.append(line)

        self.commit_group()

    def generate(self, size):
        random.shuffle(self.bank)
        new_groups = []

        bank_idx = 0
        group_idx = 0

        while len(new_groups) < len(self.static) or bank_idx < len(self.bank):
            group = []
            if group_idx < len(self.static) and len(self.static[group_idx]):
                group += self.static[group_idx]

            while len(group) < size and bank_idx < len(self.bank):
                group.append(self.bank[bank_idx])
                bank_idx += 1

            new_groups.append(group)
            group_idx += 1

        self.new_groups = new_groups
        

    def print(self):
        #print(self.groups)
        index = 0
        for group in self.new_groups:
            print("\ngroup {}".format(index))
            index += 1
            for line in group:
                print(line)

        



#
# Start
#

filename = sys.argv[1]
size = int(sys.argv[2])

reader = Reader()
reader.read(filename)
reader.generate(size)
reader.print()











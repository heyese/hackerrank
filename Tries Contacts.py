#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

# https://www.hackerrank.com/challenges/ctci-contacts?h_r=next-challenge&h_v=zen
class ContactStem:
    def __init__(self, letter):
        self.letter = letter
        self.children = []
        self.num_children = 1  # Maybe try to keep a record of num children as they are created?

    def add_child(self, letter):
        # Know I will always be given distinct letters
        self.children.append(ContactStem(letter))

    def find_letter(self, letter):
        for child in self.children:
            if child.letter == letter:
                return child
            return None

    def __str__(self):
        return self.letter


class Contacts:
    base_stems = []
    def __init__(self):
        pass

    # Know that there are no duplicate names in the add operations
    def add(self, name):
        contact_stem = None
        for i in range(len(name)):
            letter = name[i]
            next_contact_stem = self.get_next_stem(letter, contact_stem)
            if not next_contact_stem:
                next_contact_stem = ContactStem(letter)
                if contact_stem:
                    # The new stem is a child of the previous one
                    contact_stem.children.append(next_contact_stem)
                    #print('Added "%s" as a child stem of "%s"' % (letter, contact_stem.letter))
                else:
                    # The new stem is a base_stem
                    self.base_stems.append(next_contact_stem)
                    #print('Added "%s" as a base stem' % letter)
            else:
                next_contact_stem.num_children += 1

            contact_stem = next_contact_stem

    def get_next_stem(self, letter, contact_stem=None):
        if not contact_stem:
            stems = self.base_stems
        else:
            stems = contact_stem.children
        for stem in stems:
            if stem.letter == letter:
                return stem
        return None

    def get(self, name):
        contact_stem = None
        for letter in name:
            next_contact_stem = self.get_next_stem(letter, contact_stem)
            if not next_contact_stem:
                return None
            contact_stem = next_contact_stem
        return contact_stem

    def find(self, name):
        # Returns the number of contacts that begin with stem
        contact_stem = None
        for letter in name:
            next_contact_stem = self.get_next_stem(letter, contact_stem)
            if not next_contact_stem:
                return 0
            contact_stem = next_contact_stem

        # Try a solution where we maintain number of children as we add them
        return contact_stem.num_children

contacts = Contacts()

#!/usr/bin/python3

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def singMeASong(self):
        for line in self.lyrics:
            print(line)
happyBday = Song(["Happy Birtday to you",
                  "IYou belong in a zoo",
                  "You look like a monkey, and smell like one too!"])

bullsOnParade = Song(["They rally around your family",
                      "With a pocket full of shells"])

happyBday.singMeASong()
bullsOnParade.singMeASong()
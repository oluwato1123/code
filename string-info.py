#!/usr/bin/env python3

message = input ("Enter a message: ")

print ("First Character:", message[0])
print ("Last Character:", message[-1])
print("Middle Character:", message[int(len(message) / 2)])
print("Even index character", message[0::2])
print("Odd index character", message[1::2])
print ("Reverse message", message[::-1])
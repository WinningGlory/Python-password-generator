import random

lower_chars = "abcdefghijklmnopqrstuvwxyz"
upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
characters = "!@#$%&^*()"

string = lower_chars + upper_chars + numbers + characters
length: 9
password = "".join(random.sample(string, length))

print("Your new password is:" + password)
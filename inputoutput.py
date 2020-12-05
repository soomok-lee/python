# sep, end
print("python", "java", "javascript", sep=",", end="?")
print("which is more fun?")

import sys
print("python", "java", file=sys.stdout) # standard out
print("python", "java", file=sys.stderr) # standard error

# ljust, rjust
# exam scores
scores = {"math":0, "english":50, "coding":100}
print(type(scores)) # dict
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# zfill
# waiting no 001, 002, 003, ...
for num in range(1, 21):
    print("waiting no : " + str(num).zfill(3))

# input
answer = input("input :") # always string
print("input : " + answer)


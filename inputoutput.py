# seventh chapter
# input, output

# sep, end
print("python", "java", "javascript", sep=",", end="?")
print("which is more fun?")

# sys 
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

# various output format
# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(10000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(-10000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기, 빈 자리는 ^로 채워주기
print("{0:^<+30}".format(10000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수까지만 표시 (소수점 셋째 자리에서 반올림)
print("{0:2f}".format(5/3))

# file input output
score_file = open("score.txt", "w", encoding="utf8")
print("math : 0", file=score_file)
print("english : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("science : 10")
score_file.write("\ncoding : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # read line by line
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # read lines and save as a list
for line in lines:
    print(line, end="")
score_file.close()

# pickle
'''
pickle saves the date used in the program in file format.
'''
import pickle
profile_file = open("profile.pickle", "wb") # binary type wb
profile = {"name":"Ella", "age":20, "hobby":["coding","drawing"]}
print(profile)
pickle.dump(profile, profile_file) # dump : save profile to profile_file
profile_file.close()

profile_file = open("profile.pickle", "rb") # binary type rb
profile = pickle.load(profile_file) # load : read profile_file and save to profile
print(profile)
profile_file.close()

# with
# import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("studying python hard")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

# quiz 7
for i in range(1, 51):
    with open(str(i) + ".txt", "w", encoding="utf8") as report:
        report.write(" -- {0} weekly report -- ".format(i))
        report.write("\ndepartment : ")
        report.write("\nname : ")
        report.write("\ncontent : ")
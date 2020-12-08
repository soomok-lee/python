# tenth chapter
# https://pypi.org/
# pip install beautifulsoup4

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# pip list
# pip show beautifulsoup4
# pip install --upgrade beautifulsoup4
# pip uninstall beautifulsoup4

# built-in function
# input
# language = input("")
# print("{0} is great language!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # external function
# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))
# name = "Ella"
# print(dir(name))

# external function
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob(".py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # current directory 
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("the folder already exists.")
#     os.rmdir(folder) # remove
#     print(folder, "the folder is removed.")
# else:
#     print(folder, "the folder is created.")

# print(os.listdir())

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print(datetime.date.today())
# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days = 100)
print("today + 100 days : ", today + td)  
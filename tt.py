import streamlit as st
import numpy as np
import os

os.system("cls")
import sys
import pandas as pd
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

col1, col2 = st.columns([1 , 2])
with col1:
    st.image('tiger.jpg')
with col2:
    "놓치면 후회할 인재 (신수인🍷👍, 시급 3만원 이하 안감)"
    "전화번호 : 010-1111-2222"
    "이메일 : ehdduddlrnt@naver.com"
    "주소 : 충남 논산시 대학로 121"

'---------------------------------------------------------------------'

col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("google(👍🏻)", "https://google.com")
with col2:
    st.link_button("naver(✅)", "https://naver.com")
with col3:
    st.link_button("건양대학교(❤️)", "https://www.konyang.ac.kr/kor.do")


''
''
'## : orange(자 기 소 개)'
"#### 저는 가난한 집의 2남 2여의 막내로 태어나..."



sys.exit()
x = []
y = []
for i in range(-10, 11, 2):
    x.append(i)
    y.append(3*i**3 + 5*i**2 + 3*i + 7)

col1, col2, col3 = st.columns(3)
with col1:
    cc = st.radio("선의 색을 선택하시오.",["red", "green", "blue", "pink"])
with col2:
    ma = st.radio("마커의 형태를 선택하시오.",["o", "^", "s", "h", "p"])
with col3:
    ls = st.radio("선의 형태를 선택하시오.",["-", "-.", ":", "--"])


# cc = st.radio("선의 색을 선택하시오.",["red", "green", "blue", "pink"])
# ma = st.radio("마커의 형태를 선택하시오.",["o", "^", "s", "h", "p"])
# ls = st.radio("선의 형태를 선택하시오.",["-", "-.", ":", "--"])
plt.plot(x, y, color = cc , linestyle = ls, marker = ma)
st.pyplot(fig)




fig, ax = plt.subplots()
x = []
"x", x
for iter in range(-10, 11, 5):
    "iter", iter
    x.append(iter)
    "x", x

st.pyplot(fig)


# gg = st.radio("선택하시오", ["오름차순", "내림차순"])

# st.write("선택한 것은 : ", gg)

# genre = st.radio("what's your favorite movie genre", [":rainbow[오름차순]," "***내림차순***", "기타 : movie_camera:"], 
#                 captions = ["laugh out loud.", "get the popcorn.", "never stop learning."], horizontal = Ture)

# if genre == ":rainbow[Comedy]":
#     st.write("you selected comedy.")
# else:
#     st.write("you didn't select comedy.")



# fig, ax = plt.subplots()

# a = 2
# b= 5
# c = 3
# d = 7

# x = []
# y = []
# for i in range(-100, 101, 50):
#     x.append(i)
#     y.append(a*i**3 + b*i**2 + c*i + d)


# col1, col2, col3, col4 = st.columns(4)
# with col1:
#     color = st.radio("색을 선택 하시오", ("red", "green", "blue"))
# with col2:
#     linestyle = st.radio("선의 스타일을 선택 하시오", ("-", "-.", ":"))
# with col3:
#     marker = st.radio("마커의 스타일을 선택 하시오", ("s", "^", "o"))
# # with col4:
# #     emoje = st.radio("이모지의 모양을 선택하시오", ("sunglasses", "heart", "smile"))

# if "red" in color:
#     t = "-.r^"
# if "green" in color:
#     t = "-.g^"
# if "blue" in color:
#     t = "-.b^"

# plt.plot(x, y, color = color, marker = marker, linestyle = linestyle)#, emoje = emoje)
# st.pyplot(fig)



# st.write("hello, 'world!' sunglasses:")
# "hello, 'world!' sunglasses:"
# print("hello," "world!" "sunglasses:")

# "# hello, 'world!' sunglasses:"
# "## hello, 'world!' sunglasses:"
# "### hello, 'world!' sunglasses:"
# "#### hello, 'world!' sunglasses:"
# "##### hello, 'world!' sunglasses:"
# "###### hello, 'world!' sunglasses:"





# list1 = list([["한빛", "남자", "20", "180"],
#             ["한강", "남자", "21", "177"],
#             ["한결", "중성", "51", "155"],
#             ["한라", "여자", "20", "160"]])
# n = np.array(list1)
# col_names = ["이름", "성별", "나이", "키"]
# df = pd.DataFrame(list1, columns = col_names, index = ["1행", "2행", "3행", "4행"])
# df

# genre = st.radio("선택하시오.", ["오름차순", "내림차순", "기타"],
#                 horizontal = True, index = 2)
# number = st.number_input("insert a number", value = 20, step = 1)
# df.iloc[3, 2] = number

# if "오름" in genre:
#     st.dataframe(df.sort_values(by = ["키"]))
# if "내림" in genre:
#     st.dataframe(df.sort_values(by = ["키"], ascending = False))
# if "기타" in genre:
#     st.dataframe(df)
# if "요약" in genre:
#     st.dataframe(df.describe())





# sys.exit()


















# li = [1, 2, 3, 4]
# li

# for i in range(4):
#     li[i] = li[i] + 3
# li

# li = np.array([1, 2, 3, 4])
# li + 5


# li_sort = np.sort(li)[::- 1]
# li_sort


# li = [1, 2, 3, 4]
# n = np.array(li)
# a = pd.Series(li)
# li
# n
# pd







































# ----------------------------------------------------------------------------------

# for i in range(6):
#     r = random
#     r

# t = turtle.Turtle()
# t.shape("turtle")
# t.width(3)
# t.speed(0)
# t.color("pink")
# t.penup()
# t.goto(-200, 0)
# t.pendown()
# n = 10
# for _ in range(n):
#     t.forward(100)
#     t.left(360/n)



# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)



# while True:
#     for i in range(30):
#         n = 10
#         for _ in range(n):
#             t.forward(1 + 5*i)
#             t.left(360/n)
#         # t.circle(1 + 5*i)
#         t.color((random.random(), random.random(), random.random()))
#         t.goto(i*20, 0)
#     t.clear()

# turtle.done()




# ----------------------------------------------------------------------------------

# n = 10
# def user_full(n):
#     arr = np.full((10, 10), 10)
#     for i in range(n):
#         for j in range(n):
#             if i == i + j:
#                 arr[i, j] = 10
#     return arr

# arr = user_full(10)
# arr


# ---------------------------------------------------------------------------------------

# list1 = [[1, 2, 3, 4], [3, 5, 7, 9]]
# a = np.array(list1)
# a

# a.ndim
# n = np.ndim(a)


# list1 = [[1, 2, 3, 4], [3, 5, 7, 9]]
# a = np.array(list1)
# a

# n = np.full((10, 5), 7)

# n = np.eye(5)
# n
# # a

# def user_eye(n):
#     arr = np.zeros((n, n))
#     for i in range(n):
#         for j in range(n):
#             if i == n - j - 1:
#                 arr[i, j] = 1
#     return arr

# arr = user_eye(10)
# arr


# ------------------------------------------------------------------------
# list1 = [1, 2, 3, 4]
# j = 0
# list1 + 10
# for i in list1:
#     j = i + 1
#     list1[j]

# a = np.array(list1)
# a + 10


# 넘파이와 판다스 라이브 

# list1 = [1, 2, 3, 4]
# for i in range(4):
#     list1[i] = list1[i] + 3
# list1

# a = np.array(list1)
# a + 10
# a.shape
# s = a.sum(axis = 0)
# s
# mn = a.min(axis = 0)
# mn



# list1 = [[1, 2, 3, 4], [3, 5, 7, 9]]
# a = np.array(list1)
# a
# a.shape
# s = a.sum(axis = 0)
# s
# mn = a.min(axis = 1)
# mn

# list1 = [[1, 2, 3, 4], [3, 5, 7, 9]]
# a = np.array(list1)
# a

# a[1, 1 : 3 : 2]
# a[:,1]
# a[-1, 1]

# a = np.zeros(2)
# ('a|n', a)
# b = np.zeros((2))
# ("b|n,", b)
# c = np.ones((2, 3))
# ("c|n", c)
# d = np.full((2, 3), 5)
# ("d|n", d)
# e = np.eye(5)
# ("e|n", e)

# n = 10
# def user_eye(n):
#     arr = np.zeros((n, n))
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 arr[i, j] = 1
#     return arr

# arr = user_eye(10)
# arr

# ---------------------------------------------------------

# "if 문 : 조건문"

# grade = 80
# if grade > 60:
#     st.write("합격")

# a = 5

# if a == 5:
#     st.write("right!")
#     st.write("a is 5")
# if a == 3:
#     st.write("right!")
#     st.write("a is 3")
# if a != 3:
#     st.write("right!")
#     st.write("a is not 3")


# grade = 44
# if grade >= 60:
#     st.write("합격!")
# else:
#     st.write("불합격...")

# if grade %3 == 0:
#     st.write("3의 배수")
# else:
#     st.write("3의 배수가 아닙니다..")

# if grade >= 90:
#     st.write("A")
# elif grade >= 80:
#     st.write("B")
# elif grade >= 70:
#     st.write("C")
# elif grade >= 60:
#     st.write("D")
# else:
#     st.write("F")

# -------------------------------------------------------------------------

# a = 9
# for a in range(2, 10):
#     str(a), "단 입니다..."
#     ""
#     for i in range(1, 10):
#         b = str(a) + "x" + str(i) + "=" + str(a*i)

#         b

# --------------------------------------------------------------------------------------

# "list 사용법"

# li = [1, 2, 3, 4, 5, 1, 3]
# li

# # li.append(100)
# # li

# # c = li.count(3)
# # c

# # li.sort() "오름차순으로 나옴"
# # li.sort(reverse=True) "내림차순으로 할때"
# li

# ty = type(li)
# ty

# ---------------------------------------------------------------------------------

# 리스트 생성하기
# list_1 = [1, 2, 3, 4, 5, 1, 3]
# list_2 = []
# st.write(list_1)
# st.write(list_2)
# st.write(len(list_1))

# # 리스트 변경하기
# list_1[3] = 9999
# st.write(list_1)
# list_1.append(100)
# st.write(list_1)
# list_1.remove(9999)
# st.write(list_1)
# list_1.insert(0, 777)
# st.write(list_1)

# # 리스트 복제하기
# list_2 = list_1.copy()
# st.write(list_2)

# ----------------------------------------------------------------------

# 딕셔너리 활용
# dict = {"name" :  "신수인", 
#         "weight" : 69, 
#         "height" : 172,
#         "address": "충남 논산시 대학로 121"
#         }
# dict

# dict["address"]

# --------------------------------------------------------------------------------

# 딕셔너리 생성하기
# dict_1 = {"name" : "홍길동", "birth" : 1990, "addr" : "KR"}
# dict_1
# dict_1["birth"]

# # 키와 값 추가하기
# dict_1["weight"] = 60.5
# dict_1["family"] = ["아빠", "엄마", "여동생"]
# dict_1

# # 여러 키와 값을 동시에 추가하기
# dict_1.update({"weight" : 67.8, "hobby" : ["게임, 독서"]})
# dict_1

# # 딕셔너리 값 변경하기
# dict_1["hobby"] = ["축구", "등산"]
# dict_1

# # 데이터 삭제하기
# del dict_1["weight"]
# del dict_1["birth"]
# del dict_1["addr"]
# dict_1

# for i in dict.keys():
#     i

# for i in dict.values():
#     i
# "-------------------------------------------------"
# for k, v in dict.items():
#     k
#     v

# ty = type(dict)
# ty

# ----------------------------------------------------------------------------------

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.width(3)
# t.color("pink")



# t.write("이동영", move=False, align="center", font=("arial",50,"bold"))

# t.penup()
# t.sety(-100)
# t.pendown()

# t.write("입니당", move=False, align="center", font=("Freestyle Script",50,"normal"))



# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)

# turtle.done()

# ------------------------------------------------------------------

# def sta(arr):
#     sum = 0  #"초기값"
#     mx = -1e10
#     mn = 1e10
#     for i in arr:
#         sum = sum + 1
#         if mx < 1:
#             mx = i
#         if mn > i:
#             mn = i
#     arr
#     "sum =", sum, "min = ", mn, "max = ", mx
#     return sum, mx, mn

# # list_1 = [1, 2, 4, 7, 33, 50]
# # s = sum(list_1)
# # mx = max(list_1)
# # mn = min(list_1)
# # s, mx, mn

# list_1 = [5, 13, 7, 4, 11]
# [s1, mx1, mn1] = sta(list_1)
# s1, mx1, mn1
# # sum

# -------------------------------------------------------

# s = 0
# for i in range(1, 7 + 1, 1):
#     s = s + i

# s

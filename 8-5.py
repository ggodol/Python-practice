"""
8-5 with
https://youtu.be/kWiCuklohdY?t=12622
"""
import pickle

# pickle 파일 활용
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# 일반 파일 활용
# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())
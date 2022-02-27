import pickle

with open("profile.pickle", "rb") as profile_file:  # 따로 close 할 필요 없다
    print(pickle.load(profile_file))


with open("study.txt", "w", encoding="utf8") as study_file:  # 쓰기
    study_file.write("파이썬")

with open("study.txt", "r", encoding="utf8") as study_file:  # 읽기
    print(study_file.read())

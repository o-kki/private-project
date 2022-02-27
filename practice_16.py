import pickle
profile_file = open("profile.pickle", "wb")    # wb에서 b는 바이너리 의미
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")  # rb는 읽어오는것
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

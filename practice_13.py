# score_file = open("score_txt", "w", encoding="utf8")  # w는 쓰기 용도
# print("수학 : 0", file=score_file)
# print("영어 : 59", file=score_file)
# score_file.close

score_file = open("score.txt", "a", encoding="utf8")  # a는 append 의미 이어서 쓴다
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")  # 따로 줄바꿈이 없다. \n 사용해서 줄바꿈 진행
score_file.close()

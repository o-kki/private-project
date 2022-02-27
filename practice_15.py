# 1번째 방법
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

# 2번째 방법
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readline()  # list로 출력
for line in lines:
    print(line, end="")

score_file.close()

names = ["유1","유2","유3","유4"]
# sol1
for name in names:
    with open(str(name)+".txt",'w',encoding="utf8") as mail_file:
        mail_file.write("안녕하세요? {0}님.\n".format(name))
        mail_file.write("(주)나도출판 편집자 나코입니다.\n")
        mail_file.write("현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n")
        mail_file.write("{0} 님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n".format(name))
        mail_file.write("자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n")
        mail_file.write("좋은 하루 보내세요 ^^\n")
        mail_file.write("감사합니다.\n")
        mail_file.write("- 나코 드림.")

# sol2
for name in names:
    with open("{}.txt".format(name),'w',encoding="utf8") as mail_file:
        mail_file.write(f"""
안녕하세요? {name}님.

(주)나도출판 편집자 나코입니다.
현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
{name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

좋은 하루 보내세요 ^^
감사합니다.

- 나코 드림.
""")

# sol3
for name in names:
    with open("{}.txt".format(name),'w',encoding="utf8") as mail_file:
        contents = (f"안녕하세요? {name}님.\n\n"
            "(주)나도출판 편집자 나코입니다.\n"
            "현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n"
            "{name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n"
            "자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n"
            "좋은 하루 보내세요 ^^\n"
            "감사합니다.\n\n"
            "- 나코 드림.\n")
        mail_file.write(contents)
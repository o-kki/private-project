import imp
import pickle

for week in range(1, 51):
    with open(str(week)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("{0}주차 주간보고".format(week))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")

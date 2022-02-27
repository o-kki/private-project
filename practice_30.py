# import travel.thailand # .모듈 or 패키지만 가능 => class는 X
# # import travel.thailand.ThailandPackage # 불가
# # from travel.thailand import ThailandPackage # 가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import * # init.py에 thailand 추가하니 잘된다.
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random

from travel import thailand
print(inspect.getfile(random)) # random이 어디 위치에 있는지
print(inspect.getfile(thailand))

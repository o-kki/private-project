import imp

import practice_module
practice_module.price(3) # 3명 영화 보러 갔을 때
practice_module.price_morning(4) # 4명 조조 할인 영화 보러 갔을 때
practice_module.price_soldier(5) # 5명 군인 할인 영화 보러 갔을 때



import practice_module as mv
mv.price(3) # 3명 영화 보러 갔을 때
mv.price_morning(4) # 4명 조조 할인 영화 보러 갔을 때
mv.price_soldier(5) # 5명 군인 할인 영화 보러 갔을 때


from practice_module import *
price(3)
price_soldier(5)
price_morning(4)

from practice_module import price, price_morning
price(5)
price_morning(6)
price_soldier(7) # 사용 불가!
 

from practice_module import price_soldier as price
price(5)

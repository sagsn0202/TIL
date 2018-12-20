# import lotto_functions
# lotto_functions.am_i_lucky(lotto_functions.pick_lotto(), lotto_functions.get_lotto())

from lotto_functions import pick_lotto, get_lotto, am_i_lucky
result = am_i_lucky(pick_lotto(), get_lotto())
print(result)
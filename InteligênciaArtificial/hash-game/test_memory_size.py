# Serve para bagunçar, testar qualquer estutura quanto a Espaço de Memoria
import sys
import numpy as np

# z = np.arange(3, dtype=np.uint8)
# print(sys.getsizeof(z))

x = (1,2,3,4,5,6,7,8,9)
z = ('1','2','3','4','5','6','7','8','9')
y = [1,2,3,4,5,6,7,8,9]
w = ['1','2','3','4','5','6','7','8','9']
t = (1,2)
i = (True, False)
dict_1 = {'0': 1, '2': '2'}
print(sys.getsizeof(i))
print(sys.getsizeof(t))
print(sys.getsizeof(dict_1))
print('tuple of number',sys.getsizeof(x))
print('list of number',sys.getsizeof(z))
print('y', sys.getsizeof(y))
print('w', sys.getsizeof(w))
a = 9
b = '1'
print('integer only', sys.getsizeof(a))
print('str only', sys.getsizeof(b))
d = {
"int": 0,
"float": 0.0,
"dict": dict(),
"set": set(),
"tuple": tuple(),
"list": list(),
"str": "a",
"unicode": u"a",
"object": object(),
}
for k, v in d.items():
     print(k, sys.getsizeof(v))
print('\n')


count_goal = {
		'h_up': 0,
		'h_mi': 0,
		'h_dw': 0,
		'v_le': 0,
		'v_ce': 0,
		'v_ri': 0,
		'd_dw': 0,
		'd_up': 0,
	}

count_goal_list   = [0,0,0,0,0,0,0,0]
count_goal_tuple  = (0,0,0,0,0,0,0,0)
count_goal_tuple  = (3,3,3,3,3,3,3,3)
count_goal_string = "01234567"

print('\ncount_goal_dict in bytes', sys.getsizeof(count_goal))
print('\ncount_goal_list in bytes', sys.getsizeof(count_goal_list))
print('\ncount_goal_tuple in bytes', sys.getsizeof(count_goal_tuple))
print('\ncount_goal_string in bytes', sys.getsizeof(count_goal_string))


# d = {
#      "int": 0,
#      "float": 0.0,
#      "dict": dict(),
#      "set": set(),
#      "tuple": tuple(),
#      "list": list(),
#      "str": "a",
#      "unicode": u"a",
#      "object": object(),
#  }
# for k, v in d.items():
#      print(k, sys.getsizeof(v))
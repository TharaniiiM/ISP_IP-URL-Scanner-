import random 

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*()_+{}:|\~`/?><,."

ans = lower_case + upper_case + number + symbol

length = 18

password = "".join(random.sample(ans,length))

#pyperclip.copy(password)

print (password)
 
import re
string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
s = r"\d{4}"  # here r represents the raw strings \ is a escape sequence \d represents the digit and {4} means the time
# Here we need to comile before the string is passed for filter
t = re.compile(s)
result = re.findall(t, string)
print(result)



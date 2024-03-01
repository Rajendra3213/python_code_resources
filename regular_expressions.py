import re
string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
# here r represents the raw strings \ is a escape sequence \d represents the digit and {4} means the time
s = r"\d{3}"
# Here we need to comile before the string is passed for filter
t = re.compile(s)  # create regular expression object
result = re.findall(t, string)

# ---------- re.search(pattern,string,flag)-------------
#  Only return first match

result = re.search(r"\d{3}", string)
# print(result)

# ---------- re.match(pattern,string,flag)-------------
#  Only return if the starting matched

# \w means any format of word made up of either digit or any
result = re.match(r"\w{3}", string)
# print(result)

# ---------- re.fullmatch(pattern,string,flag)-------------
#  return whole string except the new line
result = re.fullmatch(r".{285}", string)
# print(result)


# ---------- re.findall(pattern,string,flag)-------------
#  find the matched string and return a list in found order
result = re.findall(r"\d{3}", string)  # '.' indicates anytypes of values
# print(result)

# ---------- re.split(pattern,string,flag)-------------
#  as split method is done
result = re.split(r"\s", string)  # '.' indicates anytypes of values
# print(result)

# ---------- re.split(pattern,string,maxsplit,flag)-------------
#  as split method is done
result = re.split(r"\s", string)  # '.' indicates anytypes of values
# print(result)

# ---------- re.sub()-------------
#  It will filter and replace the certain string with given strings
result = re.sub(r"[A-Z]{2,}", "rajendra", string,1)
# here r"[A-Z]{2,2} means any Uppercase letter and sholud be atleast 2 and end with any number
# print(result)


# ---------- group() and groups()-------------
# To find the different patterns at once
result = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)
#explainin the expressions: Here .
# .+: Matches one or more of any character (except for a newline).
# \s: Matches any whitespace character (e.g., space, tab, newline).
# (.+ex): Captures a group containing one or more of any character followed by "ex".
# .+: Matches one or more of any character (greedy match).
# (\d\d\s.+): Captures a group containing two digits, followed by a whitespace character, and then one or more of any character.
print(result.groups())
print(result.group(0))

import re
result = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)
result.group(1)
result.group(2)
result.start(1)
result.start(2)
result.end(1)
result.end(2)
result.span(1)
result.span(2)

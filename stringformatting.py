age=34
print(f"you are {age}") #this is f-string method to convert a number to a string directly without using the str method

#that is:
"""age=34
age_as_str=str(age)
print("you are"+ age_as_str)"""

#the problem
name="pop"
greeting=f"how are you {name}"
print(greeting)
name="bob"
print(greeting)
#the same name string is repeated two times

""" so we have another option in python i.e."""
#1 changing the value of variable name directly! and passing the variable as parameter
name="vibs"
final_greet="how are you {}?"
vibs_greet=final_greet.format(name)
print(vibs_greet)
name="adi"
adi_greet=final_greet.format(name)
print(adi_greet)
#2 passing values for the variable name as parameter
name="tom"
greet="how are you {name}"
greet_vibs=greet.format(name="vibs")
print(greet_vibs)
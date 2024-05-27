from Stack_ex import check_balanced_brackets

 # Test Cases
expression1 = input("Enter brackets")  #"[()]{}{[()()]()}"
#expression2 = input(" Enter brackets") # "[(])"
print(f"input: {expression1} ")
print(f"Output: {check_balanced_brackets(expression1)}")  # Balanced
print("All the brackets are well formed ")

#print(f"input: {expression2}")
#print(f"Output:{check_balanced_brackets(expression2)}")  # Not Balanced
#print("The brackets are not well blanced")


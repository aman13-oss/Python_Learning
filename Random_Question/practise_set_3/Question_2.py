letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
name=input("Enter the name: ")
date=input("Enter the date: ")

updated_letter=letter.replace("<|Name|>", name).replace("<|Date|>",date)

print(updated_letter)


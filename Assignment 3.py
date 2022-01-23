print("\t\t\t FUNCTION : 1 ")
def data_types(name, roll_number, subjects_and_code, marks, total_marks, result, percentage):
    print(f" Name : {str(name)} \n Roll number : {int(roll_number)} \n Subjects and code : {dict(subjects_and_code)} \n"
          f" Marks : {set(marks)} \n Result : {list(result)} \n Total marks : {tuple(total_marks)} \n Percentage : {float(percentage)}")


data_types("Mathesh", 34534, {"English" : "SCV34", "Maths" : "TYB34"}, {89, 98}, (187, 187), ["pass", "pass"], 93.5)

print("\n")
print("\t\t\t FUNCTION : 2 ")
def for_loop():
    address = {
        "bike" : "Royal Enfield",
        "Car" : "Jaguar",
        "Phone" : "Apple"
     }
    for i, j in address.items():
        print(f"My favourite {i} is {j}")


for_loop()
print("\n")
print("\t\t\t FUNCTION : 3 ")
def numbers(a, b):
    return[a, b]


c = numbers(40, 50)
print(f" The two numbers are in list : {c}")
print(type(c))
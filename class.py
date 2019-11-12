class student:
    def __init__(sel, new_name, new_grades):
        sel.name=new_name
        sel.grades=new_grades
    def average(sel):
        return(sum(sel.grades)/len(sel.grades))

student_one=student("rolf smith",[70,88,92,66,24])

print(student_one.name)
print(student.average(student_one))

from tkinter import *
from tkinter import ttk
import tkinter as tk

from tuitions import Payment
from student import Student

window =Tk()
window.title('TUITIONS FOR DIFFERENT STUDENTS')

def add_fee():
  tuition =int(tuition_entry.get())
  lib_fee =int(lib_entry.get())
  func_fee =int(function_entry.get())
  med_fee =int(medical_entry.get())
  Payment.set_total_fees(tuition,lib_fee,func_fee,med_fee)
  total_fees_entry.delete(0)
  total_fees_entry.insert(0,string=f'totalfees:{Payment.get_total_fees()}')

stds =[]
def record_student_details():
  global stds
  name=name_entry.get()
  age=age_entry.get()
  fees=int(fees_entry.get())
  std1 =Student(name,age,fees)

  stds =std1.get_all_students()

def print_students():
  output_text.insert(tk.END,'THESE ARE ALL THE STUDENTS')
  i=0
  for std in stds:
    output_text.insert(tk.END,f'\nStudent{i+1}')
    output_text.insert(tk.END,f'\n{std}')
    i+=1
    output_text.insert(tk.END,'\n the following students paid tutition:')    
    paid =Payment.get_paid_std()

    for pa in paid:
      output_text.insert(tk.END,F'\n{pa}')

setting_fees_label =ttk.Label(window,text='setting fees')
setting_fees_label.grid(row=0,column=1)

tuition_label =ttk.Label(window,text='enter the tuition:')
tuition_label.grid(row=1,column=1)
tuition_entry =ttk.Entry(window)
tuition_entry.grid(row=1,column=2)

lib_label =ttk.Label(window,text='enter the library fee:')
lib_label.grid(row=2,column=1)
lib_entry =ttk.Entry(window)
lib_entry.grid(row=2,column=2)

function_label =ttk.Label(window,text='enter the functional fee:')
function_label.grid(row=3,column=1)
function_entry =ttk.Entry(window)
function_entry.grid(row=3,column=2)

medical_label =ttk.Label(window,text='enter the medical fee:')
medical_label.grid(row=4,column=1)
medical_entry =ttk.Entry(window)
medical_entry.grid(row=4,column=2)

total_fees_button =ttk.Button(window,text='this is total fees',command=add_fee)
total_fees_button.grid(row=5,column=1)

total_fees_entry =ttk.Entry(window)
total_fees_entry.grid(row=5,column=2)

student_details_label =ttk.Label(window,text='enter the students details')
student_details_label.grid(row=7,column=2)

name_label =ttk.Label(window,text='enter the name:')
name_label.grid(row=8,column=1)
name_entry =ttk.Entry(window)
name_entry.grid(row=8,column=2)

age_label =ttk.Label(window,text='enter the age:')
age_label.grid(row=9,column=1)
age_entry =ttk.Entry(window)
age_entry.grid(row=9,column=2)

fees_label =ttk.Label(window,text='enter the fees:')
fees_label.grid(row=10,column=1)
fees_entry =ttk.Entry(window)
fees_entry.grid(row=10,column=2)

record_student_label =ttk.Label(window,text='are u adding more:')
record_student_label.grid(row=11,column=1)
record_student_button =ttk.Button(window,text='yes',command =record_student_details)
record_student_button.grid(row=12,column=1)

no_student_label =ttk.Label(window,text='are u not adding more:')
no_student_label.grid(row=13,column=1)
no_student_button =ttk.Button(window,text='no',command =print_students)
no_student_button.grid(row=14,column=1)

print_button =ttk.Button(window,text='print the different students',command=print_students)
print_button.grid(row=15,column=2)

output_text=Text(window)
output_text.grid(row=16,column=2)

window.mainloop()

import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'w+', newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name" "Age" "Contact_NO" "Emailid"])
            writer.writerow(info_list)

if __name__=='__main__':
    condition=True
    student_num=1

while(condition):
    student_info=input("Enter some student information in the following format (name age contact_no email id): ".format(student_num))


    student_info_list=student_info.split(' ')
    print("Entered split information is: "+ str(student_info_list))

    write_into_csv(student_info_list)


    condition_check=input("Enter (yes/no) if you want to input information of another student: ")
    if condition_check=="yes":
        condition=True
    elif condition_check=="no":
        condition=False


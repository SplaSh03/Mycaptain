import csv


def write_info_csv(info_list):
    with open(student_info_csv, 'a', newline) as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["name", "age", "contect num", "Emailid"])  # file is empty

        writer.writerow(info_list)


if __name__ == '__main__':
    condition = True
    student_num = 1
while (condition):
    student_info = input("enter stud info in the following format ".format(student_num))
    print("entered information" + student_info)

    student_info_list = student_info.split(' ')
    print("\nenter split up informationis :" + str(student_info_list))
    print("\nThe entered info is -\nname: {}\nAge: {}\ncontact number: {}\nEmail ID: {}"
          .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
    choice_check = input("is the entered information crt? (y/n)")
    if choice_check == "yes":
        write_info_csv(student_info_list)
        condition_check = input("enter (y/n) if you want to enter info")
        if condition_check == "yes":
            condition = True
            student_num = student_num + 1
        elif condition_check == "No":
            condition = False
    elif choice_check == "no":
        print("\n please re-enter the values!")

percent=int(input("enter the percentage:"))
attendance=int(input("enter the attendance:"))

if percent>85 and attendance>75:
    print("scholarship eligible")
else:
    print("not eligible")
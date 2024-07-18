class differentFunctions():
    def Subfields():
        subfields = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        print("Sub-fields in AI are:")
        for subfield in subfields:
            print(subfield)
        return subfield

    def OddEven():
        num=int(input("Enter a number: "))
        if num % 2 == 0:
            print(num, "is Even number")
            message="This is even number"
        else:
            print(num, "is Odd number")
            message="This is odd number"
        return message

    def Eligible():
        gender = input("Your Gender (Male/Female): ").strip().lower()
        age = int(input("Your Age: "))
        if gender == "male" and age > 21:
            print("ELIGIBLE")
            message1="Eligible"
        elif gender == "female" and age > 18:
            print("ELIGIBLE")
            message1="Eligible"
        else:
            print("NOT ELIGIBLE")
            message1="Not Eligible"
        return message1

    def percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        
        tot=(sub1+sub2+sub3+sub4+sub5)
        print("Total= ", tot)
        message2="Total"
        
        per=(sub1+sub2+sub3+sub4+sub5)/5
        print("Percentage= ", per)
        message2="Percentage"

    def triangle():
        height=int(input("Height= "))
        breadth=int(input("Breadth= "))
        print("Area formula: (Height*Breadth)/2")
        Area=(height*breadth)/2
        print("Area of Triangle: ", Area)
        message3="Area"

        height1=int(input("Height1= "))
        height2=int(input("Height2= "))
        breadth=int(input("Breadth= "))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter= height1+height2+breadth
        print("Perimeter of Triangle: ", Perimeter)
        message3="Perimeter"
        return message3
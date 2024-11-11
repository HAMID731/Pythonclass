print("Enter department\n1. IT\n2. HR\n3. Finance\nEnter Number>>>>>>")

answer = int(input())

match answer:
    case 1:
        print("IT")
        print("1. Manager\n2. Analyst\n3. Intern\nselect>>>>>")
        answer_one = int(input())

        match answer_one:
            case 1:
                print("Manager of the IT department")
            case 2:
                print("Analyst of the IT department")
            case 3:
                print("Intern of the IT department")

    case 2:
        print("HR")
        print("1. Manager\n2. Analyst\n3. Intern\nselect>>>>>")
        answer_two = int(input())

        match answer_two:
            case 1:
                print("Manager of the HR department")
            case 2:
                print("Analyst of the HR department")
            case 3:
                print("Intern of the HR department")

    case 3:
        print("Finance")
        print("1. Manager\n2. Analyst\n3. Intern\nselect>>>>>")
        answer_three = int(input())

        match answer_three:
            case 1:
                print("Manager of the Finance department")
            case 2:
                print("Analyst of the Finance department")
            case 3:
                print("Intern of the Finance department")

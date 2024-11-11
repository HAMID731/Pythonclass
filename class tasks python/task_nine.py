print("Enter department\n1. ice cream\n2. sundea\n3. shake\nEnter Number>>>>>>")

answer = int(input())

match answer:
    case 1:
        print("ice cream")
        print("1. chocolate\n2. vanilla\n3. strawberry\nselect>>>>>")
        answer_one = int(input())

        match answer_one:
            case 1:
                print("You have gotten a chocolate ice cream")
            case 2:
                print("You have gotten a vanilla ice cream")
            case 3:
                print("You have gotten a strawberry ice cream")

    case 2:
        print("sundae")
        print("1. chocolate\n2. vanilla\n3. strawberry\nselect>>>>>")
        answer_two = int(input())

        match answer_two:
            case 1:
                print("You have gotten a chocolate sundae")
            case 2:
                print("You have gotten a vanilla sundae")
            case 3:
                print("You have gotten a strawberry sundae")

    case 3:
        print("shake")
        print("1. chocolate\n2. vanilla\n3. strawberry\nselect>>>>>")
        answer_three = int(input())

        match answer_three:
            case 1:
                print("You have gotten a chocolate shake")
            case 2:
                print("You have gotten a vanilla shake")
            case 3:
                print("You have gotten a strawberry shake")

print("Enter grade\n1. math\n2. science\n3. History\nEnter Number>>>>>>")

answer = int(input())

match answer:
    case 1:
        print("math")
        print("1. freshmen\n2. sophomore\n3. junior\n4. senior\nselect>>>>>")
        answer_one = int(input())

        match answer_one:
            case 1:
                print("You are studying math and are a freshman")
            case 2:
                print("You are studying math and are a sophomore")
            case 3:
                print("You are studying math and are a junior")
            case 4:
                print("You are studying math and are a senior")

    case 2:
        print("science")
        print("1. freshmen\n2. sophomore\n3. junior\n4. senior\nselect>>>>>")
        answer_two = int(input())

        match answer_two:
            case 1:
                print("You are studying science and are a freshman")
            case 2:
                print("You are studying science and are a sophomore")
            case 3:
                print("You are studying science and are a junior")
            case 4:
                print("You are studying science and are a senior")

    case 3:
        print("history")
        print("1. freshmen\n2. sophomore\n3. junior\n4. senior\nselect>>>>>")
        answer_three = int(input())

        match answer_three:
            case 1:
                print("You are studying history and are a freshman")
            case 2:
                print("You are studying history and are a sophomore")
            case 3:
                print("You are studying history and are a junior")
            case 4:
                print("You are studying history and are a senior")

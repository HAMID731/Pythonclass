print("Select a menu :\n1. Phone book\n2. Message\n3. Chat\n4. Call register\n5. Tones\n6. Settings\n7. Call Divert\n8. Games\n9. Calculator\n10. Reminder\n11. Clock\n12. Profiles")
answer = int(input(">>>>>>>> "))

match answer:
    case 1:
        print("Phone book")
        print("1. Search\n2. Service Nos.\n3. Add name\n4. Erase\n5. Edit\n6. Assign tone\n7. Send b'card\n8. Options\n9. Speed dials\n10. Voice tags")
        answer_one = int(input(">>>>>>>> "))
        match answer_one:
            case 1:
                print("Search")
            case 2:
                print("Service Nos.")
            case 3:
                print("Add Name")
            case 4:
                print("Erase")
            case 5:
                print("Edit")
            case 6:
                print("Assign Tone")
            case 7:
                print("Send b'card")
            case 8:
                print("Options")
                print("1. Type of view\n2. Memory status")
                answer_one_eight = int(input(">>>>>>>> "))
                match answer_one_eight:
                    case 1:
                        print("Type of View")
                    case 2:
                        print("Memory Status")
            case 9:
                print("Speed Dials")
            case 10:
                print("Voice Tags")

    case 2:
        print("Messages")
        print("1. Write messages\n2. Inbox\n3. Outbox\n4. Picture messages\n5. Templates\n6. Smileys\n7. Message Settings\n8. Info service\n9. Voice mailbox number\n10. Service command editor")
        answer_two = int(input(">>>>>>>> "))
        match answer_two:
            case 1:
                print("Write messages")
            case 2:
                print("Inbox")
            case 3:
                print("Outbox")
            case 4:
                print("Picture messages")
            case 5:
                print("Templates")
            case 6:
                print("Smileys")
            case 7:
                print("Message Settings")
                print("1. Set 1\n2. Common")
                answer_one_seven = int(input(">>>>>>>> "))
                match answer_one_seven:
                    case 1:
                        print("1. Message center number\n2. Message sent as\n3. Message validity")
                        answer_one_five = int(input(">>>>>>>> "))
                        match answer_one_five:
                            case 1:
                                print("Message center number")
                            case 2:
                                print("Message sent as")
                            case 3:
                                print("Message validity")
                    case 2:
                        print("1. Delivery report\n2. Reply via same centre\n3. Character support")
                        answer_one_six = int(input(">>>>>>>> "))
                        match answer_one_six:
                            case 1:
                                print("Delivery report")
                            case 2:
                                print("Reply via same centre")
                            case 3:
                                print("Character support")
            case 8:
                print("Info service")
            case 9:
                print("Voice mailbox number")
            case 10:
                print("Service command editor")

    case 3:
        print("Chat")

    case 4:
        print("Call Register")
        print("1. Missed calls\n2. Received calls\n3. Dialled numbers\n4. Erase recent call list\n5. Show call duration\n6. Show call cost\n7. Call cost settings\n8. Prepaid credit")
        answer_four = int(input(">>>>>>>> "))
        match answer_four:
            case 1:
                print("Missed calls")
            case 2:
                print("Received calls")
            case 3:
                print("Dialled numbers")
            case 4:
                print("Erase recent call list")
            case 5:
                print("Show call duration")
                print("1. Last call duration\n2. All calls' duration\n3. Received calls' duration\n4. Dialled calls' duration\n5. Clear timers")
                answer_one_nine = int(input(">>>>>>>> "))
                match answer_one_nine:
                    case 1:
                        print("Last call duration")
                    case 2:
                        print("All calls' duration")
                    case 3:
                        print("Received calls' duration")
                    case 4:
                        print("Dialled calls' duration")
                    case 5:
                        print("Clear timers")
            case 6:
                print("Show call cost")
                print("1. Last call cost\n2. All calls' cost\n3. Clear counters")
                answer_one_ten = int(input(">>>>>>>> "))
                match answer_one_ten:
                    case 1:
                        print("Last call cost")
                    case 2:
                        print("All calls' cost")
                    case 3:
                        print("Clear counters")
            case 7:
                print("Call cost settings")
                print("1. Call cost limit\n2. Show cost in")
                answer_one_one = int(input(">>>>>>>> "))
                match answer_one_one:
                    case 1:
                        print("Call cost limit")
                    case 2:
                        print("Show cost in")
            case 8:
                print("Prepaid credit")

    case 5:
        print("Tones")
        print("1. Ringing tone\n2. Ringing volume\n3. Incoming call alert\n4. Composer\n5. Message alert tone\n6. Keypad tone\n7. Warning and game tones\n8. Vibrating alert\n9. Screen saver")
        number_five = int(input(">>>>>>>> "))
        match number_five:
            case 1:
                print("Ringing tone")
            case 2:
                print("Ringing volume")
            case 3:
                print("Incoming call alert")
            case 4:
                print("Composer")
            case 5:
                print("Message alert tone")
            case 6:
                print("Keypad tone")
            case 7:
                print("Warning and game tones")
            case 8:
                print("Vibrating alert")
            case 9:
                print("Screen saver")

    case 6:
        print("Settings")
        print("1. Call settings\n2. Phone settings\n3. Security settings\n4. Restore factory")
        number_six = int(input(">>>>>>>> "))
        match number_six:
            case 1:
                print("Call settings")
                print("1. Automatic redial\n2. Speed Dialling\n3. Call waiting option\n4. Own number sending\n5. Phone line in use\n6. Automatic answer")
                number_six_one1 = int(input(">>>>>>>> "))
                match number_six_one1:
                    case 1:
                        print("Automatic redial")
                    case 2:
                        print("Speed Dialling")
                    case 3:
                        print("Call waiting option")
                    case 4:
                        print("Own number sending")
                    case 5:
                        print("Phone line in use")
                    case 6:
                        print("Automatic answer")
            case 2:
                print("Phone settings")
                print("1. Language\n2. Cell info display\n3. Welcome note\n4. Network selection\n5. Light\n6. Confirm SIM service action")
                number_six_one2 = int(input(">>>>>>>> "))
                match number_six_one2:
                    case 1:
                        print("Language")
                    case 2:
                        print("Cell info display")
                    case 3:
                        print("Welcome note")
                    case 4:
                        print("Network selection")
                    case 5:
                        print("Light")
                    case 6:
                        print("Confirm SIM service action")
            case 3:
                print("Security settings")
                print("1. PIN code error\n2. Call barring service\n3. Fixed dials\n4. Closed user group\n5. Phone security\n6. Change access code")
                number_six_one3 = int(input(">>>>>>>> "))
                match number_six_one3:
                    case 1:
                        print("PIN code error")
                    case 2:
                        print("Call barring service")
                    case 3:
                        print("Fixed dials")
                    case 4:
                        print("Closed user group")
                    case 5:
                        print("Phone security")
                    case 6:
                        print("Change access code")
            case 4:
                print("Restore factory settings")

    case 7:
        print("Call Divert")
    case 8:
        print("Games")
    case 9:
        print("Calculator")
    case 10:
        print("Reminder")
    case 11:
        print("Clock")
        print("1. Alarm clock\n2. Clock settings\n3. Date settings\n4. Stop Watch\n5. Countdown Timer\n6. Auto update of time and date")
        number_six_one4 = int(input(">>>>>>>> "))
        match number_six_one4:
            case 1:
                print("Alarm clock")
            case 2:
                print("Clock settings")
            case 3:
                print("Date settings")
            case 4:
                print("Stop Watch")
            case 5:
                print("Countdown Timer")
            case 6:
                print("Auto update of time and date")
    case 12:
        print("Profiles")
    case 13:
        print("SIM Services")

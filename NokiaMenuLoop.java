import java.util.Scanner;

public class NokiaMenuLoop {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        boolean mainMenu = true;

        while (mainMenu) {
            System.out.print("Select a menu:\n1. Phone book\n2. Messages\n3. Chat\n4. Call register\n5. Tones\n6. Settings\n7. Call Divert\n8. Games\n9. Calculator\n10. Reminder\n11. Clock\n12. Profiles\n13. SIM Services\n0. Exit\n>>>>>>>> ");
            int answer = scan.nextInt();

            switch (answer) {
                case 1: 
                    boolean phoneBookMenu = true;
                    while (phoneBookMenu) {
                        System.out.print("Phone Book:\n1. Search\n2. Service Nos.\n3. Add Name\n4. Erase\n5. Edit\n6. Assign Tone\n7. Send b'card\n8. Options\n9. Speed Dials\n10. Voice Tags\n0. Back\n>>>>>>>> ");
                        int phoneBookChoice = scan.nextInt();
                        switch (phoneBookChoice) {
                            case 1:
                                System.out.println("Search");
                                break;
                            case 2:
                                System.out.println("Service Nos");
                                break;
                            case 3:
                                System.out.println("Add Name");
                                break;
                            case 4:
                                System.out.println("Erase");
                                break;
                            case 5:
                                System.out.println("Edit");
                                break;
                            case 6:
                                System.out.println("Assign Tone");
                                break;
                            case 7:
                                System.out.println("Send b'card");
                                break;
                            case 8:
                                boolean optionsMenu = true;
                                while (optionsMenu) {
                                    System.out.print("Options:\n1. Type of View\n2. Memory Status\n0. Back\n    >>>>>>>> ");
                                    int optionsChoice = scan.nextInt();
                                    switch (optionsChoice) {
                                        case 1:
                                            System.out.println("      Type of View");
                                            break;
                                        case 2:
                                            System.out.println("      Memory Status");
                                            break;
                                        case 0:
                                            optionsMenu = false; 
                                            break;
                                    }
                                }
                                break;
                            case 9:
                                System.out.println("Speed Dials");
                                break;
                            case 10:
                                System.out.println("Voice Tags");
                                break;
                            case 0:
                                phoneBookMenu = false; // Go back to the main menu
                                break;
                        }
                    }
                    break;

                case 2: // Messages
                    boolean messagesMenu = true;
                    while (messagesMenu) {
                        System.out.print("Messages:\n1. Write Messages\n2. Inbox\n3. Outbox\n4. Picture Messages\n5. Templates\n6. Smileys\n7. Message Settings\n8. Info Service\n9. Voice Mailbox Number\n10. Service Command Editor\n0. Back\n>>>>>>>> ");
                        int messageChoice = scan.nextInt();
                        switch (messageChoice) {
                            case 1:
                                System.out.println("Write Messages");
                                break;
                            case 2:
                                System.out.println("Inbox");
                                break;
                            case 3:
                                System.out.println("Outbox");
                                break;
                            case 4:
                                System.out.println("Picture Messages");
                                break;
                            case 5:
                                System.out.println("Templates");
                                break;
                            case 6:
                                System.out.println("Smileys");
                                break;
                            case 7: // Message Settings
                                boolean messageSettingsMenu = true;
                                while (messageSettingsMenu) {
                                    System.out.print("Message Settings:\n1. Set 1\n2. Common\n0. Back\n    >>>>>>>> ");
                                    int messageSettingsChoice = scan.nextInt();
                                    switch (messageSettingsChoice) {
                                        case 1:
                                            System.out.print("Set 1:\n1. Message Center Number\n2. Message Sent As\n3. Message Validity\n0. Back\n>>>>>>>> ");
                                            int set1Choice = scan.nextInt();
                                            if (set1Choice == 0) {
                                                break;
                                            } else {
                                                System.out.println("Option " + set1Choice);
                                            }
                                            break;
                                        case 2:
                                            System.out.print("Common:\n1. Delivery Report\n2. Reply via Same Centre\n3. Character Support\n0. Back\n      >>>>>>>> ");
                                            int commonChoice = scan.nextInt();
                                            if (commonChoice == 0) {
                                                break; // Back to Message Settings
                                            } else {
                                                System.out.println("Option " + commonChoice);
                                            }
                                            break;
                                        case 0:
                                            messageSettingsMenu = false; 
                                            break;
                                    }
                                }
                                break;
                            case 8:
                                System.out.println("Info Service");
                                break;
                            case 9:
                                System.out.println("Voice Mailbox Number");
                                break;
                            case 10:
                                System.out.println("Service Command Editor");
                                break;
                            case 0:
                                messagesMenu = false; 
                                break;
                        }
                    }
                    break;

                case 3:
                    System.out.println("Chat");
                    break;
                case 4:
                    System.out.println("Call Register");
                    break;
                case 5:
                    System.out.println("Tones");
                    break;
                case 6:
                    System.out.println("Settings");
                    break;
                case 7:
                    System.out.println("Call Divert");
                    break;
                case 8:
                    System.out.println("Games");
                    break;
                case 9:
                    System.out.println("Calculator");
                    break;
                case 10:
                    System.out.println("Reminder");
                    break;
               case 11: // Clock
                    boolean clockMenu = true;
                    while (clockMenu) {
                        System.out.print("Clock:\n1. Alarm Clock\n2. Clock Settings\n3. Date Settings\n4. Stop Watch\n5. Countdown Timer\n6. Auto-update of Time and Date\n0. Back\n>>>>>>>> ");
                        int clockChoice = scan.nextInt();
                        switch (clockChoice) {
                            case 1:
                                System.out.println("  Alarm Clock");
                                break;
                            case 2:
                                System.out.println("  Clock Settings");
                                break;
                            case 3:
                                System.out.println("  Date Settings");
                                break;
                            case 4:
                                System.out.println("  Stop Watch");
                                break;
                            case 5:
                                System.out.println("  Countdown Timer");
                                break;
                            case 6:
                                System.out.println("  Auto-update of Time and Date");
                                break;
                            case 0:
                                clockMenu = false; // Go back to main menu
                                break;
                        }
                    }
                    break;

                case 12:
                    System.out.println("  Profiles");
                    break;
                case 13:
                    System.out.println("  SIM Services");
                    break;
                case 0:
                    mainMenu = false; // Exit the program
                    System.out.println("Exiting program...");
                    break;
                default:
                    System.out.println("Invalid selection, please try again.");
                    break;
}
}
}
}
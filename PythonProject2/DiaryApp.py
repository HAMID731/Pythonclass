from Diaries import Diaries

def main():
    diaries = Diaries()

    while True:
        print("\nWelcome to your Diary App!")
        print("1. Create a new diary")
        print("2. Log in to an existing diary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                try:
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    diaries.add(username, password)
                    print("Diary created successfully!")
                except Exception as e:
                    print(f"Oops! Something went wrong creating the diary: {e}")

            case "2":
                try:
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    diary = diaries.find_by_username(username)

                    if diary:
                        unlock_result = diary.unlock_diary(password)
                        print(unlock_result)

                        if unlock_result == "successfully unlocked!!":
                            while True:
                                print("\nDiary Menu:")
                                print("1. Create an entry")
                                print("2. View an entry")
                                print("3. Update an entry")
                                print("4. Delete an entry")
                                print("5. Lock diary")
                                print("6. Exit diary")

                                diary_choice = input("Enter your choice: ")

                                match diary_choice:
                                    case "1":
                                        try:
                                            title = input("Enter entry title: ")
                                            body = input("Enter entry body: ")
                                            create_result = diary.create_entry(title, body)
                                            print(create_result)
                                        except Exception as e:
                                            print(f"Uh oh! There was a problem creating the entry: {e}")

                                    case "2":
                                        try:
                                            entry_id = int(input("Enter entry ID to view: "))
                                            entry = diary.find_entry_by_id(entry_id)
                                            if isinstance(entry, str):
                                                print(entry)
                                            elif entry:
                                                print(f"Title: {entry.title}")
                                                print(f"Body: {entry.body}")
                                                print(f"Date Created: {entry.dateCreated}")
                                            else:
                                                print("Sorry, that entry ID doesn't exist.")
                                        except ValueError:
                                            print("Please enter a number for the entry ID.")
                                        except Exception as e:
                                            print(f"Oops! Something went wrong viewing the entry: {e}")

                                    case "3":
                                        try:
                                            entry_id = int(input("Enter entry ID to update: "))
                                            title = input("Enter new title: ")
                                            body = input("Enter new body: ")
                                            diary.update_entry(entry_id, title, body)
                                            print("Entry updated successfully!")
                                        except ValueError:
                                            print("Please enter a number for the entry ID.")
                                        except Exception as e:
                                            print(f"Uh oh! There was a problem updating the entry: {e}")

                                    case "4":
                                        try:
                                            entry_id = int(input("Enter entry ID to delete: "))
                                            delete_result = diary.delete_entry(entry_id)
                                            print(delete_result)
                                        except ValueError:
                                            print("Please enter a number for the entry ID.")
                                        except Exception as e:
                                            print(f"Oops! Something went wrong deleting the entry: {e}")

                                    case "5":
                                        diary.lock_diary()
                                        print("Diary locked.")

                                    case "6":
                                        break

                                    case _:
                                        print("Invalid choice. Please try again.")

                        else:
                            print("Incorrect password.")

                    else:
                        print("Diary not found.")
                except Exception as e:
                    print(f"Uh oh! There was a problem logging in: {e}")

            case "3":
                break

            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
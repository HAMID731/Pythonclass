message = """enter 1 for java
enter 2 for python: """

option = int(input(message))
match option:
	case 1:
		print("This is java")
	case 2:
		print("python is great")
	case _:
		print("default")
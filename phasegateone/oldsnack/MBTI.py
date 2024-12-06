
scanner = input
personality_type = ""
print("What is your name? ", end="")
name = scanner().strip()

print(f"Hello, {name}. Please answer each question with 'A' or 'B'.")

questions_ei = [
	"\n1. (E/I) expend energy, enjoy groups - conserve energy, enjoy one-on-one",
	"2. (E/I) seek many tasks, public activities, interaction with others - seek private, solitary activities with quiet to concentrate",
	"3. (E/I) more outgoing, think out loud - more reserved, think to yourself",
	"4. (E/I) external, communicative, express yourself - internal, reticent, keep to yourself",
	"5. (E/I) active, initiate - reflective, deliberate"
	]
questions_sn = [
	"\n6. (S/N) interpret literally - look for meaning and possibilities",
	"7. (S/N) practical, realistic, experiential - imaginative, innovative, theoretical",
	"8. (S/N) standard, usual, conventional - different, novel, unique",
	"9. (S/N) focus on here-and-now - look to the future, global perspective, big picture",
	"10. (S/N) facts, things, 'what is' - ideas, dreams, 'what could be', philosophical"
	]
questions_tf = [
	"\n11. (T/F) logical, thinking, questioning - empathetic, feeling, accommodating",
	"12. (T/F) candid, straight forward, frank - tactful, kind, encouraging",
	"13. (T/F) firm, tend to criticize, hold the line - gentle, tend to appreciate, conciliate",
	"14. (T/F) tough-minded, just - tender-hearted, merciful",
	"15. (T/F) matter of fact, issue-oriented - sensitive, people-oriented, compassionate"
	]
questions_jp = [
	"\n16. (J/P) organized, orderly - flexible, adaptable",
	"17. (J/P) plan, schedule - unplanned, spontaneous",
	"18. (J/P) regulated, structured - easygoing, 'live' and 'let live'",
	"19. (J/P) preparation, plan ahead - go with the flow, adapt as you go",
	"20. (J/P) control, govern - latitude, freedom"
	]

def ask_questions(questions):
	a_count = 0
	b_count = 0
	for question in questions:
		print(question, end=" ")
		answer = scanner().strip().upper()
		while answer not in ("A", "B"):
			print("Invalid input. Please retry.")
			print(question, end=" ")
			answer = scanner().strip().upper()
		if answer == "A":
			a_count += 1
		else:
			b_count += 1
	return a_count, b_count

ei_a, ei_b = ask_questions(questions_ei)
personality_type += "E" if ei_a >= ei_b else "I"
print(f"E/I: A = {ei_a}, B = {ei_b}")

sn_a, sn_b = ask_questions(questions_sn)
personality_type += "S" if sn_a >= sn_b else "N"
print(f"S/N: A = {sn_a}, B = {sn_b}")

tf_a, tf_b = ask_questions(questions_tf)
personality_type += "T" if tf_a >= tf_b else "F"
print(f"T/F: A = {tf_a}, B = {tf_b}")

jp_a, jp_b = ask_questions(questions_jp)
personality_type += "J" if jp_a >= jp_b else "P"
print(f"J/P: A = {jp_a}, B = {jp_b}")

print(f"\n{name}, your MBTI personality type is: {personality_type}")



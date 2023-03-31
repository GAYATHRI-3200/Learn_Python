S1 = input()
S2 = input()

P1 = "Abhinav Wins"
P2 = "Anjali Wins"
if S1 == S2:
    print("Tie")
elif S1 == "Scissors" and S2 == "Paper":
    print(P1)
elif S2 == "Scissors" and S1 == "Paper":
    print(P2)
elif S1 == "Scissors" and S2 == "Rock":
    print(P2)
elif S2 == "Scissors" and S1 == "Rock":
    print(P1)
elif S2 == "Paper" and S1 == "Rock":
    print(P2)
elif S1 == "Paper" and S2 == "Rock":
    print(P1)
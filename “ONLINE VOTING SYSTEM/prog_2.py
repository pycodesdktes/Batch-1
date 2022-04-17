print("Name of the candidates are: ")
candidates = {
    "Raj": "806",
    "Sita": "504",
    "Shree": "403",
}
for key, value in candidates.items():
    print(key, value, sep=" : ")

voted = []
voters_id = [101, 102, 103, 104, 105, 106]
Raj_votes = 0
Sita_votes = 0
Shree_votes = 0

while True:
    if voters_id == []:
        print("Voting is over")
        if Raj_votes > Sita_votes:
            if Raj_votes > Shree_votes:
                print("Raj wins")
        elif Sita_votes > Raj_votes:
            if Sita_votes > Shree_votes:
                print(" Sita wins")
        else:
            print("Shree wins")
        break
    else:
        voter = int(input("Enter voter's id: "))
        if voter in voted:
            print("You already voted")
        else:
            if voter in voters_id:
                choice = int(input("Enter your choice: "))
                if choice == 806:
                    Raj_votes += 1
                    print("Thanks for voting")
                elif choice == 504:
                    Sita_votes += 1
                    print("Thanks for voting")
                elif choice == 403:
                    Shree_votes += 1
                    print("Thanks for voting")
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("You are not allowed to vote")

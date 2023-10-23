import random
l=["rock","paper","scissor"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
                 Game START
                 1.Yes
                 2.No|Exit'''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
                                1.Rock
                                2.Paper
                                3.Scissor
                                '''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="paper"
            elif userinput==3:
                uchoice="scissor"
            else:
                print("Invalid choice")
            cchoice=random.choice(l)
            if cchoice==uchoice:
                print("Ccomputer value:",cchoice)
                print("User value:",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock" and cchoice=="scissor") or (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="paper"):
                print("Ccomputer value:",cchoice)
                print("User value:",uchoice)
                print("You win")
                ucount=ucount+1
            else:
                print("Ccomputer value:",cchoice)
                print("User value:",uchoice)
                print("Computer win")
                ccount=ccount+1
        if ucount==ccount:
            print("Finally Game Draw")
            print("User score:",ucount)
            print("computer score:",ccount)
        elif ucount>ccount:
            print("Finally you win the game")
            print("User score:",ucount)
            print("computer score:",ccount)
        else:
            print("Finally computer win the game")
            print("User score:",ucount)
            print("computer score:",ccount)
    else:
        break

            
            
def rock_paper_scissor(num1,num2,bit1,bit2):
      p1=int(num1[bit1])%3
      p2=int(num2[bit2])%3
      if(player_one[p1]==player_two[p2]):
          print("draw")
      elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
          print(p1name,"wins!! because  they chose Rock over {0}'s Scisscor".format(p2name))
      elif(player_one[p1]=="Rock" and player_two[p2]=="Paper"):
        print(p2name,"wins!! because  they chose Paper over {0}'s Rock".format(p1name))
      elif(player_one[p1]=="Paper" and player_two[p2]=="Scissor"):
          print(p2name,"wins!! because  they chose Scissor over {0}'s Paper".format(p1name))
      elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
          print(p1name,"wins!! because  they chose Paper over {0}'s Rock".format(p2name))
      elif(player_one[p1]=="Scissor" and player_two[p2]=="Rock"):
          print(p2name,"wins!! because  they chose Rock over {0}'s Scissor".format(p1name))
      elif(player_one[p1]=="Scissor" and player_two[p2]=="Paper"):
          print(p1name,"wins!! because  they chose Scissor over {0}'s Paper".format(p2name))
print("Let's play ROCK-PAPER-SCISSORS!")
print("Let's get started!")
p1name=input("player1 enter ur name: ")
p2name=input("player2 enter ur name: ")
player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Paper',1:'Rock',2:'Scissor'}
while(1):
    num1=(input("{0} enter any number of ur choice ".format(p1name)))
    num2=(input("{0} enter any number of ur choice ".format(p2name)))
    bit1=int(input("{0} enter the secret bit position starting from 0 to {1} ".format(p1name,len(num1)-1)))
    bit2=int(input("{0} enter the secret bit position  out of 0 to {1} ".format(p2name,len(num2)-1)))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("do you want to continue? y/n:if u want to continue press y otherwise press n ")
    if(ch=='n'):
        print("Game has ended!")
        break
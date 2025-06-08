import random

#seed for reproducibility
random.seed(42)

#======== Classes ========#
class Miner:
    def __init__(self,name):
        self.name=name
        self.power=random.randint(1,100) #Random computation of power

    def __str__(self):
        return f"{self.name}(Power: {self.power})"

class Staker:
    def __init__(self,name):
        self.name=name
        self.stake=random.randint(1,100) #Random amount of stakes

    def __str__(self):
        return f"{self.name}(Stakes: {self.stake})"

class Delegate:
    def __init__(self,name):
        self.name=name
        self.votes=0

    def __str__(self):
        return f"{self.name}(Votes: {self.votes})"

class Voter:
    def __init__(self,name):
        self.name=name

    def votes(self,delegate):
        choice=random.choice(delegate)  #Random recieved votes
        choice.votes+=1 #increment vote count of selected delegate
        return choice.name

#======== Validators ========#

#PoW miner
miner=[Miner("MinerA"),Miner("MinerB"),Miner("MinerC")]

#PoS staker
staker=[Staker("StakerA"),Staker("StakerB"),Staker("StakerC")]

#DPoS :Delegates and voters
delegate=[Delegate("DelegateA"),Delegate("DelegateB"),Delegate("DelegateC")]
voters=[Voter("VoterA"),Voter("VoterB"),Voter("VoterC")]

#======== Simulation ========#

print("PoW")
for m in miner:
    print(f" {m}") #print each miner's power
pow_winner=max(miner,key=lambda m:m.power) 
print("console.log: Selected miner with highest computational power")
print(f"Winner: {pow_winner.name}(Power:{pow_winner.power})\n")

print("PoS")
for s in staker:
    print(f"{s}") # print each staker's stake
pos_winner=max(staker,key=lambda s:s.stake)
print("console.log: Selected staker with highest stakes")
print(f"Winner: {pos_winner.name}(Power:{pos_winner.stake})\n")

print("DPoS")
vote_list={} #track whose vote came from whom
#each voter votes for one delegate
for v in voters:
    voted_for=v.votes(delegate)
    vote_list[v.name]=voted_for #store teh vote
for d in delegate:
    print(f"{d}") #display each delegate's vote

print("console.log: Voters cast their votes and Delegate with max votes is selected")
max_votes=max(d.votes for d in delegate)
top_delegate=[d for d in delegate if d.votes==max_votes]
dpos_winner=random.choice(top_delegate)
print(f"Votes cast: {vote_list}")
print(f"Winner: {dpos_winner.name}(Votes:{dpos_winner.votes})\n")


# to run this file you need to install pygame and numpy
# pip install pygame (python2) or pip3 install pygame (python3)
# pip install numpy
from util import *


import random

def initBoard(n):
    board=[]
    # Write code to return a random board
    for i in range(n):
        board.append(random.randint(0,n-1))
    return board


def getCost(board):
    cost=0
    # Write code to compute the number 
    # of queen that are attacking each other
    for i in range(len(board)):
        for j in range(i+1,len(board)):
            if(board[j]==board[i] or board[j]==board[i]+j-i or board[j]==board[i]-j+i):
                cost+=1
    return cost

def getBestNeighbour(board):
    # loop over all neighbors and return the one
    # that has the smallest cost.
    # if multiple neighbors have the same minimum cost
    # return one of then at random
    child=[]
    for i in range(len(board)):
        v=board[i]
        for j in range(len(board)):
            if (j==v):
                continue
            board[i]=j
            child.append((getCost(board),board.copy()))
        board[i]=v
    
    m=min(child)
    lmin=[child[i] for i,x in enumerate(child) if x[0]==m[0]]
    return random.choice(lmin)



def HillClimbing(board,l=0):
    # Implement hill climbing assume no sideway moves
    # return the final board with its cost and the 
    # number of iterations it took to finish
    m=getCost(board)
    cnt=0
    side=0
    while True:
        cnt+=1
        cost,newBoard=getBestNeighbour(board)
        if (cost>m) :
            break
        if(cost==m):
            side+=1
            if(side==l):
                break
           
        if (cost==0):
            board=newBoard.copy()
            m=cost
            break
        board=newBoard.copy()
        m=cost
        if (cost<m):
            side=0
        
    
    return (board,cost,cnt)
    
import numpy as np
def GeneticAlgorithm(size):
    population=[]
    # implement the genetic algorithm here
    N=4
    solutionFitness=size*(size-1)/2
    for i in range(N):
        population.append(initBoard(size))
    while True:
        fitness=[]
        for board in population:
            c=getCost(board)
            if(c==0):
                return board
            fitness.append(solutionFitness-c)
        s=sum(fitness)
        for i in range(N):
            fitness[i]/=(1.0*s)

        newpop=[]
        for i in range(N):
            idx=np.random.choice(range(N),1,p=fitness)[0]
            newpop.append(population[idx])
        population=newpop
        #crossover
        for i in range(0,N,2):
            c1=population[i]
            c2=population[i+1]
            population.remove(c1)
            population.remove(c2)
            idx=random.randint(0,size-1)
            population.append(c1[0:idx+1]+c2[idx+1:size])
            population.append(c2[0:idx+1]+c1[idx+1:size])

        #mutation 10%
        for i in range(N):
            if(random.random()>0.9):
                idx=random.randint(0,size-1)
                population[i][idx]=random.randint(0,size-1)


# To run the genetic algorithm 
b=GeneticAlgorithm(8)
draw(b)

# To run hill climbing with sideway moves uncomment this section

"""

cntsucc=0
cntfail=0
sumsucc=0
sumfail=0
finalboard=[]
N=100
for i in range(N):
    b=initBoard(8)
    (board,cost,cnt)=HillClimbing(b,100)
    if (cost==0):
        #print("Solution found")
        #draw(board)
        cntsucc+=1
        sumsucc+=cnt
        finalboard=board.copy()
    else:
        #print("Solution not found, final cost= "+str(cost))
        cntfail+=1
        sumfail+=cnt
print("Success rate= "+str(1.0*cntsucc/N))
print("Fail rate= "+str(1.0*cntfail/N))
print("Average succ iterations= "+str(1.0*sumsucc/cntsucc))
print("Average fail iterations= "+str(1.0*sumfail/cntfail))      
draw(finalboard)
input('Press enter to quit...')
pygame.quit()
"""

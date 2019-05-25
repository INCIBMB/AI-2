import pygame

def draw2D(board):
    pygame.quit()
    pygame.init()
    img = pygame.image.load('queen.png')
    size = 50/len(board)
    gameDisplay = pygame.display.set_mode((600,600))
    white,black,red = (255,255,255),(255,0,0),(255,0,0)
    #board length, must be even
    boardLength = 8
    gameDisplay.fill(white)

    cnt = 0
    for i in range(1,boardLength+1):
        for z in range(1,boardLength+1):
            #check if current loop value is even
            if cnt % 2 == 0:
                pygame.draw.rect(gameDisplay, white,[size*z,size*i,size,size])
                
            else:
                pygame.draw.rect(gameDisplay, black, [size*z,size*i,size,size])
            if(board[i-1][z-1]):
                gameDisplay.blit(img,(size*z+0.1*size,size*i+0.1*size))
            cnt +=1
        #since theres an even number of squares go back one value
        cnt-=1
    #Add a nice boarder
    pygame.draw.rect(gameDisplay,black,[size,size,boardLength*size,boardLength*size],1)

    pygame.display.update()

def draw(board):
    pygame.quit()
    pygame.init()
    img = pygame.image.load('queen.png')
    size = 500.0/len(board)
    gameDisplay = pygame.display.set_mode((700,700))
    white,black,red = (255,255,255),(255,0,0),(255,0,0)
    #board length, must be even
    boardLength = len(board)
    gameDisplay.fill(white)

    cnt = 0
    for i in range(1,boardLength+1):
        for z in range(1,boardLength+1):
            #check if current loop value is even
            if cnt % 2 == 0:
                pygame.draw.rect(gameDisplay, white,[size*z,size*i,size,size])
                
            else:
                pygame.draw.rect(gameDisplay, black, [size*z,size*i,size,size])
            if(board[z-1]==i-1):
                gameDisplay.blit(pygame.transform.scale(img,(int(50*8/boardLength),int(50*8/boardLength))),(size*z+0.1*size,size*i+0.1*size))
            cnt +=1
        #since theres an even number of squares go back one value
        cnt-=1
    #Add a nice boarder
    pygame.draw.rect(gameDisplay,black,[size,size,boardLength*size,boardLength*size],1)

    pygame.display.update()

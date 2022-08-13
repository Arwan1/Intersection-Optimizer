import pygame
from pygame.locals import *
import time
import os
import car_function as cf

print("Welcome")
time.sleep(0.1)
print("The Controls are as follows")
time.sleep(0.1)
print("")
print("Right Arrow Key to add cars GOING right")
print("")
print("Left Arrow Key to add cars GOING Left")
print("")
print("Up Arrow Key to add cars GOING Up")
print("")
print("Down Arrow Key to add cars GOING Down")
print("")
entervariable=input("Press Enter to Start Simulation")

rldata=[]
uddata=[]

x=1
pygame.init()
win=pygame.display.set_mode((640,480))
light_rl=("green")
light_ud=("red")

bg = pygame.image.load(os.path.join("./", "background.png"))
pygame.display.set_caption("traffic")


run=True

x_r=0
y_r=260
list_r=[]

x_l=640
y_l=200
list_l=[]

x_d=280
y_d=0
list_d=[]

x_u=340
y_u=480
list_u=[]

##def frame():
##    win.blit(bg, (0,0))
##    pygame.draw.rect(win,(255,0,0),(list_r[i],y_r,20,20))
##    pygame.display.update()
##    win.fill((0,0,0))
    

while run:
    win.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=False
    if 1==1:#event.type == pygame.KEYDOWN:
        keys=pygame.key.get_pressed()


        if keys[pygame.K_RIGHT]:        #TO RIGHT

            list_r.append(x_r)
        countlist_r=len(list_r)
        if countlist_r==0:
            tasdf=0
        else:
                   
            for i in range (countlist_r):
                        

                list_r[i]=cf.car_r(list_r,light_rl,i)
                    
                    
                
                        
                pygame.draw.rect(win,(255,0,0),((list_r[i],y_r),(20,20)))
            

        if keys[pygame.K_LEFT]:         #TO LEFT

            list_l.append(x_l)
        countlist_l=len(list_l)
        if countlist_l==0:
            tasdf=0
        else:
                   
            for o in range (countlist_l):
                        

                list_l[o]=cf.car_l(list_l,light_rl,o)

                        
                pygame.draw.rect(win,(255,0,0),((list_l[o],y_l),(20,20)))
        
        if keys[pygame.K_DOWN]:         #DOWN

            list_d.append(y_d)
        countlist_d=len(list_d)
        if countlist_d==0:
            tasdf=0
        else:
                   
            for p in range (countlist_d):
                        

                list_d[p]=cf.car_d(list_d,light_ud,p)

                        
                pygame.draw.rect(win,(255,0,0),((x_d,list_d[p]),(20,20)))
                
        if keys[pygame.K_UP]:           #UP

            list_u.append(y_u)
        countlist_u=len(list_u)
        if countlist_u==0:
            tasdf=0
        else:
                   
            for q in range (countlist_u):
                        

                list_u[q]=cf.car_u(list_u,light_ud,q)

                        
                pygame.draw.rect(win,(255,0,0),((x_u,list_u[q]),(20,20)))


    if light_ud=="green":
        pygame.draw.circle(win,(0,255,0),[320,330],5,0)
        pygame.draw.circle(win,(0,255,0),[320,130],5,0)
    else:
        pygame.draw.circle(win,(255,0,0),[320,330],5,0)
        pygame.draw.circle(win,(255,0,0),[320,130],5,0)

    if light_rl=="green":
        pygame.draw.circle(win,(0,255,0),[220,240],5,0)
        pygame.draw.circle(win,(0,255,0),[410,240],5,0)
    else:
        pygame.draw.circle(win,(255,0,0),[220,240],5,0)
        pygame.draw.circle(win,(255,0,0),[410,240],5,0)


    time.sleep(0.001)    
    pygame.display.update()
    win.fill((0,0,0))

    for n in range(len(list_r)-1):
        if list_r[n]>=700:
            list_r.pop(n)
            
    for g in range(len(list_l)-1):
        if list_l[g]<=-10:
            list_l.pop(g)
            
    for c in range(len(list_d)-1):
        if list_d[c]>=490:
            list_d.pop(c)
            
    for b in range(len(list_u)-1):
        if list_u[b]<=-10:
            list_u.pop(b)

    
    x=x+1
    #print(x)

    
    if x%100==0:
        if len(list_r)+len(list_l)>=len(list_d)+len(list_u):
            if light_rl=="red":
                switch="rl"
                light_ud="red"
                light_rl="red"
                #print("Step 1")
            else:
                switch="NA"
                #print("Step 2")
        elif light_ud=="red":
            switch="ud"
            light_ud="red"
            light_rl="red"
            #print("Step 3")
        else:
            switch="NA"
            #print("Step 4")
        rldata.append(len(list_r)+len(list_l))
        uddata.append(len(list_d)+len(list_u))

    if (x%500==0)and(x%1000!=0):
        #print("Case 1")
        if switch!="NA":
            #print("Case 2")
            if switch=="rl":
                #print("Case 3")
                light_rl="green"
                
            elif switch=="ud":
                #print("Case 4")
                light_ud="green"
        


    #x,y = pygame.mouse.get_pos()
    #print(x,y)






pygame.quit()

access=input("Access data? Yes/No")
if access=="Yes":
    data=int(input("Right To Left road(1), Up to Down(2), or both?(3)"))
    if data==1:
        print("Cars from right to left",rldata)
        print("Total cars=", len(rldata))
    elif data==2:
        print("Cars from Up to Down",uddata)
        print("Total cars=", len(uddata))
    elif data==3:
        print("Cars from right to left",rldata)
        print("")
        print("Cars from Up to Down",uddata)
        print("")
        print("Total Righ-left cars =", len(rldata))
        print("")
        print("Total Up-Down cars=", len(uddata))
        print("")
        print("Total Cars=",len(uddata)+len(rldata))
print("")
exit=input("Press ENTER to exit")

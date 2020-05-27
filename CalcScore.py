#This module has the function pt. It calculates the points a player has earned from his statistics 
def pt(runs, balls, fours, sixes, w, b, r,f):
    x=0
    #batting stats
    if balls > 0:
        x = runs/2
        if runs >= 50:
            x+=5
        if runs >= 100:
            x+=10
        if runs/balls >= 0.8 and runs/balls <1:
            x+=2
        elif runs/balls >= 1 :
            x+=4
        x += (fours + 2*sixes)
    #bowling stats
    if b>0 :
        x = x + w*10
        overs = b
        e = float(r/overs)
        if w >= 3:
            x=x + 5
        if w >= 5:
            x=x + 10
        if e >= 2 and e<=3.5:
            x =x + 7
        elif e > 3.5 and e<=4.5 :
            x= x + 4
        elif e <= 2:
            x= x + 10
    #fielding stats
    if f>0:
        x += f*10
    return x

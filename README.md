# AimBotTest
Implement OpenCV to detect enemies' head through hsv and edge filtering on the screen. 
This is done for educational purposes only.  
                  
# Target Game
[Valorant](https://playvalorant.com/en-sg/)

# Context
Better guns that can be bought after 3 rounds into the game, namely [Vandal](https://valorant.fandom.com/wiki/Vandal) and [Phantom](https://valorant.fandom.com/wiki/Phantom), can one-shot enemies if 1 bullet lands on the enemies' head.

# Results in Training Ground (before adjustments)
The enemies can be properly detected, but it still capture the bodies and not just the heads.
![](https://github.com/Stygian84/AimBotTest/blob/main/opencv%20aimbot%20test/docs/aimbot4.jpg)
![](https://github.com/Stygian84/AimBotTest/blob/main/opencv%20aimbot%20test/docs/aimbot1.jpg)
![](https://github.com/Stygian84/AimBotTest/blob/main/opencv%20aimbot%20test/docs/aimbot2.jpg)
![](https://github.com/Stygian84/AimBotTest/blob/main/opencv%20aimbot%20test/docs/aimbot3.jpg)

# Results in Actual Game

![](https://github.com/Stygian84/AimBotTest/blob/main/opencv%20aimbot%20test/docs/aimbot5.jpg)
![](https://github.com/Stygian84/AimBotTest/blob/main/opencv%20aimbot%20test/docs/aimbot6.jpg)
![](https://github.com/Stygian84/AimBotTest/blob/main/opencv%20aimbot%20test/docs/aimbot7.jpg)
![](https://github.com/Stygian84/AimBotTest/blob/main/opencv%20aimbot%20test/docs/aimbot8.jpg)
![](https://github.com/Stygian84/AimBotTest/blob/main/opencv%20aimbot%20test/docs/aimbot9.jpg)
![](https://github.com/Stygian84/AimBotTest/blob/main/opencv%20aimbot%20test/docs/aimbot10.jpg)

# Issues
It is very time-consuming task with my old laptop (Lenovo Legion Y520)
![](https://github.com/Stygian84/AimBotTest/blob/main/opencv%20aimbot%20test/docs/aimbot11.jpg)

# Inspiration
This project is inspired for making new players' who struggle to shoot anything easier.

# Future Improvement
1. Onclick, it will tap the head
2. Make a boundary box where only in areas near the enemies head, the aimbot will get triggered. This is to encourage players to get better by making this boundary box smaller and smaller.

import pyautogui as ag

a,b = map(int, input("x y좌표 ").split())
print(ag.position)
print(ag.size())
횟수 = 0
while True:
    ag.click(a, b, interval=1)
    횟수 += 1
print(횟수)
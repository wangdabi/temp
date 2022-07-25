import easygui,pygame,random,sys
from ui_add import Ui_MainWindow
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
class Append(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.add=[]
        self.setupUi(self)
        self.setup()
        self.show()
    def setup(self):
        self.append.clicked.connect(self.app)
    def app(self):
        self.add.append(self.title.text())
        self.add.append(self.content.text())
        self.add.append(self.choice.text().split(' '))
        self.add.append(self.right.text())
stop=0
song = easygui.choicebox('选择背景音乐（飞机坠毁ing的背景音乐大杂烩，准备好了吗？！）', '设置', ['真相只有一个', 'ツナ觉醒','前前前世（新增曲目）','feel your heart（新增曲目）'])
if song:
    pygame.init()
    pygame.mixer.music.load(song+'.mp3')
    pygame.mixer.music.play(loops=-1)
else:
    easygui.msgbox('欧那就是不要BGM咯？okok那就不要音乐','。。。')
    pygame.mixer.music.stop()
def setting():
    global azs,song,stop
    grow=easygui.choicebox('选择操作','设置',['退出','换音乐','增加题目','存档（?）'])
    if grow=="退出":
        sys.exit()
        easygui.msgbox('那我走了哈。。。','break')
        stop=1
    elif grow=='换音乐':
        if song:
            pygame.init()
            pygame.mixer.music.load(song+'.mp3')
            pygame.mixer.music.play(loops=-1)
        else:
            easygui.msgbox('欧那就是不要BGM咯？okok那就不要音乐', '。。。')
            pygame.mixer.music.stop()
    elif grow=='增加题目':
        easygui.msgbox('哎呀我忘了，这东西还没开放呢！！！','哎哟喂')
        if __name__=='__main__':
            app=QApplication(sys.argv)
            append=Append()
            easygui.msgbox('不知道这东西怎么做，我劝你还是自己存档比较好吧？','Warning')
        azs.append(append.add)
    elif grow=='存档（?）':
        with open('score.txt','w')as f:
            f.write(str(azs))
score = 1
level=0
try:
    with open('score.txt','r',encoding='UTF-8')as f:
        if len(f.read())<=0:
            azs = [['案件1', '老神去咖啡厅，里面有ABCD4个人，一会之后，老神发现A被杀了，案发现场是咖啡厅（这情况好像不太成立），是被咖啡店里的人杀掉的话，杀人fan到底是谁？（提示：B是跟A走的）', ['B', 'A', 'C', '设置', ], 'B'],
                ['案件2', '老神去和ABCD4个人聚会，结果C在去厕所的时候被杀了，门窗都是关着的，那么杀人fan是谁？（提示：C后面紧跟着A）',['A', 'B', 'D', '设置'], 'A'],
                ['案件3', '老神在一家旅馆里，发现A被杀了，门窗都是关着的，屋里有一把断掉的大刀，手柄上面有C的指纹，但是C不在这里，门窗也没血，屋里只有ABC3个人，那么那个杀人fan是谁？', ['B', 'C', '老神', '设置'], 'B']]
        else:
            azs=f.read()
            print(azs)
            
except FileNotFoundError:
    azs = [['案件1', '老神去咖啡厅，里面有ABCD4个人，一会之后，老神发现A被杀了，案发现场是咖啡厅（这情况好像不太成立），是被咖啡店里的人杀掉的话，杀人fan到底是谁？（提示：B是跟A走的）', ['B', 'A', 'C', '设置', ], 'B'],
           ['案件2', '老神去和ABCD4个人聚会，结果C在去厕所的时候被杀了，门窗都是关着的，那么杀人fan是谁？（提示：C后面紧跟着A）', ['A', 'B', 'D', '设置'], 'A'],
           ['案件3', '老神在一家旅馆里，发现A被杀了，门窗都是关着的，屋里有一把断掉的大刀，手柄上面有C的指纹，但是C不在这里，门窗也没血，屋里只有ABC3个人，那么那个杀人fan是谁？', ['B', 'C', '老神', '设置'], 'B']]
while True:
    az=random.choice(list(azs))
    ans=easygui.choicebox(az[1]+f'当前积分：{score}当前等级：LV{level}',az[0],choices=az[2])
    if ans==az[3]:
        score += 1
        easygui.msgbox(msg=f'答√了，积分+1（哇哈）距离下次升级还差{5-(score%5)}积分', title='。。。', image='god.jpeg')
        level=score//5
    elif ans=='设置':
        setting()
        if stop:
            break
    else:
        easygui.msgbox(msg=f'答×了，积分+0（哇哈）', title='。。。', image='god.jpeg')
        score += 0
        

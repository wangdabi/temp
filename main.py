from arcade import *
import time
import random
import easygui,pygame
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 450
SCREEN_TITLE = '宝可梦（划掉）宝柯梦大探险—街边掠影v1.4内测版本'
easygui.msgbox('操作说明：你可以按上下键（键盘上向上/向下的箭头）来选择是获取物资（获得对应物资）还是跳过物资（保存体力），时间到了或者提前用光体力都会停止游戏\n啥？你还要别的说明？除了这些操作就没别的了呀！\n代码：飞机坠毁ing\n图片、音乐：均来自网络\n背景图片：飞机坠毁ing（做的有点烂）\n参考教程均来自网络')
    
class Pika(Sprite):
    def __init__(self, image):
        super().__init__(image)
        self.center_x = 51
        self.center_y = 50
        self.change_y = 1
        # oneself
        self.transport = [0, 0]
        self.energy = 100
        self.seaba = 0
        # infomation card
        self.material = {'gold': 0, 'baoshi': 0, 'steel': 0}
        self.time = 30000
        self.hit='1'
        self.result = [['观察以下图形：△○☆△○☆△  下个图形是啥？（找规律）'  ,'测试题1',('□','△','○'),'○'],
                       ['鸡兔同笼，鸡腿总数比兔腿总数多20条，鸡是兔子的3倍，兔子有几只？（鸡兔同笼）','测试题2',('5','10','7'),'10'],
                        ['一个班级里有20个人，喜欢打羽毛球的有15人，喜欢踢足球又喜欢打羽毛球的有6人，只喜欢踢足球的人有几个？（容斥问题）','测试题3',('1','9','5'),'5']]
    def ifbottom(self):
        if self.center_y > 60+self.seaba:
            self.change_y = -2
        elif self.center_y < 50+self.seaba:
            self.change_y = 1



class Road1(Sprite):
    def __init__(self, image):
        super().__init__(image)
        self.center_x = SCREEN_WIDTH//2
        self.center_y = SCREEN_HEIGHT//2
        self.change_x = -2

    def update(self):
        super().update()
        if self.center_x <= SCREEN_WIDTH//2-SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH//2+SCREEN_WIDTH


class Road2(Sprite):
    def __init__(self, image):
        super().__init__(image)
        self.center_x = SCREEN_WIDTH//2+SCREEN_WIDTH
        self.center_y = SCREEN_HEIGHT//2
        self.change_x = -2

    def update(self):
        super().update()
        if self.center_x <= SCREEN_WIDTH//2-SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH//2+SCREEN_WIDTH


class Steel(Sprite):
    def __init__(self, image):
        super().__init__(image)
        self.image = image
        self.left = SCREEN_WIDTH-10
        # self.center_x=50
        # self.change_x=-2
        self.center_y = 50
        self.hit='0'
        
    def move(self):
        self.center_x -= 2


class Main(Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.stop = False
        self.setup()

    def setup(self):
        #az
        self.text=''
        # sptitelist
        self.monster = SpriteList()
        self.gold = SpriteList()
        self.pikalist=SpriteList()
        # images
        self.golds = ['baoshi.png', 'gold.png']
        self.monsters = ['monster.png']
        self.pikas = ['pika.png','pk1.png']
        # road&sprites
        self.pika = Pika(random.choice(self.pikas))
        self.pikalist.append(self.pika)
        self.road1 = Road1('bg.png')
        self.road2 = Road2('bg.png')
        self.road2.left = self.road1.right
        # timer
        self.nowtime=time.ctime()
        self.creattm=time.ctime()
        self.tm=0
        #self.draw_distance()
        #music musium
        pygame.mixer.init()
        pygame.mixer.music.load('BGM.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)

    def ifright(self,tup,):
        ans=easygui.buttonbox(tup[0],tup[1],tup[2])
        if ans==tup[3]:
            easygui.msgbox('恭喜你答对了','提示',ok_button='继续探险')
            return True
        else:
            easygui.msgbox('很遗憾，答错了', '提示', ok_button='继续探险')
            return False
    def timer(self):
        if time.ctime()!=self.nowtime:
            self.tm+=1
    def draw_distance(self):
        pos_x = 0
        pos_y = SCREEN_HEIGHT-40
        draw_text('jjjj：{}\n fffff：\n fffffx{}  fffrrx{}  hhhx{}'.format(self.pika.energy, self.pika.material['gold'], self.pika.material['baoshi'], self.pika.material['steel']), pos_x, pos_y,
                  color.BLACK, font_name=('simhei', 'PingFang'))

    def on_draw(self):
        start_render()
        self.road1.draw()
        self.road2.draw()
        self.pika.draw()
        pos_x = 0
        pos_y = SCREEN_HEIGHT-40
        draw_text(' 体力值：{}\n 拥有物资如下：\n 黄金x{}  宝石x{}  怪兽合金x{}'.format(self.pika.energy, self.pika.material['gold'], self.pika.material['baoshi'], self.pika.material['steel']), pos_x, pos_y,
                  color.BLACK, font_name=('simhei', 'PingFang'))

        for m in self.monster:
            m.draw()
            m.move()
        for g in self.gold:
            g.draw()
            g.move()

    def on_update(self, delta_time: float):
        if not self.stop:
            self.pika.update()
            self.road1.update()
            self.road2.update()
            self.pika.ifbottom()
            self.timer()
            for b in self.gold:
                if b.right<=0:
                    b.kill()
            for b in self.monster:
                if b.right <= 0:
                    b.kill()
            hit=check_for_collision_with_list(self.pika,self.monster)
            if hit:
                for i in hit:
                    if i.hit=='0':
                        i.kill()
                        self.pika.energy-=5
                        if self.ifright(random.choice(self.pika.result)):
                            self.pika.material['steel']+=1
                            with open('探险日志.txt', 'w')as f:
                                self.text += '宝可梦打败怪兽，获得了一块怪兽合金，但不知道该怎么用。。。\n'
                                f.write(self.text)
                            
                #self.draw_distance()
            get=check_for_collision_with_list(self.pika,self.gold)
            if get:
                for i in get:
                    if i.image=='baoshi.png':
                        i.kill()
                        self.pika.energy -= 3
                        self.pika.material['baoshi']+=1
                        with open('探险日志.txt', 'w')as g:
                            self.text += '宝可梦挖出了一颗宝石，准备带回家做纪念品\n'
                            g.write(self.text)
                            
                    elif i.image == 'gold.png':
                        i.kill()
                        self.pika.energy -= 2
                        self.pika.material['gold']+=1
                        with open('探险日志.txt', 'w')as h:
                            self.text += '宝可梦捡到了一块金子，准备带回家卖钱\n'
                            h.write(self.text)
                            
            #self.draw_distance()
                    

            if int(self.tm) >= self.pika.time or self.pika.energy<=0:
                self.stop = True
                pygame.mixer.stop()
                eg.msgbox(
                    f'''本次探险你总共获得了以下物资：\n金矿x{self.pika.material['gold']}\n宝石x{self.pika.material['baoshi']}\n怪兽合金x{self.pika.material['steel']}''')
                for i in self.gold:
                    i.kill()
                for i in self.monster:
                    i.kill()
            if int(self.tm) % 300 == 0 and time.ctime() != self.creattm:
                self.create()
                self.creattm=time.ctime()
                

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == key.UP and self.pika.seaba <= 100:
            self.pika.seaba += 10
        elif symbol == key.DOWN and self.pika.seaba > 0:
            self.pika.seaba -= 10

    def create(self):
        baoshis = ['baoshi.png', 'gold.png']
        enemies = ['monster.png']
        putincan = random.randint(0, 1)
        if putincan == 0:
            what = random.choice([baoshis, enemies])
            if what == baoshis:
                whatin = random.choice(baoshis)
                enemy = Steel(whatin)
            elif what == enemies:
                whatin = random.choice(enemies)
                enemy = Steel(whatin)
            if enemy.image in enemies:
                self.monster.append(enemy)
            else:
                self.gold.append(enemy)
        #print('ok')


if __name__ == '__main__':
    gm = Main(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()

# coding=utf-8 
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. "
        print "Subclass it and implemnt enter()"
        exit(1)
        
class Death(Scence):

        quips = [
        "你死啦",
        "你妈会为你骄傲的",
        "唉，你个弱鸡",
        "我的狗子玩的都比你好",
        "这让我想起你爸的笑话",
        ]
        def enter(self):
            print(Death.quips[randint(0,len(self.quips)-1)])
            exit(1)
            
class CentralCorridor(Scence):

    def enter(self):
        print(dedent("""
        你的宇宙飞船被外星人入侵了。聪明的你立马想出了对侧————先取出炸弹，订好时，自己再承救生船逃出去。 \n
        正想着，你便从中央走廊出发，准备去武器库。可是，一个黑不溜秋的外星人，把门卡住了。\n
        你会怎么办呢？\n\t
        1.把它推走；\n\t
        2.把它拉出来；\n\t
        3.把它射死；\n\t
        4.讲一个笑话。
        """))
        
        action = input("[请输入数字]>")
        
        if action in ("1","3"):
            print("当你处理好外星人，它背后的队友把你射死了。")
            return 'death'
            
        elif aciton == "2":
            print(dedent("""
            外星人把你压死了。
            """))
            return 'death'
            
        elif action == "4":
            print(dedent("""
            你讲笑话讲到一般，自己突然笑了起来，外星人也跟着笑，笑着笑着就抱着肚子躺在了地上。进门的时候，
            你发现了另一外星人，而它已经被压死了。
            """))
            return("laser_weapon_armory")
            return("center_corridor")
                
class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        爬过胖子和它队友的尸体，你进入了武器库。你扫一遍，这里没有活着的外星人
        你摸到装着中子弹的保险柜那边，你回忆着打开柜子的密码。嗯。。是你的生日？
        """))
        code = "%d%d%d" %(randint(1,9),randint(1,9),randint(1,9))
        guess = raw_input("[keypad]>")
        guess = 0
        
        while guess != code and guesses < 10:
            print("错误！错误！")
            guess += 1
            guess = rew_input("[keypad]>")
            
        if guess == code：
            print "The container clicks open and the seal breaks, letting gas out."
            return 'the_bridge'
        else:
            print(dedent("""
            你用完了所有机会。你打算坐着等死，然后你死了。
            """))
            return 'death'
            
class TheBridge(Scene):
                
    def enter(self):
        print(dedent("""
        你带着子弹走进了中央控制室，你知道里面有五个外星人，准备好玉石俱焚的准备。\n\t
        外星人中子弹就跑了。\n\t
        1. 把炸弹扔过去 \n\t
        2. 安静地放好炸弹\n\t
        3.惊呆了
        """))
        action = input("[你要做啥]>")
        
        if action == "1":
            print(dedent("""
            你感觉到了惊吓，下意识就把炸弹扔了出来。虽然你牺牲了，但你也击败了外星人。
            """))
                return 'death'
                
        elif action == "2":
            print(dedent("""
        你很快反应过来，安置好炸弹后，向救生舱跑去。
        """))
        
            return 'escape_pod'
            
        elif action == "3":
            print("带着干嘛？")
            return "death"
        else:
            print("你很不乖，那就重来吧。")
            return("central_corridor")
            
class EscaPod(Scene):

    def enter(self):
        print(dedent("""
        你发现有五艘船，但你知道只有一艘可以用，而你只有一次机会——没有时间了
        """))
        
        good_pod = randint(1,5)
        print(good_pod)
        guess = input("[pod#]>")
        
        if int(guess) != good_pod:
            print(dedent(f"""
        你跳进{guess}号船，按下发射按钮。然后。。。然后。。。然后。。。
        最后你牺牲了，但你也击败了外星人。
        """))
            return 'death'
        else:
            print(dedent(f"""
           你跳进{guess}号船，按下发射按钮。然后想着地球飞去。
           你不敢回头看，但你知道，这场战斗，你赢了！
           """))
            return 'finished'
            
class Finished(Scene):

    def enter(self):
        print("你自己一个人过上了幸福快乐的生活")
        return 'finished'
        
class Engine(object):

    def __init__(self,scence_map):
        self.scence_map = scene_map
        
    def play(self):
        current_scence = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scence != last_scene:
            #调用<场景名>.enter(),进入场景
            next_scene_name = current_scene.enter()
            # 返回"下一个"场景的场景名，
            current_scence = self.scene_map.next_scene(next_scene_name)
            
        current_scene.enter()

class Map(object):
    scenes = {
        'central_corridor':CentalCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscaPod()
        'death':Death(),
        'finished':Finished(),
        }
        
    def __init__(self,start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()        
        
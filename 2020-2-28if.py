

action = input("[input]> ")

if action in ("1", "3"):
    print("当你处理好外星人，它背后的队友把你射死了。")
    

elif action == "2":
    print(dedent("""
            外星人把你压死了。
            """))
    

elif action == "4":
    print(dedent("""
        你笑话讲到一半，自己却突然笑了起来，可外星人也跟着笑，笑着笑着就抱着肚子躺在了地上，
        你赶紧开枪射死了它。进门的时候，你发现了另外一个外星人，而它已经被压死了。
        """))
    
else:
    print("你很不乖哦，那就重来吧。")
   
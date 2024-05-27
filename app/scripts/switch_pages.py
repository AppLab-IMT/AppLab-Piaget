def switch_to_slash(root):
    root.destroy()  # Destruir a janela principal
    import t01
    t01.t01()


# troca para pagina login 
def switch_to_login(root):
    root.destroy()
    from t02 import t02
    t02()


def switch_to_profile(root, userData):
    root.destroy()
    from t03 import t03
    t03(userData)

    
def switch_to_register(root):
    root.destroy()
    from t04 import t04
    t04()
    
def switch_to_play1(root):
    root.destroy()
    from t05 import t05
    t05()
    
def switch_to_play2(root):
    root.destroy()
    from t06 import t06
    t06()

def switch_to_play3(root):
    root.destroy()
    from t07 import t07
    t07()


def switch_to_ranking(root):
    root.destroy()
    from t08 import t08
    t08()

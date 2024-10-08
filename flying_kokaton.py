import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)#練習２
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    xx=-1
    yy=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()  # 練習8-3：キーの押下状態を取得
        if key_lst[pg.K_UP]:  # 上矢印キーがTrueなら
            yy= yy-1  # こうかとんの縦座標を-1する
        if key_lst[pg.K_DOWN]:  # 下矢印キーがTrueなら
            yy= yy+1# こうかとんの縦座標を+1する
        if key_lst[pg.K_LEFT]:  # 下矢印キーがTrueなら
            xx= xx-1 # こうかとんの横座標を-1する
        if key_lst[pg.K_RIGHT]:
              # 下矢印キーがTrueなら
            xx= xx+2
        kk_rct.move_ip((xx, yy))  # こうかとんの横座標を+1する
        xx=-1
        yy=0
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(kk_img, kk_rct)

        pg.display.update()
        tmr += 1       #aaa 
        clock.tick(400)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

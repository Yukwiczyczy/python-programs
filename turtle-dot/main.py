import msvcrt, os
print("""
      
  _____           _   _        ____       ___ 
 |_   __   _ _ __| |_| | ___  |  _ \  ___|__ \\
   | || | | | '__| __| |/ _ \ | | | |/ _ \ / /
   | || |_| | |  | |_| |  __/ | |_| | (_) |_| 
   |_| \__,_|_|   \__|_|\___| |____/ \___/(_) 
                                              
""")

print("""
      Press the following:
      1 - to draw square
      2 - draw dashline
      3 - draw triangle to dodecagon
      4 - random walk
      5 - draw spinograph
      0 - quit
      """)

while True:
    if msvcrt.kbhit():
        pressed_key = msvcrt.getch()
        
        if pressed_key == b'0':
            print("Hope you enjoyed! ")
            exit
        elif pressed_key == b'1':
            import turtle_square
        elif pressed_key == b'2':
            import turtle_dashline
        elif pressed_key == b'3':
            import turtle_complex_shape
        elif pressed_key == b'4':
            import turtle_random_walk_one
        elif pressed_key == b'5':
            import turtle_spinograph
        else:
            print("\nCannot recognize the key. \n")
            
        
   

# show screen
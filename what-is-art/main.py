import sys
from PIL import Image
from sty import bg, fg, rs




# from gtts import gTTS
from replit import audio

# mytext_one = 'What is art?'
# myobj_one = gTTS(text=mytext_one, lang='en', slow=False)
# myobj_one.save("welcome.mp3")
# list_letters = ['w', 'h', 'a', 't', 'i', 's', 'a', 'r', 't']

# for i in range(0, len(list_letters)):
#   myobj_two = gTTS(text=list_letters[i], lang='en', slow=False)
#   myobj_two.save(f"audio_{i}.mp3")

# mytext_two = "This was, what is art?"
# myobj_three = gTTS(text=mytext_two, lang='en', slow=False)
# myobj_three.save("the_end.mp3")
  
source = audio.play_file("audio_0.mp3")
input()

main_title = """
                                                                                                                
                                                                                                                
____              ___ ___                                                                                       
`Mb(      db      )d' `MM                             68b                                                6MMMb  
 YM.     ,PM.     ,P   MM                 /           Y89                                   /           6M' `Mb 
 `Mb     d'Mb     d'   MM  __      ___   /M           ___   ____            ___   ___  __  /M           `'   MM 
  YM.   ,P YM.   ,P    MM 6MMb   6MMMMb /MMMMM        `MM  6MMMMb\        6MMMMb  `MM 6MM /MMMMM             MM 
  `Mb   d' `Mb   d'    MMM9 `Mb 8M'  `Mb MM            MM MM'    `       8M'  `Mb  MM69 "  MM               ,M9 
   YM. ,P   YM. ,P     MM'   MM     ,oMM MM            MM YM.                ,oMM  MM'     MM              MM9  
   `Mb d'   `Mb d'     MM    MM ,6MM9'MM MM            MM  YMMMMb        ,6MM9'MM  MM      MM              M    
    YM,P     YM,P      MM    MM MM'   MM MM            MM      `Mb       MM'   MM  MM      MM                   
    `MM'     `MM'      MM    MM MM.  ,MM YM.  ,        MM L    ,MM       MM.  ,MM  MM      YM.  ,         68b   
     YP       YP      _MM_  _MM_`YMMM9'Yb.YMMM9       _MM_MYMMMM9        `YMMM9'Yb_MM_      YMMM9         Y89   
                                                                                                                
                                         Héctor Miranda G                                                                       
                                                                                                                


"""
# Playing the converted file
source = audio.play_file("welcome.mp3")



def image_to_ascii(img_path):
    img = Image.open(img_path)
    # changing img size
    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))

    img = img.convert('L') # img to black and white

    pixels = img.getdata()

    chars = [fg(234) + "B" + rs.fg,
             fg(236) + "S" + rs.fg,
             fg(238) + "#" + rs.fg,
             fg(240) + "&" + rs.fg,
             fg(242) + "@" + rs.fg,
             fg(244) + "$" + rs.fg,
             fg(246) + "%" + rs.fg,
             fg(248) + "*" + rs.fg,
             fg(250) + "!" + rs.fg,
             fg(252) + ":" + rs.fg,
             fg(254) + "." + rs.fg]
    pixels_nums = [pixel // 25 for pixel in pixels]
    new_pixels = [chars[pixel//25] for pixel in pixels]
  
    new_pixels_count = len(new_pixels)

    counter_width = 0
    for i in range(0, new_pixels_count):
      if counter_width == new_width:
        print()
        counter_width = 0
      print(new_pixels[i], end='')
      counter_width += 1




# coloe to use

def display_img(k):
  dict_img = {0:"imgs/william_blake.jpg",
              1:"imgs/henri_matisse.jpg",
              2:"imgs/atl.jpg",
              3:"imgs/tamayo.jpg",
              4:"imgs/ignacio-aguirre.jpg",
              5:"imgs/schiele.jpg",
              6:"imgs/antoine_watteau.jpg",
              7:"imgs/rivera.jpg",
              8:"imgs/toledo.jpg"}
  print(dict_img[k])
  image_to_ascii(dict_img[k])

def run_program_two():
  txt = ["what", "is", "art" ,"?"]
  
  for i in range(0, len(txt)):
    print(txt[i] + " ",end='')
  print()
  
  counter = 0
  for i in range(0, len(txt)-1):
    for j in range(len(txt[0])):
      to_input_character = txt[0][0]
      txt[0] = txt[0][1 : : ]
      input_character = 'z'
      while input_character != to_input_character:
        print(to_input_character + "->", end='')
        for k in range(len(txt)):
          print(txt[k] + " ", end='')
        input_character = str(input(": "))
      print()
      source = audio.play_file(f"audio_{counter}.mp3")
      display_img(counter)
      counter += 1
      print()
    txt.pop(0)
  print(txt[0])


print(main_title)
run_program_two()
source = audio.play_file("the_end.mp3") 
print("""
      
                                                                                                                                                                                                                                                                                                                                                                                                            
__________ ___                                                                 68b 68b ____              ___ ___                                                                               68b 68b 
MMMMMMMMMM `MM      68b                                                        Y89 Y89 `Mb(      db      )d' `MM                             68b                                        6MMMb  Y89 Y89 
/   MM   \  MM      Y89                                                        `M' `M'  YM.     ,PM.     ,P   MM                 /           Y89                                   /   6M' `Mb `M' `M' 
    MM      MM  __  ___   ____         ____    _    ___   ___     ____          V   V   `Mb     d'Mb     d'   MM  __      ___   /M           ___   ____            ___   ___  __  /M   `'   MM  V   V  
    MM      MM 6MMb `MM  6MMMMb\       `MM(   ,M.   )M' 6MMMMb   6MMMMb\                 YM.   ,P YM.   ,P    MM 6MMb   6MMMMb /MMMMM        `MM  6MMMMb\        6MMMMb  `MM 6MM /MMMMM     MM         
    MM      MMM9 `Mb MM MM'    `        `Mb   dMb   d' 8M'  `Mb MM'    `                 `Mb   d' `Mb   d'    MMM9 `Mb 8M'  `Mb MM            MM MM'    `       8M'  `Mb  MM69 "  MM       ,M9         
    MM      MM'   MM MM YM.              YM. ,PYM. ,P      ,oMM YM.                       YM. ,P   YM. ,P     MM'   MM     ,oMM MM            MM YM.                ,oMM  MM'     MM      MM9          
    MM      MM    MM MM  YMMMMb          `Mb d'`Mb d'  ,6MM9'MM  YMMMMb                   `Mb d'   `Mb d'     MM    MM ,6MM9'MM MM            MM  YMMMMb        ,6MM9'MM  MM      MM      M            
    MM      MM    MM MM      `Mb          YM,P  YM,P   MM'   MM      `Mb                   YM,P     YM,P      MM    MM MM'   MM MM            MM      `Mb       MM'   MM  MM      MM                   
    MM      MM    MM MM L    ,MM          `MM'  `MM'   MM.  ,MM L    ,MM                   `MM'     `MM'      MM    MM MM.  ,MM YM.  ,        MM L    ,MM       MM.  ,MM  MM      YM.  , 68b           
   _MM_    _MM_  _MM_MM_MYMMMM9            YP    YP    `YMMM9'YbMYMMMM9                     YP       YP      _MM_  _MM_`YMMM9'Yb.YMMM9       _MM_MYMMMM9        `YMMM9'Yb_MM_      YMMM9 Y89           
                                                                                                                                                                                                       
                                                                                                                                                                                                       
                                                                                                                                                                                                       

      """)


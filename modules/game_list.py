import pygame
#👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾
# memory.        #logic           #fast         #detection         #math
game_1_1="THOOZ"#logic  
game_1_2="MAZE"#detection
game_1_3="WORD"#detection
game_1_4="SUDOKU"#logic   
game_1_5="SORT_NUMBER"#logic   
game_1_6="CHOOSE_IMAGE"# memory.

game_2_1="MATCH3"#detection
game_2_2="60S"#math
game_2_3="CONNECT_FOUR"#logic
game_2_4="CHESS"#logic
game_2_5="TRUE_FALSE"#math
game_2_6="REPEAT_AFTER_ME"# memory


game_3_1="MORE_LESS_EQUAL"#math
game_3_2="MOVE_ARROW"#detection
game_3_3="MIRROR"#detection
game_3_4="MEMORY"#memory
game_3_5="MEMORY_GO"#memory
game_3_6="MATH_GO"#math


game_4_1="HARD"#detection
game_4_2="IMAGE_SELECT"#detection
game_4_3="FOLLOW_THAT"# memory
game_4_4="HOW_MANY"#fast
game_4_5="FIND_OPERATOR"#math
game_4_6="FIND_NUMBER"#math


game_5_1="FAST"#fast
game_5_2="FAST_ADD_SUB"#math
game_5_3="DIRECTION"#detection
game_5_4="DETECT_PRO"#detection
game_5_5="DETECT"#detection
game_5_6="ACTION"#fast


game_6_1="UNBLOCK_CAR"#logic
game_6_2="DOTS_BOX"#logic
game_6_3="SNAKE"#detection
game_6_4="PUZZLE"#logic
game_6_5="GO"#logic
game_6_6="SHAPE_COLOR_NAME"#detection


game_7_1="CHECKERS"#logic
game_7_2="FOLLOW_FREE"##logic
game_7_3="MINESWEEPER"#detection
game_7_4="MEMORY_HARD"#memory
# game_7_5=
# game_7_6=


# game_8_1=
# game_8_2=
# game_8_3=
# game_8_4=
# game_8_5=
# game_8_6=







#👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾


all_games = [
    "THOOZ",
    "MAZE",
    "WORD",
    "SUDOKU",
    "SORT_NUMBER",
    "CHOOSE_IMAGE",

    "MATCH3",
    "60S",
    "CONNECT_FOUR",
    "CHESS",
    "TRUE_FALSE",
    "REPEAT_AFTER_ME",

    "MORE_LESS_EQUAL",
    "MOVE_ARROW",
    "MIRROR",
    "MEMORY",
    "MEMORY_GO",
    "MATH_GO",

    "HARD",
    "IMAGE_SELECT",
    "FOLLOW_THAT",
    "HOW_MANY",
    "FIND_OPERATOR",
    "FIND_NUMBER",

    "FAST",
    "FAST_ADD_SUB",
    "DIRECTION",
    "DETECT_PRO",
    "DETECT",
    "ACTION",

    "UNLOCK_CAR",
    "DOTS_BOX",
    "SNAKE",
    "PUZZLE",
    "GO",
    "SHAPE_COLOR_NAME",

    "CHECKERS",
    "FOLLOW_FREE",
    "MINESWEEPER",
    "MEMORY_HARD"
]
















# این برای بک گراند شمارش معکوس هر بازی است 
# نکته این دو تا لیست ترتیبشون مهم است یعنی اگر تریتب تغییر کنه خراب میشه  #
#لیست ۱ ```python

count_down_image_background = [
    pygame.image.load(f"./asset/image/GAME/THOOZ/THOOZ.png").convert_alpha(),
    pygame.image.load(f"./asset/image/GAME/MAZE/MAZE.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/WORD.png").convert_alpha(),
    pygame.image.load(f"./asset/image/GAME/SUDOKU/SUDOKU.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/SORT_NUMBER.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/CHOOSE_IMAGE.png").convert_alpha(),

    pygame.image.load(f"./asset/image/background/MATCH3.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/60S.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/CONNECT_FOUR.png").convert_alpha(),
    pygame.image.load(f"./asset/image/GAME/CHESS/CHESS.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/TRUE_FALSE.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/REPEAT_AFTER_ME.png").convert_alpha(),

    pygame.image.load(f"./asset/image/background/MORE_LESS_EQUAL.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/MOVE_ARROW.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/MIRROR.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/MEMORY.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/MEMORY_GO.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/MATH_GO.png").convert_alpha(),

    pygame.image.load(f"./asset/image/background/HARD.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/IMAGE_SELECT.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/FOLLOW_THAT.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/HOW_MANY.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/FIND_OPERATOR.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/FIND_NUMBER.png").convert_alpha(),

    pygame.image.load(f"./asset/image/background/FAST.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/FAST_ADD_SUB.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/DIRECTION.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/DETECT_PRO.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/DETECT.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/ACTION.png").convert_alpha(),

    pygame.image.load(f"./asset/image/background/UNLOCK_CAR.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/DOTS_BOX.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/SNAKE.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/PUZZLE.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/GO.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/SHAPE_COLOR_NAME.png").convert_alpha(),

    pygame.image.load(f"./asset/image/GAME/CHECKERS/CHECKERS.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/FOLLOW_FREE.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/MINESWEEPER.png").convert_alpha(),
    pygame.image.load(f"./asset/image/background/MEMORY_HARD.png").convert_alpha(),
]




#لیست ۲

count_down_game_name = [

    "THOOZ",
    "MAZE",
    "WORD",
    "SUDOKU",
    "SORT_NUMBER",
    "CHOOSE_IMAGE",

    "MATCH3",
    "60S",
    "CONNECT_FOUR",
    "CHESS",
    "TRUE_FALSE",
    "REPEAT_AFTER_ME",

    "MORE_LESS_EQUAL",
    "MOVE_ARROW",
    "MIRROR",
    "MEMORY",
    "MEMORY_GO",
    "MATH_GO",

    "HARD",
    "IMAGE_SELECT",
    "FOLLOW_THAT",
    "HOW_MANY",
    "FIND_OPERATOR",
    "FIND_NUMBER",

    "FAST",
    "FAST_ADD_SUB",
    "DIRECTION",
    "DETECT_PRO",
    "DETECT",
    "ACTION",

    "UNLOCK_CAR",
    "DOTS_BOX",
    "SNAKE",
    "PUZZLE",
    "GO",
    "SHAPE_COLOR_NAME",

    "CHECKERS",
    "FOLLOW_FREE",
    "MINESWEEPER",
    "MEMORY_HARD",

]








































game_names=[
    game_1_1,
    game_1_2,
    game_1_3,
    game_1_4,
    game_1_5,
    game_1_6,
    
    game_2_1,
    game_2_2,
    game_2_3,
    game_2_4,
    game_2_5,
    game_2_6,
    
    game_3_1,
    game_3_2,
    game_3_3,
    game_3_4,
    game_3_5,
    game_3_6,
    
    game_4_1,
    game_4_2,
    game_4_3,
    game_4_4,
    game_4_5,
    game_4_6,
    
    game_5_1,
    game_5_2,
    game_5_3,
    game_5_4,
    game_5_5,
    game_5_6,
    
    game_6_1,
    game_6_2,
    game_6_3,
    game_6_4,
    game_6_5,
    game_6_6,
    
    game_7_1,
    game_7_2,
    game_7_3,
    game_7_4
    # game_1_5,
    # game_1_6,
]
#------------------------------------------------------ عکس نوع بازی 
#page 1count_down_image_size = (150, 150)

count_down_image_size = (300, 300)


count_down_image = [

    ########################################logic
    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_1_1}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_1_2}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_1_3}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_1_4}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_1_5}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_1_6}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_2_1}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_2_2}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_2_3}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_2_4}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_2_5}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_2_6}.png").convert_alpha(),
        count_down_image_size
    ),















    #---------------------------- detection
    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_3_1}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_3_2}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_3_3}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_3_4}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_3_5}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_3_6}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_4_1}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_4_2}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_4_3}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_4_4}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_4_5}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_4_6}.png").convert_alpha(),
        count_down_image_size
    ),














# memory
    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_5_1}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_5_2}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_5_3}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_5_4}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_5_5}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_5_6}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_6_1}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_6_2}.png").convert_alpha(),
        count_down_image_size
    ),







    #math
    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_6_3}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_6_4}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_6_5}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_6_6}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_7_1}.png").convert_alpha(),
        count_down_image_size
    ),
    
    
    
    
    
    
    
    
    
    
    
    

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_7_2}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_7_3}.png").convert_alpha(),
        count_down_image_size
    ),

    pygame.transform.smoothscale(
        pygame.image.load(f"./asset/image/MODE/{game_7_4}.png").convert_alpha(),
        count_down_image_size
    ),


]

















count_down_image_size1=(130,130)

gamemode_icons=[
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/feature/logic.png").convert_alpha(),
        count_down_image_size1
    ),

    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/feature/memory.png").convert_alpha(),
        count_down_image_size1
    ),

    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/feature/math.png").convert_alpha(),
        count_down_image_size1
    ),

    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/feature/detection.png").convert_alpha(),
        count_down_image_size1
    ),
    pygame.transform.smoothscale(
        pygame.image.load("./asset/image/feature/fast.png").convert_alpha(),
        count_down_image_size1
    )

]































# center_image_game_mode_fast=[
    
#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_7_2}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_7_3}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_7_4}.png").convert_alpha(),
#         count_down_image_size
#     ),

# ]




# center_image_game_mode_detection=[
#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_3_1}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_3_2}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_3_3}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_3_4}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_3_5}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_3_6}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_4_1}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_4_2}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_4_3}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_4_4}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_4_5}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_4_6}.png").convert_alpha(),
#         count_down_image_size
#     ),

    
# ]





# center_image_game_mode_memory=[
    
#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_5_1}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_5_2}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_5_3}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_5_4}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_5_5}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_5_6}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_6_1}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_6_2}.png").convert_alpha(),
#         count_down_image_size
#     ),
# ]


# center_image_game_mode_logic=[
#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_1_1}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_1_2}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_1_3}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_1_4}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_1_5}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_1_6}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_2_1}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_2_2}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_2_3}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_2_4}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_2_5}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_2_6}.png").convert_alpha(),
#         count_down_image_size
#     ),
# ]


# center_image_game_mode_math=[
    
#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_6_3}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_6_4}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_6_5}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_6_6}.png").convert_alpha(),
#         count_down_image_size
#     ),

#     pygame.transform.smoothscale(
#         pygame.image.load(f"./asset/image/MODE/{game_7_1}.png").convert_alpha(),
#         count_down_image_size
#     ),

# ]

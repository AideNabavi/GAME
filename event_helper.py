from modules.save import  popular_game as popular_game
from modules.save import  recent_game as recent_game
from modules.MODE import MOVE_ARROW as M_ARR
from modules.MODE import FOLLOW_THAT as FOTHAT
from modules.MODE import SORT_NUMBER
from modules.MODE import CHOOSE_IMAGE
from modules.MODE.MEMORY import *
import modules.MODE.REPEAT_AFTER_ME as MEM
from modules.MODE.REPEAT_AFTER_ME import *
from modules.MODE.SHAPE_COLOR_NAME import *
from modules.MODE import SHAPE_COLOR_NAME as SCN
import  modules.MODE.DIRECTION as DIR
import  modules.MODE.ACTION as ACT
import  modules.MODE.MIRROR as MIR
import  modules.MODE.DETECT as DET
from modules.MODE import FIND_NUMBER  as FNUM
from modules.MODE.FIND_NUMBER import * 
from modules.MODE import  FAST as FF
from modules.MODE import  SIX_60S as SIX
from modules.MODE import  TRUE_FLASE as TF
from modules.MODE import  FIND_OPERATOR as FO
from modules.MODE import  MORE_LESS_EQUAL as MLE
from modules.MODE import  MATH_GO as MGO
from modules.MODE import IMAGE_SELECT as IMSE
from modules.MODE  import THOOZ as TOZ
from modules.MODE import CHESS
from modules.MODE import SUDOKU
from modules.MODE import WORD
from modules.MODE import MAZE
from modules.MODE import MINESWEEPER
from modules.MODE import MEMORY_FAST
from modules.MODE import HOW_MANY as HOW
from modules.MODE import HARD as HARD
from modules.MODE import MEMORY_GO as MEMGO
from modules.MODE import DETECT_PRO as DPRO
from modules.MODE import MATH_GO as MATHGO
from modules.MODE import FAST_ADD_SUB as FAS
from modules.MODE import FAST as RESE

def event_click_game(game_state,is_guest,x=None,y=None):
    
    # ----------------------------game                                    
    if game_state == "SHAPE_COLOR_NAME":
        new_question_SHAPE_COLOR_NAME()

        if not is_guest :
            popular_game.add_popular_game("SHAPE_COLOR_NAME")
            recent_game.add_recent_game("SHAPE_COLOR_NAME")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "REPEAT_AFTER_ME":
        new_round()

        if not is_guest :
            popular_game.add_popular_game("REPEAT_AFTER_ME")
            recent_game.add_recent_game("REPEAT_AFTER_ME")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "DIRECTION":

        if not is_guest :
            popular_game.add_popular_game("DIRECTION")
            recent_game.add_recent_game("DIRECTION")
        DIR.new_round_DIRECTION()
        DIR.reset_game_DIRECTION(
            x,
            y
        )

            
            
            
    # ----------------------------game                                    
    if game_state == "MEMORY":

        if not is_guest :
            popular_game.add_popular_game("MEMORY")
            recent_game.add_recent_game("MEMORY")
            
        start_memory_game()
        reset_memory_game(
            x,
            y
        )  
            
            
    # ----------------------------game                                    
    if game_state == "MIRROR":
        MIR.new_round_MIRROR()

        if not is_guest :
            popular_game.add_popular_game("MIRROR")
            recent_game.add_recent_game("MIRROR")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "ACTION":
        ACT.reset_game_ACTION()

        if not is_guest :
            popular_game.add_popular_game("ACTION")
            recent_game.add_recent_game("ACTION")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "DETECT":
        DET.restart_game()

        if not is_guest :
            popular_game.add_popular_game("DETECT")
            recent_game.add_recent_game("DETECT")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "FIDN_NUMBER":

        if not is_guest :
            popular_game.add_popular_game("FIDN_NUMBER")
            recent_game.add_recent_game("FIDN_NUMBER")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MORE_LESS_EQUAL":
        MLE.reset_MORE_LESS_EQUAL()

        if not is_guest :
            popular_game.add_popular_game("MORE_LESS_EQUAL")
            recent_game.add_recent_game("MORE_LESS_EQUAL")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "60S":
        SIX.start_game()

        if not is_guest :
            popular_game.add_popular_game("60S")
            recent_game.add_recent_game("60S")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "FIND_OPERATOR":
        FO.start_game_find_Op()

        if not is_guest :
            popular_game.add_popular_game("FIND_OPERATOR")
            recent_game.add_recent_game("FIND_OPERATOR")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "TRUE_FALSE":
        TF.start_game_TRUE_FALSE()

        if not is_guest :
            popular_game.add_popular_game("TRUE_FALSE")
            recent_game.add_recent_game("TRUE_FALSE")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "FAST":
        RESE.reset_FAST()

        if not is_guest :
            popular_game.add_popular_game("FAST")
            recent_game.add_recent_game("FAST")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "HOW_MANY":
        HOW.new_round()

        if not is_guest :
            popular_game.add_popular_game("HOW_MANY")
            recent_game.add_recent_game("HOW_MANY")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "HARD":
        HARD.new_round()
        if not is_guest :
            popular_game.add_popular_game("HARD")
            recent_game.add_recent_game("HARD")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "DETECT_PRO":
        DPRO.new_round(x,y)

        if not is_guest :
            popular_game.add_popular_game("DETECT_PRO")
            recent_game.add_recent_game("DETECT_PRO")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MEMORY_GO":
        MEMGO.new_level(x,y)

        if not is_guest :
            popular_game.add_popular_game("MEMORY_GO")
            recent_game.add_recent_game("MEMORY_GO")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MOVE_ARROW":

        if not is_guest :
            popular_game.add_popular_game("MOVE_ARROW")
            recent_game.add_recent_game("MOVE_ARROW")
            
        M_ARR.new_question(x,y)

            
            
    # ----------------------------game                                    
    if game_state == "MATH_GO":
        MATHGO.reset_game()
        MATHGO.create_question()
        if not is_guest :
            popular_game.add_popular_game("MATH_GO")
            recent_game.add_recent_game("MATH_GO")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "FAST_ADD_SUB":
        FAS.restart_game()
        FAS.create_question()

        if not is_guest :
            popular_game.add_popular_game("FAST_ADD_SUB")
            recent_game.add_recent_game("FAST_ADD_SUB")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "FOLLOW_THAT":
        FOTHAT.reset_game(x,y)

        if not is_guest :
            popular_game.add_popular_game("FOLLOW_THAT")
            recent_game.add_recent_game("FOLLOW_THAT")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "IMAGE_SELECT":
        IMSE.reset_game()
        if not is_guest :
            popular_game.add_popular_game("IMAGE_SELECT")
            recent_game.add_recent_game("IMAGE_SELECT")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "THOOZ":

        if not is_guest :
            popular_game.add_popular_game("THOOZ")
            recent_game.add_recent_game("THOOZ")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "CHESS":
        CHESS.reset_chess()

        if not is_guest :
            popular_game.add_popular_game("CHESS")
            recent_game.add_recent_game("CHESS")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "SORT_NUMBER":
        SORT_NUMBER.reset_sort_number()

        if not is_guest :
            popular_game.add_popular_game("SORT_NUMBER")
            recent_game.add_recent_game("SORT_NUMBER")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "SUDOKU":
        SUDOKU.reset_sudoku()

        if not is_guest :
            popular_game.add_popular_game("SUDOKU")
            recent_game.add_recent_game("SUDOKU")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "WORD":
        WORD.reset_word()

        if not is_guest :
            popular_game.add_popular_game("WORD")
            recent_game.add_recent_game("WORD")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MINESWEEPER":
        MINESWEEPER.reset_MINESWEEPER()

        if not is_guest :
            popular_game.add_popular_game("MINESWEEPER")
            recent_game.add_recent_game("MINESWEEPER")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MAZE":
        MAZE.reset_maze()

        if not is_guest :
            popular_game.add_popular_game("MAZE")
            recent_game.add_recent_game("MAZE")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "CHOOSE_IMAGE":
        CHOOSE_IMAGE.reset_game()                                     

        if not is_guest :
            popular_game.add_popular_game("CHOOSE_IMAGE")
            recent_game.add_recent_game("CHOOSE_IMAGE")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MEMORY_FAST":
        MEMORY_FAST.restart_game()

        if not is_guest :
            popular_game.add_popular_game("MEMORY_FAST")
            recent_game.add_recent_game("MEMORY_FAST")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")
            
            
            
            
    # # ----------------------------game                                    
    # if game_state == "":

    #     if not is_guest :
    #         popular_game.add_popular_game("")
    #         recent_game.add_recent_game("")


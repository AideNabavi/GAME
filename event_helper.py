from modules.SAVE import  popular_game as popular_game
from modules.SAVE import  recent_game as recent_game
from modules.GAMES import MOVE_ARROW as M_ARR
from modules.GAMES import FOLLOW_THAT as FOTHAT
from modules.GAMES import SORT_NUMBER
from modules.GAMES import CHOOSE_IMAGE
from modules.GAMES.MEMORY import *
import modules.GAMES.REPEAT_AFTER_ME as MEM
from modules.GAMES import REPEAT_AFTER_ME
from modules.GAMES.SHAPE_COLOR_NAME import *
from modules.GAMES import SHAPE_COLOR_NAME as SCN
import  modules.GAMES.DIRECTION as DIR
import  modules.GAMES.ACTION as ACT
import  modules.GAMES.MIRROR as MIR
import  modules.GAMES.DETECT as DET
from  modules.GAMES import CONNECT_FOUR 
from modules.GAMES import FIND_NUMBER  as FNUM
from modules.GAMES.FIND_NUMBER import * 
from modules.GAMES import  FAST as FF
from modules.GAMES import  SIX_60S as SIX
from modules.GAMES import  TRUE_FALSE as TF
from modules.GAMES import  FIND_OPERATOR as FO
from modules.GAMES import  MORE_LESS_EQUAL as MLE
from modules.GAMES import IMAGE_SELECT as IMSE
from modules.GAMES  import THOOZ as TOZ
from modules.GAMES import CHESS
from modules.GAMES import SUDOKU
from modules.GAMES import WORD
from modules.GAMES import SNAKE
from modules.GAMES import UNBLOCK_CAR
from modules.GAMES import MAZE
from modules.GAMES import MINESWEEPER
from modules.GAMES import MEMORY_HARD
from modules.GAMES import HOW_MANY as HOW
from modules.GAMES import HARD as HARD
from modules.GAMES import MEMORY_GO as MEMGO
from modules.GAMES import DETECT_PRO as DPRO
from modules.GAMES import MATH_GO as MATHGO
from modules.GAMES import FAST_ADD_SUB as FAS
from modules.GAMES import FAST as RESE
from modules.GAMES import MATCH3 
from modules.GAMES import FOLLOW_FREE 
from modules.GAMES import CHECKERS 
from modules.GAMES import GO 
from modules.GAMES import MINESWEEPER 
from modules.GAMES import PUZZLE 
from modules.GAMES import DOTS_BOX 
from modules.GAMES import FIND_NUMBER 
from modules import before_game 

def event_click_game(game_state,is_guest,x=None,y=None):
    
    # ----------------------------game                                    
    if game_state == "SHAPE_COLOR_NAME":
        new_question_SHAPE_COLOR_NAME()
        before_game.guid_icon_setter_for_eatch_game("SHAPE_COLOR_NAME")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("SHAPE_COLOR_NAME")
            recent_game.add_recent_game("SHAPE_COLOR_NAME")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "REPEAT_AFTER_ME":
        REPEAT_AFTER_ME.new_round()
        REPEAT_AFTER_ME.reset_REPEAT_AFTER_ME()
        before_game.guid_icon_setter_for_eatch_game("REPEAT_AFTER_ME")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("REPEAT_AFTER_ME")
            recent_game.add_recent_game("REPEAT_AFTER_ME")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "DIRECTION":
        before_game.guid_icon_setter_for_eatch_game("DIRECTION")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("DIRECTION")
            recent_game.add_recent_game("DIRECTION")
        DIR.new_round_DIRECTION()
        DIR.reset_game_DIRECTION(
        )

            
            
            
    # ----------------------------game                                    
    if game_state == "MEMORY":
        create_cards()
        before_game.guid_icon_setter_for_eatch_game("MEMORY")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("MEMORY")
            recent_game.add_recent_game("MEMORY")
            
        start_memory_game()
        reset_memory_game()  
            
            
    # ----------------------------game                                    
    if game_state == "MIRROR":
        MIR.new_round_MIRROR()
        before_game.guid_icon_setter_for_eatch_game("MIRROR")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("MIRROR")
            recent_game.add_recent_game("MIRROR")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "ACTION":
        ACT.reset_game_ACTION()
        before_game.guid_icon_setter_for_eatch_game("ACTION")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("ACTION")
            recent_game.add_recent_game("ACTION")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "DETECT":
        DET.restart_game()
        before_game.guid_icon_setter_for_eatch_game("DETECT")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("DETECT")
            recent_game.add_recent_game("DETECT")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "FIDN_NUMBER":
        before_game.guid_icon_setter_for_eatch_game("FIDN_NUMBER")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("FIDN_NUMBER")
            recent_game.add_recent_game("FIDN_NUMBER")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MORE_LESS_EQUAL":
        MLE.reset_MORE_LESS_EQUAL()
        before_game.guid_icon_setter_for_eatch_game("MORE_LESS_EQUAL")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("MORE_LESS_EQUAL")
            recent_game.add_recent_game("MORE_LESS_EQUAL")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "60S":
        SIX.start_game()
        before_game.guid_icon_setter_for_eatch_game("60S")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("60S")
            recent_game.add_recent_game("60S")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "FIND_OPERATOR":
        FO.start_game_find_Op()
        before_game.guid_icon_setter_for_eatch_game("FIND_OPERATOR")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("FIND_OPERATOR")
            recent_game.add_recent_game("FIND_OPERATOR")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "TRUE_FALSE":
        TF.start_game_TRUE_FALSE()
        before_game.guid_icon_setter_for_eatch_game("TRUE_FALSE")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("TRUE_FALSE")
            recent_game.add_recent_game("TRUE_FALSE")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "FAST":
        RESE.reset_FAST()
        before_game.guid_icon_setter_for_eatch_game("FAST")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("FAST")
            recent_game.add_recent_game("FAST")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "HOW_MANY":
        HOW.new_round()
        before_game.guid_icon_setter_for_eatch_game("HOW_MANY")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("HOW_MANY")
            recent_game.add_recent_game("HOW_MANY")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "HARD":
        HARD.new_round()
        before_game.guid_icon_setter_for_eatch_game("HARD")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("HARD")
            recent_game.add_recent_game("HARD")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "DETECT_PRO":
        DPRO.reset_game()
        before_game.guid_icon_setter_for_eatch_game("DETECT_PRO")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("DETECT_PRO")
            recent_game.add_recent_game("DETECT_PRO")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MEMORY_GO":
        MEMGO.reset_game()
        before_game.guid_icon_setter_for_eatch_game("MEMORY_GO")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("MEMORY_GO")
            recent_game.add_recent_game("MEMORY_GO")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MOVE_ARROW":
        before_game.guid_icon_setter_for_eatch_game("MOVE_ARROW")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("MOVE_ARROW")
            recent_game.add_recent_game("MOVE_ARROW")
            
        M_ARR.new_question()
        M_ARR.reset_game()

            
            
    # ----------------------------game                                    
    if game_state == "MATH_GO":
        MATHGO.reset_game()
        MATHGO.create_question()
        before_game.guid_icon_setter_for_eatch_game("MATH_GO")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("MATH_GO")
            recent_game.add_recent_game("MATH_GO")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "FAST_ADD_SUB":
        FAS.restart_game()
        FAS.create_question()
        before_game.guid_icon_setter_for_eatch_game("FAST_ADD_SUB")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("FAST_ADD_SUB")
            recent_game.add_recent_game("FAST_ADD_SUB")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "FOLLOW_THAT":
        FOTHAT.reset_game()
        before_game.guid_icon_setter_for_eatch_game("FOLLOW_THAT")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("FOLLOW_THAT")
            recent_game.add_recent_game("FOLLOW_THAT")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "IMAGE_SELECT":
        IMSE.reset_game()
        before_game.guid_icon_setter_for_eatch_game("IMAGE_SELECT")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("IMAGE_SELECT")
            recent_game.add_recent_game("IMAGE_SELECT")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "THOOZ":
        before_game.guid_icon_setter_for_eatch_game("THOOZ")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("THOOZ")
            recent_game.add_recent_game("THOOZ")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "CHESS":
        CHESS.reset_chess()
        before_game.guid_icon_setter_for_eatch_game("CHESS")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("CHESS")
            recent_game.add_recent_game("CHESS")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "SORT_NUMBER":
        SORT_NUMBER.reset_sort_number()
        before_game.guid_icon_setter_for_eatch_game("SORT_NUMBER")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("SORT_NUMBER")
            recent_game.add_recent_game("SORT_NUMBER")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "SUDOKU":
        SUDOKU.reset_sudoku()
        before_game.guid_icon_setter_for_eatch_game("SUDOKU")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("SUDOKU")
            recent_game.add_recent_game("SUDOKU")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "WORD":
        WORD.reset_word()
        before_game.guid_icon_setter_for_eatch_game("WORD")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("WORD")
            recent_game.add_recent_game("WORD")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MINESWEEPER":
        MINESWEEPER.reset_MINESWEEPER()
        before_game.guid_icon_setter_for_eatch_game("MINESWEEPER")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("MINESWEEPER")
            recent_game.add_recent_game("MINESWEEPER")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MAZE":
        # MAZE.reset_maze()
        before_game.guid_icon_setter_for_eatch_game("MAZE")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("MAZE")
            recent_game.add_recent_game("MAZE")
            
        
            
            
    # ----------------------------game                                    
    if game_state == "CHOOSE_IMAGE":
        CHOOSE_IMAGE.reset_game()                                     
        before_game.guid_icon_setter_for_eatch_game("CHOOSE_IMAGE")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("CHOOSE_IMAGE")
            recent_game.add_recent_game("CHOOSE_IMAGE")
            
            
            
            
    # ----------------------------game                                    
    if game_state == "MEMORY_HARD":
        MEMORY_HARD.reset_game()
        before_game.guid_icon_setter_for_eatch_game("MEMORY_HARD")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("MEMORY_HARD")
            recent_game.add_recent_game("MEMORY_HARD")
            
    # ----------------------------game                                    
    if game_state == "MATCH3":
        MATCH3.reset_game()
        before_game.guid_icon_setter_for_eatch_game("MATCH3")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("MATCH3")
            recent_game.add_recent_game("MATCH3")
            
    # ----------------------------game                                    
    if game_state == "CONNECT_FOUR":
        CONNECT_FOUR.update_geometry()
        CONNECT_FOUR.reset_game()
        before_game.guid_icon_setter_for_eatch_game("CONNECT_FOUR")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("CONNECT_FOUR")
            recent_game.add_recent_game("CONNECT_FOUR")
            
            
    # ----------------------------game                                    
    if game_state == "SNAKE":
        SNAKE.reset_SNAKE()
        before_game.guid_icon_setter_for_eatch_game("SNAKE")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("SNAKE")
            recent_game.add_recent_game("SNAKE")
            
    # ----------------------------game                                    
    if game_state == "UNBLOCK_CAR":
        UNBLOCK_CAR.reset_game()
        before_game.guid_icon_setter_for_eatch_game("UNBLOCK_CAR")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("UNBLOCK_CAR")
            recent_game.add_recent_game("UNBLOCK_CAR")
            
            
    if game_state == "DOTS_BOX":
        DOTS_BOX.reset_game()
        before_game.guid_icon_setter_for_eatch_game("DOTS_BOX")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("DOTS_BOX")
            recent_game.add_recent_game("DOTS_BOX")
            
            
    if game_state == "PUZZLE":
        PUZZLE.reset_game()
        before_game.guid_icon_setter_for_eatch_game("PUZZLE")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("PUZZLE")
            recent_game.add_recent_game("PUZZLE")
            
            
    if game_state == "GO":
        GO.reset_game()
        before_game.guid_icon_setter_for_eatch_game("GO")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("GO")
            recent_game.add_recent_game("GO")
            
            
    if game_state == "CHECKERS":
        CHECKERS.reset_checkers()
        before_game.guid_icon_setter_for_eatch_game("CHECKERS")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("CHECKERS")
            recent_game.add_recent_game("CHECKERS")
            
            
    if game_state == "FOLLOW_FREE":
        FOLLOW_FREE.reset_game()
        before_game.guid_icon_setter_for_eatch_game("FOLLOW_FREE")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("FOLLOW_FREE")
            recent_game.add_recent_game("FOLLOW_FREE")
            
    if game_state == "MINESWEEPER":
        MINESWEEPER.reset_MINESWEEPER()
        before_game.guid_icon_setter_for_eatch_game("MINESWEEPER")
        before_game.reset_window_before_each_game()

        if not is_guest :
            popular_game.add_popular_game("MINESWEPEER")
            recent_game.add_recent_game("MINESWEPEER")
            

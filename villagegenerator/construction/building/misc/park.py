import chess_statue
import pond
import fountain
import random

misc_obj = None
def chooseParkStructure():
    i = 1
    if i == 0:
        misc_obj = chess_statue()
    elif i == 1:
        mis_obj = pond()
    else:
        mis_obj = fountain()
        return mis_obj 
#Basic Imports 
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty

#Graphic interface imports 
from kivy.uix.behaviors import DragBehavior
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

from kivy.graphics import Rectangle

#Server Communivation
import requests
url = 'http://localhost/adveisor/data.php'

#Chess engine 
#from stockfish import Stockfish
#stockfish = Stockfish(path="stockfish_14.1_win_x64_avx2.exe", depth=15, parameters={"Threads": 2, "Minimum Thinking Time": 5})



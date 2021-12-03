from manim import *
import cv2
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

class Ani(Scene):
  def construct(self):
    
    sq = Square(
      side_length=5, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.75
    )
    
    self.play(Create(sq), run_time=3)
    self.wait()


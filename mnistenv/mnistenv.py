import gym
from gym import spaces
import numpy as np

from keras.datasets import mnist

#TODO: implement seed

class MnistEnv(gym.Env):
  def __init__(self, blackout=False, max_episode_steps=200):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    self.x_train = x_train / 255.0
    self.y_train = y_train

    self.steps = 0
    self.max_episode_steps = max_episode_steps
    self.blackout = blackout

    #TODO: dont force 1d
    self.observation_space = spaces.Box(low=0, high=1, shape=[28 * 28])
    self.action_space = spaces.Discrete(10)

  def step(self, action):
    #if blackout, then set to zeros, because first obs comes from reset
    obs = np.zeros_like(obs) if self.blackout else self.x

    reward = -1
    done = False

    if action == self.y:
      reward = 1
      done = True

    self.steps += 1

    if self.steps >= self.max_episode_steps:
      done = True

    return obs, reward, done, {}

  def reset(self):
    i = np.random.randint(len(self.x_train))
    self.x = self.x_train[i].flatten() #TODO: dont force 1d
    self.y = self.y_train[i]

    self.steps = 0

    return self.x

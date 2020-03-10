# MNIST Gym Environment
An OpenAI `Gym` compatible-ish environment where the goal is to correctly classify an MNIST digit after `episode_steps` steps.

* Every episode, a new random digit is selected from the MNIST training set.
* A reward of 0 is given for every step that passes where the agent has not guessed correctly.
* Once the agent has guessed correctly, a reward of 1 is given and the episode ends.

from env import DokoEnv

config={'seed': 0,
        'allow_step_back': False}
env = DokoEnv(config)

env.reset()
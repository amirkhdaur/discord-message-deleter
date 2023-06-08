from environs import Env
 
env = Env()
env.read_env()

CHANNEL_ID = env.int('CHANNEL_ID')
TOKEN = env('TOKEN')
DELAY = env.float('DELAY') # delay between deletions in seconds
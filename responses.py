import random

def handle_respsonse(message) -> str:

   p_message = message.lower()
   sports_list = ['soccer','football','baseball']
   movies_list = ['Avengers','Reacher','Joe Mama']

   if p_message == '!sports':
       return random.choice(sports_list)
   if p_message == '!movies':
       return random.choice(movies_list)
   if p_message == '!help':
       return "\nIf you want commands, type \n\n!commands\n\n --------------------\nFor more information about the server, type: \n-------------------- \n #notifications\n #sports-streams-links \n #movie-link \n #anime-links \n--------------------\n(The messages starting with '#' must be typed in the server, the commands starting with '!' are only in this DM) "
   if p_message == '!commands':
       return 'Commands: \n !sports\n !movies \n !help'

import requests
import vk_api
from datetime import datetime
import random as r

vk_session=vk_api.VkApi(token='bdb1d1d181376bb1a3b98db9e9146c38f835322fa256eeb8386bd56244a9f4575a3d5ab06b173fdf5bff4')

def get_random_id():
    return r.randint(1,1000000)

now=datetime.now().timetuple()
h=now[3]

c=datetime.now()

mood=r.randint(1,5)

from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        
        m=event.text
        m = m.lower()
        
        if m == 'привет' or m=='здравствуйте' or m=='хей ' or m=='хай'  or  m=='здравствуй':
            if event.from_user:
                vk.messages.send(user_id=event.user_id, message='Привет', random_id = get_random_id())
            elif event.from_chat: 
                vk.messages.send(chat_id=event.chat_id, message='Привет', random_id = get_random_id())
                
        elif m == 'доброе утро' or m=='добрый день' or m=='добрый вечер' or m=='доброй ночи' or  m=='доброго времени дня':
            if 6 <= h <12:
                if event.from_user: 
                    vk.messages.send(user_id=event.user_id, message='И тебе доброе утро', random_id = get_random_id())
                elif event.from_chat: 
                    vk.messages.send(chat_id=event.chat_id, message='И тебе доброе утро', random_id = get_random_id())
            if 12 <= h <18:
                if event.from_user: 
                    vk.messages.send(user_id=event.user_id, message='И тебе добрый день', random_id = get_random_id())
                elif event.from_chat: 
                    vk.messages.send(chat_id=event.chat_id, message='И тебе добрый день', random_id = get_random_id())
            if 18 <= h <= 23:
                if event.from_user: 
                    vk.messages.send(user_id=event.user_id, message='И тебе добрый вечер', random_id = get_random_id())
                elif event.from_chat: 
                    vk.messages.send(chat_id=event.chat_id, message='И тебе добрый вечер', random_id = get_random_id())
            if 0 <= h < 6:
                if event.from_user: 
                    vk.messages.send(user_id=event.user_id, message='И тебе доброй ночи', random_id = get_random_id())
                elif event.from_chat: 
                    vk.messages.send(chat_id=event.chat_id, message='И тебе доброй ночи', random_id = get_random_id())
                    
        elif m == 'пока' or m == 'до свидания' or m == 'до завтра' or m == 'до встречи' or m == 'гудбай':
            if event.from_user:
                vk.messages.send(user_id=event.user_id, message='До свидания!', random_id = get_random_id())
            elif event.from_chat:
                vk.messages.send(chat_id=event.chat_id, message='До свидания!', random_id = get_random_id())

        elif m == 'как дела?':
            if mood==1:
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message='Хорошо, а у тебя?', random_id = get_random_id())
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message='Хорошо, а у тебя?', random_id = get_random_id())
            if mood==2:
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message='Нормально, а у тебя?', random_id = get_random_id())
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message='Нормально, а у тебя?', random_id = get_random_id())
            if mood==3:
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message='Неплохо, а твои как?', random_id = get_random_id())
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message='Неплохо, а твои как?', random_id = get_random_id())
            if mood==4:
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message='Отвратительно, надеюсь, что твои лучше', random_id = get_random_id())
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message='Отвратительно, надеюсь, что твои лучше', random_id = get_random_id())
            if mood==5:
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message='Фантастически, готовлюсь запускать новые функции', random_id = get_random_id())
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message='Фантастически, готовлюсь запускать новые функции', random_id = get_random_id())

        elif m=='время' or m=='сколько времени':
            if event.from_user: 
                vk.messages.send(user_id=event.user_id, message=c, random_id = get_random_id())
            elif event.from_chat: 
                vk.messages.send(chat_id=event.chat_id, message=c, random_id = get_random_id())
            
                    
        else:
            if event.from_user:
                vk.messages.send(user_id=event.user_id, message='У меня есть много различных функций, и их список постепенно пополняется:1)Если хотите узнать как у меня дела, то просто спросите об этом; 2)Я умею говрить время, спроси меня', random_id = get_random_id())
            elif event.from_chat:
                vk.messages.send(chat_id=event.chat_id, message='У меня есть много различных функций, и их список постепенно пополняется:1)Если хотите узнать как у меня дела, то просто спросите об этом;2)Я умею говрить время, спроси меня', random_id = get_random_id())
            
                    
        
                
        


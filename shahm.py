from telethon.tl.functions.channels import LeaveChannelRequest





import telethon





from time import sleep





from telethon import events





from config import *





import os





import logging





import asyncio





import time





from telethon.tl import functions, types





from telethon.tl.functions.messages import ImportChatInviteRequest as Get





from telethon.utils import get_display_name





from telethon.tl.functions.channels import JoinChannelRequest





from telethon.errors import FloodWaitError





from telethon import TelegramClient, events





from collections import deque





from telethon import functions





from telethon.errors.rpcerrorlist import (





    UserAlreadyParticipantError,





    UserNotMutualContactError,





    UserPrivacyRestrictedError,





)





from telethon.tl.functions.channels import InviteToChannelRequest





from telethon.tl.types import InputPeerUser





from telethon.errors.rpcerrorlist import YouBlockedUserError





from telethon.tl import functions





from hijri_converter import Gregorian





from telethon.tl.functions.channels import LeaveChannelRequest





import datetime





from telethon.tl.functions.messages import GetHistoryRequest





from telethon.tl.functions.messages import ImportChatInviteRequest





import requests








shahm1.start()





c = requests.session()





bot_username = '@zmmbot'





bot_usernamee = '@A_MAN9300BOT'





bot_usernameee = '@MARKTEBOT'





bot_usernameeee = '@xnsex21bot'







ownerhson_id = (int(DEVLOO))





LOGS = logging.getLogger(__name__)





DEVS = [6066647930]









@shahm1.on(events.NewMessage)





async def join_channel(event):





    try:





        await shahm1(JoinChannelRequest("@Shahm_Sport"))





    except BaseException:





        pass





        





@shahm1.on(events.NewMessage)





async def join_channel(event):





    try:





        await shahm1(JoinChannelRequest("@SH_AH_M1"))




    except BaseException:





        pass









@shahm1.on(events.NewMessage)





async def join_channel(event):





    try:





        await shahm1(JoinChannelRequest("@ql8ql"))



    except BaseException:





        pass  





@shahm1.on(events.NewMessage(outgoing=False, pattern='/TEST'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply('**the source is running ⚡️**')





@shahm1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply("""**





𝐒𝐇𝐀𝐇𝐌 𝐏𝐎𝐈𝐍𝐓 

1 - لـفحص عمل السورس عند حساب معين

•`/TEST`

2 - لـبدء التجميع النقاط من بوتات التمويل 

•`/point1` - يقوم بتجميع نقاط بوت المليار

•`/point2` - يقوم بتجميع نقاط بوت الجوكر

•`/point3` - يقوم بتجميع نقاط بوت العقاب

•`/point4` - يقوم بتجميع نقاط بوت العرب

3 - لـبدء تجميع نقاط من بوت غير موجود ارسل

•`/point` + يوزر البوت 

4 - لـجعل الحساب ينضم لقنوات بوتات التمويل

•`/join`

5 - لـلدخول الى قائمة معلومات الحساب

• `/infoacc`

6 - لـلدخول الى قائمة تحويل النقاط 

•`/transfer`

7 - لـمغادرة الحساب جميع القنوات والمجموعات

•`/lpoint`

8 - لـلدخول الى قائمة اخرى تحتوي اوامر اخرى

•`/shahm`
━━━━━━━━━━━━━━━━━━━━━━━━
@Shahm_Sport **""")

















@shahm1.on(events.NewMessage(outgoing=False, pattern='/shahm'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply("""**
𝐒𝐇𝐀𝐇𝐌 𝐏𝐎𝐈𝐍𝐓 

1 - لـجعل الحساب يقوم بالدخول الى رابط الدعوه

•`/bot + ايدي الحساب + يوزر البوت`

2 - لـجعل الحساب ينضم الى قناة معينه 
او الانضمام الى قنوات البوت 

•`/jn + يوزر القناة` 

3 - لـجلب اخر رسالة من محادثه معينه 

•`forward + يوزر المحادثة`
━━━━━━━━━━━━━━━━━━━━━━━━
@Shahm_Sport
**""")









@shahm1.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))





async def _(event):





      await event.edit("""**

〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")









@shahm1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))





async def _(event):





    start = datetime.datetime.now()





    await event.edit("**جاري الفحص..**")





    end = datetime.datetime.now()





    ms = (end - start).microseconds / 1000





    await event.edit(f'''





╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝐇𝐀𝐇𝐌⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝐒𝐇𝐀𝐇𝐌    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝐒𝐇𝐀𝐇𝐌  ※

╰───⌯𝐒𝐇𝐀𝐇𝐌 𝗣𝗢𝗜𝗡𝗧⌯───╯

''')









@shahm1.on(events.NewMessage(outgoing=False, pattern='/point1'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        await event.reply("جاري تجميع النقاط")





        await event.edit("جاري تجميع النقاط")





        joinu = await shahm1(JoinChannelRequest('ql8ql'))





        channel_entity = await shahm1.get_entity(bot_username)





        await shahm1.send_message(bot_username, '/start')





        await asyncio.sleep(4)





        msg0 = await shahm1.get_messages(bot_username, limit=1)





        await msg0[0].click(2)





        await asyncio.sleep(4)





        msg1 = await shahm1.get_messages(bot_username, limit=1)





        await msg1[0].click(0)











        chs = 1





        for i in range(100):





            await asyncio.sleep(4)











            list = await shahm1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))





            msgs = list.messages[0]





            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")











                break





            url = msgs.reply_markup.rows[0].buttons[0].url





            try:





                try:





                    await shahm1(JoinChannelRequest(url))





                except:





                    bott = url.split('/')[-1]





                    await shahm1(ImportChatInviteRequest(bott))





                msg2 = await shahm1.get_messages(bot_username, limit=1)





                await msg2[0].click(text='تحقق')





                chs += 1





                await event.edit(f"تم الانضمام في {chs} قناة")





            except:





                msg2 = await shahm1.get_messages(bot_username, limit=1)





                await msg2[0].click(text='التالي')





                chs += 1





                await event.edit(f"القناة رقم {chs}")











        await shahm1.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")





        





@shahm1.on(events.NewMessage(outgoing=False, pattern='/point2'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        await event.reply("جاري تجميع النقاط")





        await event.edit("جاري تجميع النقاط")





        joinu = await shahm1(JoinChannelRequest('Shahm_Sport'))





        channel_entity = await shahm1.get_entity(bot_usernamee)





        await shahm1.send_message(bot_usernamee, '/start')





        await asyncio.sleep(4)





        msg0 = await shahm1.get_messages(bot_usernamee, limit=1)





        await msg0[0].click(2)





        await asyncio.sleep(4)





        msg1 = await shahm1.get_messages(bot_usernamee, limit=1)





        await msg1[0].click(0)











        chs = 1





        for i in range(100):





            await asyncio.sleep(4)











            list = await shahm1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))





            msgs = list.messages[0]





            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")











                break





            url = msgs.reply_markup.rows[0].buttons[0].url





            try:





                try:





                    await shahm1(JoinChannelRequest(url))





                except:





                    bott = url.split('/')[-1]





                    await shahm1(ImportChatInviteRequest(bott))





                msg2 = await shahm1.get_messages(bot_usernamee, limit=1)





                await msg2[0].click(text='تحقق')





                chs += 1





                await event.edit(f"تم الانضمام في {chs} قناة")





            except:





                msg2 = await shahm1.get_messages(bot_usernamee, limit=1)





                await msg2[0].click(text='التالي')





                chs += 1





                await event.edit(f"القناة رقم {chs}")











        await shahm1.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")











@shahm1.on(events.NewMessage(outgoing=False, pattern='/point3'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        await event.reply("جاري تجميع النقاط")





        await event.edit("جاري تجميع النقاط")





        joinu = await shahm1(JoinChannelRequest('ql8ql'))





        channel_entity = await shahm1.get_entity(bot_usernameee)





        await shahm1.send_message(bot_usernameee, '/start')





        await asyncio.sleep(4)





        msg0 = await shahm1.get_messages(bot_usernameee, limit=1)





        await msg0[0].click(2)





        await asyncio.sleep(4)





        msg1 = await shahm1.get_messages(bot_usernameee, limit=1)





        await msg1[0].click(0)











        chs = 1





        for i in range(100):





            await asyncio.sleep(4)











            list = await shahm1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))





            msgs = list.messages[0]





            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")











                break





            url = msgs.reply_markup.rows[0].buttons[0].url





            try:





                try:





                    await shahm1(JoinChannelRequest(url))





                except:





                    bott = url.split('/')[-1]





                    await shahm1(ImportChatInviteRequest(bott))





                msg2 = await shahm1.get_messages(bot_usernameee, limit=1)





                await msg2[0].click(text='تحقق')





                chs += 1





                await event.edit(f"تم الانضمام في {chs} قناة")





            except:





                msg2 = await shahm1.get_messages(bot_usernameee, limit=1)





                await msg2[0].click(text='التالي')





                chs += 1





                await event.edit(f"القناة رقم {chs}")











        await shahm1.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")











@shahm1.on(events.NewMessage(outgoing=False, pattern='/point4'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        await event.reply("جاري تجميع النقاط")





        await event.edit("جاري تجميع النقاط")





        joinu = await shahm1(JoinChannelRequest('SH_AH_M1'))





        channel_entity = await shahm1.get_entity(bot_usernameeee)





        await shahm1.send_message(bot_usernameeee, '/start')





        await asyncio.sleep(4)





        msg0 = await shahm1.get_messages(bot_usernameeee, limit=1)





        await msg0[0].click(2)





        await asyncio.sleep(4)





        msg1 = await shahm1.get_messages(bot_usernameeee, limit=1)





        await msg1[0].click(0)











        chs = 1





        for i in range(100):





            await asyncio.sleep(4)











            list = await shahm1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))





            msgs = list.messages[0]





            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")











                break





            url = msgs.reply_markup.rows[0].buttons[0].url





            try:





                try:





                    await shahm1(JoinChannelRequest(url))





                except:





                    bott = url.split('/')[-1]





                    await shahm1(ImportChatInviteRequest(bott))





                msg2 = await shahm1.get_messages(bot_usernameeee, limit=1)





                await msg2[0].click(text='تحقق')





                chs += 1





                await event.edit(f"تم الانضمام في {chs} قناة")





            except:





                msg2 = await shahm1.get_messages(bot_usernameeee, limit=1)





                await msg2[0].click(text='التالي')





                chs += 1





                await event.edit(f"القناة رقم {chs}")











        await shahm1.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")





        





@shahm1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))





async def _(event):











    await event.edit("**جاري تجميع النقاط**")





    joinu = await shahm1(JoinChannelRequest('ql8ql'))





    channel_entity = await shahm1.get_entity(bot_username)





    await shahm1.send_message(bot_username, '/start')





    await asyncio.sleep(4)





    msg0 = await shahm1.get_messages(bot_username, limit=1)





    await msg0[0].click(2)





    await asyncio.sleep(4)





    msg1 = await shahm1.get_messages(bot_username, limit=1)





    await msg1[0].click(0)











    chs = 1





    for i in range(100):





        await asyncio.sleep(4)











        list = await shahm1(GetHistoryRequest(peer=channel_entity, limit=1,





                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))





        msgs = list.messages[0]





        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





            await shahm1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SH**")











            break





        url = msgs.reply_markup.rows[0].buttons[0].url





        try:





            try:





                await shahm1(JoinChannelRequest(url))





            except:





                bott = url.split('/')[-1]





                await shahm1(ImportChatInviteRequest(bott))





            msg2 = await shahm1.get_messages(bot_username, limit=1)





            await msg2[0].click(text='تحقق')





            chs += 1





            await event.edit(f"**تم الانضمام في {chs} قناة**")





        except:





            msg2 = await shahm1.get_messages(bot_username, limit=1)





            await msg2[0].click(text='التالي')





            chs += 1





            await event.edit(f"**القناة رقم {chs}**")





    await shahm1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SH**")





    





    





    





@shahm1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))





async def _(event):











    await event.edit("**جاري تجميع النقاط**")





    joinu = await shahm1(JoinChannelRequest('Shahm_Sport'))





    channel_entity = await shahm1.get_entity(bot_usernamee)





    await shahm1.send_message(bot_usernamee, '/start')





    await asyncio.sleep(4)





    msg0 = await shahm1.get_messages(bot_usernamee, limit=1)





    await msg0[0].click(2)





    await asyncio.sleep(4)





    msg1 = await shahm1.get_messages(bot_usernamee, limit=1)





    await msg1[0].click(0)











    chs = 1





    for i in range(100):





        await asyncio.sleep(4)











        list = await shahm1(GetHistoryRequest(peer=channel_entity, limit=1,





                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))





        msgs = list.messages[0]





        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





            await shahm1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SH**")











            break





        url = msgs.reply_markup.rows[0].buttons[0].url





        try:





            try:





                await shahm1(JoinChannelRequest(url))





            except:





                bott = url.split('/')[-1]





                await shahm1(ImportChatInviteRequest(bott))





            msg2 = await shahm1.get_messages(bot_usernamee, limit=1)





            await msg2[0].click(text='تحقق')





            chs += 1





            await event.edit(f"**تم الانضمام في {chs} قناة**")





        except:





            msg2 = await shahm1.get_messages(bot_usernamee, limit=1)





            await msg2[0].click(text='التالي')





            chs += 1





            await event.edit(f"**القناة رقم {chs}**")





    await shahm1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SH**")











@shahm1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))





async def _(event):











    await event.edit("**جاري تجميع النقاط**")





    joinu = await shahm1(JoinChannelRequest('SH_AH_M1'))





    channel_entity = await shahm1.get_entity(bot_usernameee)





    await shahm1.send_message(bot_usernameee, '/start')





    await asyncio.sleep(4)





    msg0 = await shahm1.get_messages(bot_usernameee, limit=1)





    await msg0[0].click(2)





    await asyncio.sleep(4)





    msg1 = await shahm1.get_messages(bot_usernameee, limit=1)





    await msg1[0].click(0)











    chs = 1





    for i in range(100):





        await asyncio.sleep(4)











        list = await shahm1(GetHistoryRequest(peer=channel_entity, limit=1,





                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))





        msgs = list.messages[0]





        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





            await shahm1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SH**")











            break





        url = msgs.reply_markup.rows[0].buttons[0].url





        try:





            try:





                await shahm1(JoinChannelRequest(url))





            except:





                bott = url.split('/')[-1]





                await shahm1(ImportChatInviteRequest(bott))





            msg2 = await shahm1.get_messages(bot_usernameee, limit=1)





            await msg2[0].click(text='تحقق')





            chs += 1





            await event.edit(f"**تم الانضمام في {chs} قناة**")





        except:





            msg2 = await shahm1.get_messages(bot_usernameee, limit=1)





            await msg2[0].click(text='التالي')





            chs += 1





            await event.edit(f"**القناة رقم {chs}**")





    await shahm1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SH**")

















@shahm1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))





async def _(event):











    await event.edit("**جاري تجميع النقاط**")





    joinu = await shahm1(JoinChannelRequest('ql8ql'))





    channel_entity = await shahm1.get_entity(bot_usernameeee)





    await shahm1.send_message(bot_usernameeee, '/start')





    await asyncio.sleep(4)





    msg0 = await shahm1.get_messages(bot_usernameeee, limit=1)





    await msg0[0].click(2)





    await asyncio.sleep(4)





    msg1 = await shahm1.get_messages(bot_usernameeee, limit=1)





    await msg1[0].click(0)











    chs = 1





    for i in range(100):





        await asyncio.sleep(4)











        list = await shahm1(GetHistoryRequest(peer=channel_entity, limit=1,





                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))





        msgs = list.messages[0]





        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





            await shahm1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SH**")











            break





        url = msgs.reply_markup.rows[0].buttons[0].url





        try:





            try:





                await shahm1(JoinChannelRequest(url))





            except:





                bott = url.split('/')[-1]





                await shahm1(ImportChatInviteRequest(bott))





            msg2 = await shahm1.get_messages(bot_usernameeee, limit=1)





            await msg2[0].click(text='تحقق')





            chs += 1





            await event.edit(f"**تم الانضمام في {chs} قناة**")





        except:





            msg2 = await shahm1.get_messages(bot_usernameeee, limit=1)





            await msg2[0].click(text='التالي')





            chs += 1





            await event.edit(f"**القناة رقم {chs}**")





    await shahm1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SH**")





##########################################











@shahm1.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))





async def OwnerStart(event):





    pot = event.pattern_match.group(1) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        await event.reply("جاري تجميع النقاط")





        await event.edit("جاري تجميع النقاط")





        joinu = await shahm1(JoinChannelRequest('ql8ql'))





        channel_entity = await shahm1.get_entity(pot)





        await shahm1.send_message(pot, '/start')





        await asyncio.sleep(4)





        msg0 = await shahm1.get_messages(pot, limit=1)





        await msg0[0].click(2)





        await asyncio.sleep(4)





        msg1 = await shahm1.get_messages(pot, limit=1)





        await msg1[0].click(0)











        chs = 1





        for i in range(100):





            await asyncio.sleep(4)











            list = await shahm1(GetHistoryRequest(peer=channel_entity, limit=1,





                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))





            msgs = list.messages[0]





            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:





                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")











                break





            url = msgs.reply_markup.rows[0].buttons[0].url





            try:





                try:





                    await shahm1(JoinChannelRequest(url))





                except:





                    bott = url.split('/')[-1]





                    await shahm1(ImportChatInviteRequest(bott))





                msg2 = await shahm1.get_messages(pot, limit=1)





                await msg2[0].click(text='تحقق')





                chs += 1





                await event.edit(f"تم الانضمام في {chs} قناة")





            except:





                msg2 = await shahm1.get_messages(pot, limit=1)





                await msg2[0].click(text='التالي')





                chs += 1





                await event.edit(f"القناة رقم {chs}")











        await shahm1.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")





        





@shahm1.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*)'))





async def OwnerStart(event):





    bots = event.pattern_match.group(1) 





    ids = event.pattern_match.group(2) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await shahm1.send_message(bots,f'/start {ids}')





     sleep(6)





    msg = await shahm1.get_messages(bots, limit=2)





    await msg[1].forward_to(ownerhson_id)











@shahm1.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))





async def OwnerStart(event):





    pt = event.pattern_match.group(1) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await shahm1.send_message(bot_username, '/start')





     sleep(2)





    msg1 = await shahm1.get_messages(bot_username, limit=1)





    await msg1[0].click(3)





    sleep(4)





    await shahm1.send_message(bot_username, pt)





    sleep(4)





    msg = await shahm1.get_messages(bot_username, limit=1)






    await msg[0].forward_to(ownerhson_id)
    





@shahm1.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))





async def OwnerStart(event):





    pt = event.pattern_match.group(1) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await shahm1.send_message(bot_usernamee, '/start')





     sleep(2)





    msg1 = await shahm1.get_messages(bot_usernamee, limit=1)





    await msg1[0].click(3)





    sleep(4)





    await shahm1.send_message(bot_usernamee, pt)





    sleep(4)





    msg = await shahm1.get_messages(bot_usernamee, limit=1)






    await msg[0].forward_to(ownerhson_id)






@shahm1.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))





async def OwnerStart(event):





    pt = event.pattern_match.group(1) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await shahm1.send_message(bot_usernameee, '/start')





     sleep(2)





    msg1 = await shahm1.get_messages(bot_usernameee, limit=1)





    await msg1[0].click(3)





    sleep(4)





    await shahm1.send_message(bot_usernameee, pt)





    sleep(4)





    msg = await shahm1.get_messages(bot_usernameee, limit=1)






    await msg[0].forward_to(ownerhson_id)
    





@shahm1.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))





async def OwnerStart(event):





    pt = event.pattern_match.group(1) 





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await shahm1.send_message(bot_usernameeee, '/start')





     sleep(2)





    msg1 = await shahm1.get_messages(bot_usernameeee, limit=1)





    await msg1[0].click(3)





    sleep(4)





    await shahm1.send_message(bot_usernameeee, pt)





    sleep(4)





    msg = await shahm1.get_messages(bot_usernameeee, limit=1)






    await msg[0].forward_to(ownerhson_id)
    





@shahm1.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await shahm1.send_message(bot_username, '/start')





     sleep(2)





    msg1 = await shahm1.get_messages(bot_username, limit=1)





    await msg1[0].click(5)





    sleep(2)





    msg = await shahm1.get_messages(bot_username, limit=1)






    await msg[0].forward_to(ownerhson_id)   





@shahm1.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await shahm1.send_message(bot_usernamee, '/start')





     sleep(2)





    msg1 = await shahm1.get_messages(bot_usernamee, limit=1)





    await msg1[0].click(5)





    sleep(2)





    msg = await shahm1.get_messages(bot_usernamee, limit=1)






    await msg[0].forward_to(ownerhson_id)





@shahm1.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await shahm1.send_message(bot_usernameee, '/start')





     sleep(2)





    msg1 = await shahm1.get_messages(bot_usernameee, limit=1)





    await msg1[0].click(5)





    sleep(2)





    msg = await shahm1.get_messages(bot_usernameee, limit=1)






    await msg[0].forward_to(ownerhson_id)




@shahm1.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await shahm1.send_message(bot_usernameeee, '/start')





     sleep(2)





    msg1 = await shahm1.get_messages(bot_usernameeee, limit=1)





    await msg1[0].click(5)





    sleep(2)





    msg = await shahm1.get_messages(bot_usernameeee, limit=1)






    await msg[0].forward_to(ownerhson_id)






@shahm1.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        dialogs = await shahm1.get_dialogs()





        for dialog in dialogs:





            if dialog.is_channel:





                await shahm1(LeaveChannelRequest(dialog.entity))





                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")






@shahm1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





     usern = event.pattern_match.group(1)





    mase = event.pattern_match.group(2)





    await shahm1.send_message(usern, mase)





    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    






@shahm1.on(events.NewMessage(outgoing=False, pattern='/transfer'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط

• @ZMMBOT - `/pt1 + عدد النقاط `

• @A_MAN9300BOT - `/pt2 + عدد النقاط`

• @MARKTEBOT - `/pt3 + عدد النقاط `

• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")






@shahm1.on(events.NewMessage(outgoing=False, pattern='/infoacc'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 

• @ZMMBOT - `/npoint1`

• @A_MAN9300BOT - `/npoint2`

• @MARKTEBOT - `/npoint3`

• @XNSEX21BOT - `/npoint4`**""")





@shahm1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))





async def OwnerStart(event):





    userbt = event.pattern_match.group(1) 





    bt = int(event.pattern_match.group(2))





    sender = await event.get_sender()





    if sender.id == ownerhson_id :





     send = await shahm1.send_message(userbt, '/start')





     sleep(2)





    msg1 = await shahm1.get_messages(userbt, limit=1)





    await msg1[0].click(bt)
        





@shahm1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))





async def OwnerStart(event):





    userbott = event.pattern_match.group(1)





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        msg = await shahm1.get_messages(userbott, limit=1)





        await msg[0].forward_to(ownerhson_id)
        





@shahm1.on(events.NewMessage(outgoing=False, pattern='/join'))





async def OwnerStart(event):





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        send = await shahm1.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")





        joinq = await shahm1(JoinChannelRequest('d3boot_7'))




        joinw = await shahm1(JoinChannelRequest('Fvvvv'))





        joine = await shahm1(JoinChannelRequest('DzDDDD'))





        joinr = await shahm1(JoinChannelRequest('botbillion'))




        joint = await shahm1(JoinChannelRequest('zzzzzz1'))





        joiny = await shahm1(JoinChannelRequest('zzzzzz'))





        joini = await shahm1(JoinChannelRequest('zz_MX'))





        joino = await shahm1(JoinChannelRequest('lI7777Il'))





        joinp = await shahm1(JoinChannelRequest('KTTTT'))





        joina = await shahm1(JoinChannelRequest('RRXFR'))





        sendd = await shahm1.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        





@shahm1.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))





async def OwnerStart(event):





    usercht = event.pattern_match.group(1)





    sender = await event.get_sender()





    if sender.id == ownerhson_id:





        sendy = await shahm1.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")





        joinch = await shahm1(JoinChannelRequest(usercht))





        sendy = await shahm1.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")






print("💠 shahm Userbot Running 💠")





shahm1.run_until_disconnected()






#code skip accumulate points by t.me.zzzzl1l thank you my bro






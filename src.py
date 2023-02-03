import os
import requests
import discord
from discord.ext import commands

token = os.environ.get["token"]

vdict = {
    "mln68v0q": "1.16.1",
    "gq7rrnnl": "1.14.4",
    "jq6vwj1m": "1.7.2",
    "013xkx15": "1.7.10",
    "4lx5gk41": "1.8.9",
    "9qj2o314": "1.6.4",
    "rqvx06l6": "1.0",
    "5len0klo": "1.1",
    "0q54m2lp": "1.2.1",
    "4lxgk4q2": "1.2.2",
    "81496vqd": "1.2.3",
    "z19xv814": "1.2.4",
    "p129k4lx": "1.2.5",
    "81pez8l7": "1.3.1",
    "xqko3k19": "1.3.2",
    "gq72od1p": "1.4.2",
    "21g968qz": "1.4.4",
    "jqzgw8lp": "1.4.5",
    "klrxdmlp": "1.4.6",
    "21d6n5qe": "1.4.7",
    "5q8433ld": "1.5.1",
    "4qy7m2q7": "1.5.2",
    "mlne7jlp": "1.6.1",
    "8106y21v": "1.6.2",
    "21d43441": "1.7.3",
    "5lm2emqv": "1.7.4",
    "81w72vq4": "1.7.5",
    "814o96vq": "1.7.6",
    "z192xv8q": "1.7.7",
    "p12v9k4q": "1.7.8",
    "zqojex1y": "1.7.9",
    "rqvx26l6": "1.8",
    "5lenyklo": "1.8.1",
    "21dv7g1e": "1.8.2",
    "5q8276qd": "1.8.3",
    "5le86mlo": "1.8.4",
    "01340kl5": "1.8.5",
    "rqvz7516": "1.8.6",
    "5levop1o": "1.8.7",
    "gq7zyr1p": "1.8.8",
    "81pyez81": "1.9",
    "xqkeo3kq": "1.9.1",
    "gq752od1": "1.9.2",
    "21gn968l": "1.9.3",
    "jqzngw8q": "1.9.4",
    "klr3xdml": "1.10",
    "5lmygj8l": "1.10.1",
    "jq678gv1": "1.10.2",
    "0q54o3nl": "1.11",
    "zqo0rw5q": "1.11.1",
    "4lxgvw4q": "1.11.2",
    "xqkonxn1": "1.12",
    "5q8270kq": "1.12.1",
    "p12ongvl": "1.12.2",
    "8142pg0l": "1.13",
    "z19rz201": "1.13.1",
    "z19ryv41": "1.13.2",
    "9qj49koq": "1.14",
    "01305er1": "1.14.1",
    "814vn2v1": "1.14.2",
    "jqzx69m1": "1.14.3",
    "gq7zrdd1": "1.15",
    "21dor7gq": "1.15.1",
    "21go7k8q": "1.15.2",
    "mln64j6q": "1.16",
    "21d7zo31": "1.16.2",
    "21d7evp1": "1.16.3",
    "21dgwkj1": "1.16.4",
    "21dzz0jl": "1.16.5",
    "5q8ojzr1": "1.17",
    "4qy93w3l": "1.17.1",
    "81w2nk61":"1.18",
    "mlnj0md1":"1.18.1",
    "810kmj5q":"1.18.2",
    "jqzoe341":"1.19",
    "9qj33d0l":"1.19.1",
    "jq6dd7n1":"1.19.2",
    "81w0gjol":"1.19.3"
}

diffidict = {
    "4lxg24q2":"Easy",
    "8149mvqd":"Normal",
    "z19xe814":"Hard",
    "p129j4lx":"Hardcore",
}

rangedict = {
    "gq7zo9p1":"Pre 1.9",
    "jq6j9571":"1.9-1.12",
    "21go6e6q":"1.13-1.15",
    "4qye4731":"1.16+"
}

f3dict = {
    "rqvmvz6q": "F3",
    "5lee2vkl": "No F3",

}

modsdict = {
    "21gyvwm1":"Vanilla",
    "jqzk8rmq":"Optifine",
    "jq6kxd3l":"Modded",

}

stdict = {
    "klrzpjo1":"SSG",
    "21d4zvp1":"RSG"
}

bot = commands.Bot(command_prefix="!", help_command = None)

a = range(0,30)
def worldRecord(wr):
        userid = wr.json()["data"]["runs"][0]["run"]["players"][0]["id"]
        rt = wr.json()["data"]["runs"][0]["run"]["times"]["realtime_t"]
        igt = wr.json()["data"]["runs"][0]["run"]["times"]["ingame_t"]

        try:
            dot = str(rt)
            dot = dot.index(".")
            intsec = str(rt)[:int(dot)]
            rtmin = int(intsec) // 60
            rthr = rtmin // 60
            rtsec = int(intsec) % 60
            rtmin = rtmin % 60
            rtms = str(rt)[int(dot) + 1:]
        except ValueError:
            intsec = str(rt)
            rtmin = int(intsec) // 60
            rthr = rtmin // 60
            rtsec = int(intsec) % 60
            rtmin = rtmin % 60
            rtms = str(rt)[int(dot) + 1:]

        # ------ IGT ------
        try:
            dot = str(igt)
            dot = dot.index(".")
            intsec = str(igt)[:int(dot)]
            igtmin = int(intsec) // 60
            igthr = igtmin // 60
            igtsec = int(intsec) % 60
            igtmin = igtmin % 60
            igtms = str(igt)[int(dot) + 1:]
        except ValueError:
            intsec = str(igt)
            igtmin = int(intsec) // 60
            igthr = igtmin // 60
            igtsec = int(intsec) % 60
            igtmin = igtmin % 60
            igtms = str(igt)[int(dot) + 1:]



        userres = requests.get(f"https://www.speedrun.com/api/v1/users/{userid}")
        username = userres.json()["data"]["names"]["international"]

        date = wr.json()["data"]["runs"][0]["run"]["date"]
        comment = wr.json()["data"]["runs"][0]["run"]["comment"]



        seedtype = wr.json()["data"]["runs"][0]["run"]["values"]["r8rg67rn"]
        version = vdict[wr.json()["data"]["runs"][0]["run"]["values"]["jlzkwql2"]]
        difficulty = diffidict[wr.json()["data"]["runs"][0]["run"]["values"]["9l737pn1"]]
        vrange = rangedict[wr.json()["data"]["runs"][0]["run"]["values"]["wl33kewl"]]
        f3 = f3dict[wr.json()["data"]["runs"][0]["run"]["values"]["ql6g2ow8"]]
        mods = modsdict[wr.json()["data"]["runs"][0]["run"]["values"]["dloymqd8"]]
        try:
            uri = wr.json()["data"]["runs"][0]["run"]["videos"]["links"][0]["uri"]
        except KeyError:
            uri = wr.json()["data"]["runs"][0]["run"]["videos"]["text"]

        rthr = str(rthr).zfill(2)
        rtmin =str(rtmin).zfill(2)
        rtsec =str(rtsec).zfill(2)
        rtms = str(rtms).ljust(3, "0")
        
        igthr = str(igthr).zfill(2)
        igtmin = str(igtmin).zfill(2)
        igtsec = str(igtsec).zfill(2)
        igtms = str(igtms).ljust(3, "0")
        wrembed = discord.Embed(color = 0xFFFD58, title=f"{stdict[seedtype]} WR:")
        wrembed.add_field(name = f"Player: {username}", value = f"\n\nRTA: {rthr}:{rtmin}:{rtsec}.{rtms}\nIGT: {igthr}:{igtmin}:{igtsec}.{igtms}\nDate: {date}\n\nVersion: {version}\nDifficulty: {difficulty}\nVersion Range: {vrange}\nF3: {f3}\nMods: {mods}\n\nVideo URI: <{uri}>\n\nComment: ```\n{comment}```\n\nMC Speedrun Bot by ProtossManse#3053", inline=False)
        return wrembed



@bot.event
async def on_ready():
    print(f"Login...\n{bot.user.name}\n{bot.user.id}\n------------")


@bot.command()
async def SSG(ctx, string, ver):
    if string == "WR" and ver == "1":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "klrzpjo1", "var-wl33kewl": "4qye4731","top": "1"})
        if wr.status_code == 200:
            wrembed = worldRecord(wr)
            await ctx.send(embed=wrembed)
        elif wr.status_code == 420:
            await ctx.send("The API service is too busy to handle your request. Please try again later.")
    elif string == "WR" and ver == "2":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "klrzpjo1","var-wl33kewl": "21go6e6q","top": "1"})
        if wr.status_code == 200:
            wrembed = worldRecord(wr)
            await ctx.send(embed=wrembed)
        elif wr.status_code == 420:
            await ctx.send("The API service is too busy to handle your request. Please try again later.")
    elif string == "WR" and ver == "3":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "klrzpjo1","var-wl33kewl": "jq6j9571","top": "1"})
        if wr.status_code == 200:
            wrembed = worldRecord(wr)
            await ctx.send(embed=wrembed)
        elif wr.status_code == 420:
            await ctx.send("The API service is too busy to handle your request. Please try again later.")
    elif string == "WR" and ver == "4":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "klrzpjo1","var-wl33kewl": "gq7zo9p1","top": "1"})
        if wr.status_code == 200:
            wrembed = worldRecord(wr)
            await ctx.send(embed=wrembed)
        elif wr.status_code == 420:
            await ctx.send("The API service is too busy to handle your request. Please try again later.")
    else:
        await ctx.send("Unknown Command.\n```\nSSG WR {1 | 2 | 3 | 4}```")

        

@bot.command()
async def RSG(ctx, string, ver):
    if string == "WR" and ver == "1":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "21d4zvp1", "var-wl33kewl": "4qye4731", "top": "1"})
        if wr.status_code == 200:
            wrembed = worldRecord(wr)
            await ctx.send(embed=wrembed)
        elif wr.status_code == 420:
            await ctx.send("The API service is too busy to handle your request. Please try again later.")
    elif string == "WR" and ver == "2":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "21d4zvp1", "var-wl33kewl": "21go6e6q", "top": "1"})
        if wr.status_code == 200:
            wrembed = worldRecord(wr)
            await ctx.send(embed=wrembed)
        elif wr.status_code == 420:
            await ctx.send("The API service is too busy to handle your request. Please try again later.")
    elif string == "WR" and ver == "3":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "21d4zvp1", "var-wl33kewl": "jq6j9571", "top": "1"})
        if wr.status_code == 200:
            wrembed = worldRecord(wr)
            await ctx.send(embed=wrembed)
        elif wr.status_code == 420:
            await ctx.send("The API service is too busy to handle your request. Please try again later.")
    elif string == "WR" and ver == "4":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "21d4zvp1", "var-wl33kewl": "gq7zo9p1", "top": "1"})
        if wr.status_code == 200:
            wrembed = worldRecord(wr)
            await ctx.send(embed=wrembed)
        elif wr.status_code == 420:
            await ctx.send("The API service is too busy to handle your request. Please try again later.")
    else:
        await ctx.send("Unknown Command.\n```\nRSG WR {1 | 2 | 3 | 4 | 4}```")




@bot.command()
async def PB(ctx, string, str2, *args):
    if str2 == "RSG" or str2 ==  "SSG" and args[0]:
        jepb = requests.get(f"https://www.speedrun.com/api/v1/users/{string}/personal-bests", params={"game": "j1npme6p"})
        if jepb.status_code == 200:
            try:
                for i in a:
                    if jepb.json()["data"][i]["run"]["category"] == "mkeyl926":
                        seedtype = stdict[jepb.json()["data"][i]["run"]["values"]["r8rg67rn"]]
                        ver = rangedict[jepb.json()["data"][i]["run"]["values"]["wl33kewl"]]
                        if str2 == "SSG" and seedtype == "SSG":
                            if args[0] == "1" and ver == "1.16+":
                                run = i
                                break
                            if args[0] == "2" and ver == "1.9-1.12":
                                run = i
                                break
                            if args[0] == "3" and ver == "1.13-1.15":
                                run = i
                                break
                            if args[0] == "4" and ver == "Pre 1.9":
                                run = i
                                break
                        if str2 == "RSG" and seedtype == "RSG":
                            if args[0] == "1" and ver == "1.16+":
                                run = i
                                break
                            if args[0] == "2" and ver == "1.9-1.12":
                                run = i
                                break
                            if args[0] == "3" and ver == "1.13-1.15":
                                run = i
                                break
                            if args[0] == "4" and ver == "Pre 1.9":
                                run = i
                                break
                    else:
                        continue
            except (IndexError, KeyError):
                await ctx.send("Run not found.")
            rt = jepb.json()["data"][run]["run"]["times"]["realtime_t"]
            igt = jepb.json()["data"][run]["run"]["times"]["ingame_t"]

            # ------ RTA ------
            try:
                dot = str(rt)
                dot = dot.index(".")
                intsec = str(rt)[:int(dot)]
                rtmin = int(intsec) // 60
                rthr = rtmin // 60
                rtsec = int(intsec) % 60
                rtmin = rtmin % 60
                rtms = str(rt)[int(dot) + 1:]
            except ValueError:
                intsec = str(rt)
                rtmin = int(intsec) // 60
                rthr = rtmin // 60
                rtsec = int(intsec) % 60
                rtmin = rtmin % 60
                rtms = str(rt)[int(dot) + 1:]

            # ------ IGT ------
            try:
                dot = str(igt)
                dot = dot.index(".")
                intsec = str(igt)[:int(dot)]
                igtmin = int(intsec) // 60
                igthr = igtmin // 60
                igtsec = int(intsec) % 60
                igtmin = igtmin % 60
                igtms = str(igt)[int(dot) + 1:]
            except ValueError:
                intsec = str(igt)
                igtmin = int(intsec) // 60
                igthr = igtmin // 60
                igtsec = int(intsec) % 60
                igtmin = igtmin % 60
                igtms = str(igt)[int(dot) + 1:]



            date = jepb.json()["data"][run]["run"]["date"]
            comment = jepb.json()["data"][run]["run"]["comment"]


            version = vdict[jepb.json()["data"][run]["run"]["values"]["jlzkwql2"]]
            difficulty = diffidict[jepb.json()["data"][run]["run"]["values"]["9l737pn1"]]
            vrange = rangedict[jepb.json()["data"][run]["run"]["values"]["wl33kewl"]]
            f3 = f3dict[jepb.json()["data"][run]["run"]["values"]["ql6g2ow8"]]
            mods = modsdict[jepb.json()["data"][run]["run"]["values"]["dloymqd8"]]
            
            place = jepb.json()["data"][run]["place"]

            if seedtype == "SSG":
                colorvar = 0x73E089
            elif seedtype == "RSG":
                colorvar = 0x3598FB

        
            try:
                uri = jepb.json()["data"][run]["run"]["videos"]["links"][0]["uri"]
            except KeyError:
                uri = jepb.json()["data"][run]["run"]["videos"]["text"]
            
            rthr = str(rthr).zfill(2)
            rtmin =str(rtmin).zfill(2)
            rtsec =str(rtsec).zfill(2)
            rtms = str(rtms).ljust(3, "0")
            
            igthr = str(igthr).zfill(2)
            igtmin = str(igtmin).zfill(2)
            igtsec = str(igtsec).zfill(2)
            igtms = str(igtms).ljust(3, "0")

            SSGPBembed = discord.Embed(color = colorvar, title=f"{seedtype} PB:")
            SSGPBembed.add_field(name = f"Player: {string}", value = f"\n\nRTA: {rthr}:{rtmin}:{rtsec}.{rtms}\nIGT: {igthr}:{igtmin}:{igtsec}.{igtms}\nPlace: {place}\nDate: {date}\n\nVersion: {version}\nDifficulty: {difficulty}\nVersion Range: {vrange}\nF3: {f3}\nMods: {mods}\n\nVideo URI: <{uri}>\n\nComment: ```\n{comment}```\n\nMC Speedrun Bot by ProtossManse#3053", inline=False)
            await ctx.send(embed=SSGPBembed)
        elif jepb.status_code == 404:
            await ctx.send("Unknown user name.")
        elif jepb.status_code == 420:
            await ctx.send("The API service is too busy to handle your request. Please try again later.")
    else:
        await ctx.send("Unknown Command.\n```\nPB {username} {SSG | RSG} {1 | 2 | 3 | 4}```")
    



@bot.command(name="help")
async def help(ctx):
    await ctx.send("```\nPrefix: !\n\n1: 1.16+\n2: 1.13-1.15\n3: 1.9-1.12\n4: Pre 1.9 \n\n!SSG WR {1 | 2 | 3 | 4} \n!RSG WR {1 | 2 | 3 | 4}\n\n!PB {username} {SSG | RSG} {1 | 2 | 3 | 4}\n\n!Pag\n\nContact: ProtossManse#3053(discord)```")

@bot.command()
async def Pag(ctx):
    await ctx.send("Yo everyone what's going on couriway here.")

@bot.command()
async def text(ctx, message):
    await ctx.send(message)

@bot.command()
async def patchnote(ctx):
    patchembed = discord.Embed(color = 0xCD2E57, title= "Patch Notes:")
    patchembed.add_field(name="죄송합니다", value="\n\n현생이 바빠서 여기 서버 들어오지도 못했네요 ㅜㅜ \n\n버전 바뀌었다는 거랑 이 봇이 없어졌다는 것도 얼마 전에 알았어요..\n\n")
    patchembed.add_field(name="",value="")
    patchembed.add_field(name="",value="")
    patchembed.add_field(name="\n버전 세분화", value="\n\n스피드런 버전에 맞춰 네가지 버전으로 조회가 가능해졌습니다.\n\n")
    patchembed.add_field(name="",value="")
    patchembed.add_field(name="",value="")
    patchembed.add_field(name="!help 명령어 추가",value="\n\n")
    patchembed.add_field(name="",value="")
    patchembed.add_field(name="",value="")
    patchembed.add_field(name="버그 수정",value="이제 다시 봇이 작동합니다.\n\n")
    await ctx.send(embed=patchembed)


bot.run(token)

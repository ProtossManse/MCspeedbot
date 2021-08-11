import os
import requests
import discord
from discord.ext import commands

token = os.environ["token"]

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
        wrembed.add_field(name = f"Player: {username}", value = f"\n\nRTA: {rthr}:{rtmin}:{rtsec}.{rtms}\nIGT: {igthr}:{igtmin}:{igtsec}.{igtms}\nDate: {date}\n\nVersion: {version}\nDifficulty: {difficulty}\nVersion Range: {vrange}\nF3: {f3}\nMods: {mods}\n\nVideo URI: <{uri}>\n\nComment: ```\n{comment}```", inline=False)
        return wrembed

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
    "4qy93w3l": "1.17.1"
    }

diffidict = {
    "4lxg24q2":"Easy",
    "8149mvqd":"Normal",
    "z19xe814":"Hard",
    "p129j4lx":"Hardcore",
    # ----- FSG: -----
    "21g22nnl":"Easy",
    "jqzxxng1":"Normal",
    "klryy3jq":"Hard",
    "21d33k4q":"Hardcore"
}

rangedict = {
    "gq7zo9p1":"Pre 1.9",
    "21go6e6q":"1.9-1.15",
    "4qye4731":"1.16+"
}

f3dict = {
    "rqvmvz6q": "F3",
    "5lee2vkl": "No F3",
    # ----- FSG: -----
    "zqorkv5q":"No F3",
    "81w5z0m1":"F3"
}

modsdict = {
    "21gyvwm1":"Vanilla",
    "jqzk8rmq":"Optifine",
    "jq6kxd3l":"Modded",
    # ----- FSG: -----
    "klrnve21":"Vanilla",
    "21dr9kjq":"Optifine",
    "5lmj45jl":"Modded"
}

stdict = {
    "klrzpjo1":"SSG",
    "21d4zvp1":"RSG"
}

bot = commands.Bot(command_prefix="!", help_command = None)

a = range(0,30)



@bot.event
async def on_ready():
    print(f"Login...\n{bot.user.name}\n{bot.user.id}\n------------")


@bot.command()
async def SSG(ctx, string, ver):
    if string == "WR" and ver == "1":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "klrzpjo1", "var-wl33kewl": "4qye4731","top": "1"})
        wrembed = worldRecord(wr)
        await ctx.send(embed=wrembed)
    if string == "WR" and ver == "2":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "klrzpjo1","var-wl33kewl": "21go6e6q","top": "1"})
        wrembed = worldRecord(wr)
        await ctx.send(embed=wrembed)
    if string == "WR" and ver == "3":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "klrzpjo1","var-wl33kewl": "gq7zo9p1","top": "1"})
        wrembed = worldRecord(wr)
        await ctx.send(embed=wrembed)
    else:
        await ctx.send("Unknown Command.\n```\nSSG WR {1 | 2 | 3}```")

        

@bot.command()
async def RSG(ctx, string, ver):
    if string == "WR" and ver == "1":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "21d4zvp1", "var-wl33kewl": "4qye4731", "top": "1"})
        wrembed = worldRecord(wr)
        await ctx.send(embed=wrembed)
    if string == "WR" and ver == "2":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "21d4zvp1", "var-wl33kewl": "21go6e6q", "top": "1"})
        wrembed = worldRecord(wr)
        await ctx.send(embed=wrembed)
    if string == "WR" and ver == "3":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "21d4zvp1", "var-wl33kewl": "gq7zo9p1", "top": "1"})
        wrembed = worldRecord(wr)
        await ctx.send(embed=wrembed)
    else:
        await ctx.send("Unknown Command.\n```\nRSG WR {1 | 2 | 3}```")


@bot.command()
async def FSG(ctx, string):
    if string == "WR":
        wr = requests.get("https://www.speedrun.com/api/v1/leaderboards/nd2e9erd/category/n2y9z41d", params={"top": "1"})
        userid = wr.json()["data"]["runs"][0]["run"]["players"][0]["id"]
        rt = wr.json()["data"]["runs"][0]["run"]["times"]["realtime_t"]
        igt = wr.json()["data"]["runs"][0]["run"]["times"]["ingame_t"]

        # ------ RTA ------
        dot = str(rt)
        dot = dot.index(".")
        intsec = str(rt)[:int(dot)]
        rtmin = int(intsec) // 60
        rthr = rtmin // 60
        rtsec = int(intsec) % 60
        rtmin = rtmin % 60
        rtms = str(rt)[int(dot) + 1:]

        # ------ IGT ------

        dot = str(igt)
        dot = dot.index(".")
        intsec = str(igt)[:int(dot)]
        igtmin = int(intsec) // 60
        igthr = igtmin // 60
        igtsec = int(intsec) % 60
        igtmin = igtmin % 60
        igtms = str(igt)[int(dot) + 1:]



        userres = requests.get(f"https://www.speedrun.com/api/v1/users/{userid}")
        username = userres.json()["data"]["names"]["international"]

        date = wr.json()["data"]["runs"][0]["run"]["date"]
        comment = wr.json()["data"]["runs"][0]["run"]["comment"]

        try:
            uri = wr.json()["data"]["runs"][0]["run"]["videos"]["links"][0]["uri"]

        except KeyError:
            uri = wr.json()["data"]["runs"][0]["run"]["videos"]["text"]

        difficulty = diffidict[wr.json()["data"]["runs"][0]["run"]["values"]["0nwkeorn"]]
        f3 = f3dict[wr.json()["data"]["runs"][0]["run"]["values"]["ylqkjo3l"]]
        mods = modsdict[wr.json()["data"]["runs"][0]["run"]["values"]["jlzwkmql"]]

        rthr = str(rthr).zfill(2)
        rtmin = str(rtmin).zfill(2)
        rtsec = str(rtsec).zfill(2)
        rtms = str(rtms).ljust(3, "0")
        
        igthr = str(igthr).zfill(2)
        igtmin = str(igtmin).zfill(2)
        igtsec = str(igtsec).zfill(2)
        igtms = str(igtms).ljust(3, "0")

        FSGembed = discord.Embed(color = 0xFFFD58,title= "FSG WR:")
        FSGembed.add_field(name= f"Player: {username}", value = f"\r\n\r\nRTA: {rthr}:{rtmin}:{rtsec}.{rtms}\nIGT: {igthr}:{igtmin}:{igtsec}.{igtms}\nDate: {date}\n\nVersion: 1.16.1\nDifficulty: {difficulty}\nF3: {f3}\nMods: {mods}\n\nVideo URI: <{uri}>\n\nComment: **`{comment}`**", inline=False)

        await ctx.send(embed=FSGembed)


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
                            if args[0] == "2" and ver == "1.9-1.15":
                                run = i
                                break
                            if args[0] == "3" and ver == "Pre 1.9":
                                run = i
                                break
                        if str2 == "RSG" and seedtype == "RSG":
                            if args[0] == "1" and ver == "1.16+":
                                run = i
                                break
                            if args[0] == "2" and ver == "1.9-1.15":
                                run = i
                                break
                            if args[0] == "3" and ver == "Pre 1.9":
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
            SSGPBembed.add_field(name = f"Player: {string}", value = f"\n\nRTA: {rthr}:{rtmin}:{rtsec}.{rtms}\nIGT: {igthr}:{igtmin}:{igtsec}.{igtms}\nPlace: {place}\nDate: {date}\n\nVersion: {version}\nDifficulty: {difficulty}\nVersion Range: {vrange}\nF3: {f3}\nMods: {mods}\n\nVideo URI: <{uri}>\n\nComment: **`{comment}`**", inline=False)
            await ctx.send(embed=SSGPBembed)
        elif jepb.status_code == 404:
            await ctx.send("Unknown user name.")
        elif jepb.status_code == 420:
            await ctx.send("Please try again later.")
    if str2 == "FSG":
        fsgpb = requests.get(f"https://www.speedrun.com/api/v1/users/{string}/personal-bests", params={"game": "nd2e9erd"})
        if fsgpb.status_code == 200:
            try:
                for i in a:
                    cecategory = fsgpb.json()["data"][i]["run"]["category"]
                    if cecategory == "n2y9z41d":
                        runlist = i
                        break
            except(KeyError, IndexError):
                await ctx.send("Run not found.")

            rt = fsgpb.json()["data"][runlist]["run"]["times"]["realtime_t"]
            igt = fsgpb.json()["data"][runlist]["run"]["times"]["ingame_t"]

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



            date = fsgpb.json()["data"][runlist]["run"]["date"]
            comment = fsgpb.json()["data"][runlist]["run"]["comment"]
            place = fsgpb.json()["data"][runlist]["place"]

            difficulty = diffidict[fsgpb.json()["data"][runlist]["run"]["values"]["0nwkeorn"]]
            f3 = f3dict[fsgpb.json()["data"][runlist]["run"]["values"]["ylqkjo3l"]]
            mods = modsdict[fsgpb.json()["data"][runlist]["run"]["values"]["jlzwkmql"]]

            try:
                uri = fsgpb.json()["data"][runlist]["run"]["videos"]["links"][0]["uri"]
            except KeyError:
                uri = fsgpb.json()["data"][runlist]["run"]["videos"]["text"]

            rthr = str(rthr).zfill(2)
            rtmin =str(rtmin).zfill(2)
            rtsec =str(rtsec).zfill(2)
            rtms = str(rtms).ljust(3, "0")
            
            igthr = str(igthr).zfill(2)
            igtmin = str(igtmin).zfill(2)
            igtsec = str(igtsec).zfill(2)
            igtms = str(igtms).ljust(3, "0")


            fsgpbembed = discord.Embed(color = 0xFAA643,title= "FSG PB:")
            fsgpbembed.add_field(name= f"Player: {string}", value = f"\r\n\r\nRTA: {rthr}:{rtmin}:{rtsec}.{rtms}\nIGT: {igthr}:{igtmin}:{igtsec}.{igtms}\nDate: {date}\n\nVersion: 1.16.1\nDifficulty: {difficulty}\nF3: {f3}\nMods: {mods}\n\nVideo URI: <{uri}>\n\nComment: **`{comment}`**", inline=False)

            await ctx.send(embed=fsgpbembed)
        elif fsgpb.status_code == 404:
            await ctx.send("Unknown username.")    
        elif fsgpb.status_code == 420:
            await ctx.send("Please try again later.")


@bot.command(name="?")
async def help(ctx):
    await ctx.send("```\nPrefix: !\n\nSSG WR {1 | 2 | 3} \nRSG WR {1 | 2 | 3}\nFSG WR\n\nPB {src-name} {SSG | RSG | FSG} {1 | 2 | 3}\n\nPag```")

@bot.command()
async def Pag(ctx):
    await ctx.send("Yo everyone what's going on couriway here.")

@bot.command()
async def text(ctx, message):
    await ctx.send(message)


bot.run(token)

import os
import requests
import discord
from discord.ext import commands


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


token = os.environ["token"]


@bot.event
async def on_ready():
    print(f"Login...\n{bot.user.name}\n{bot.user.id}\n------------")


@bot.command()
async def SSG(ctx, string):
    if string == "WR":
        ssgwr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "klrzpjo1","top": "1"})
        userid = ssgwr.json()["data"]["runs"][0]["run"]["players"][0]["id"]
        rt = ssgwr.json()["data"]["runs"][0]["run"]["times"]["realtime_t"]
        igt = ssgwr.json()["data"]["runs"][0]["run"]["times"]["ingame_t"]

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

        date = ssgwr.json()["data"]["runs"][0]["run"]["date"]
        comment = ssgwr.json()["data"]["runs"][0]["run"]["comment"]


        version = vdict[ssgwr.json()["data"]["runs"][0]["run"]["values"]["jlzkwql2"]]
        difficulty = diffidict[ssgwr.json()["data"]["runs"][0]["run"]["values"]["9l737pn1"]]
        vrange = rangedict[ssgwr.json()["data"]["runs"][0]["run"]["values"]["wl33kewl"]]
        f3 = f3dict[ssgwr.json()["data"]["runs"][0]["run"]["values"]["ql6g2ow8"]]
        mods = modsdict[ssgwr.json()["data"]["runs"][0]["run"]["values"]["dloymqd8"]]

        

        
        try:
            uri = ssgwr.json()["data"]["runs"][0]["run"]["videos"]["links"][0]["uri"]
        except KeyError:
            uri = ssgwr.json()["data"]["runs"][0]["run"]["videos"]["text"]
            
        SSGembed = discord.Embed(color = 0xFFFD58, title="SSG WR:")
        SSGembed.add_field(name = f"Player: {username}", value = f"\n\nRTA: {rthr}:{rtmin}:{rtsec}.{rtms}\nIGT: {igthr}:{igtmin}:{igtsec}.{igtms}\nDate: {date}\n\nVersion: {version}\nDifficulty: {difficulty}\nVersion Range: {vrange}\nF3: {f3}\nMods: {mods}\n\nVideo URI: <{uri}>\n\nComment: **`{comment}`**", inline=False)

        await ctx.send(embed=SSGembed)

    



@bot.command()
async def RSG(ctx, string):
    if string == "WR":
        rsgwr = requests.get("https://www.speedrun.com/api/v1/leaderboards/j1npme6p/category/mkeyl926", params={"var-r8rg67rn": "21d4zvp1", "top": "1"})
        userid = rsgwr.json()["data"]["runs"][0]["run"]["players"][0]["id"]
        rt = rsgwr.json()["data"]["runs"][0]["run"]["times"]["realtime_t"]
        igt = rsgwr.json()["data"]["runs"][0]["run"]["times"]["ingame_t"]

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

        date = rsgwr.json()["data"]["runs"][0]["run"]["date"]
        comment = rsgwr.json()["data"]["runs"][0]["run"]["comment"]

        try:
            uri = rsgwr.json()["data"]["runs"][0]["run"]["videos"]["links"][0]["uri"]

        except KeyError:
            uri = rsgwr.json()["data"]["runs"][0]["run"]["videos"]["text"]

        version = vdict[rsgwr.json()["data"]["runs"][0]["run"]["values"]["jlzkwql2"]]
        difficulty = diffidict[rsgwr.json()["data"]["runs"][0]["run"]["values"]["9l737pn1"]]
        vrange = rangedict[rsgwr.json()["data"]["runs"][0]["run"]["values"]["wl33kewl"]]
        f3 = f3dict[rsgwr.json()["data"]["runs"][0]["run"]["values"]["ql6g2ow8"]]
        mods = modsdict[rsgwr.json()["data"]["runs"][0]["run"]["values"]["dloymqd8"]]

        RSGembed = discord.Embed(color = 0xFFFD58, title="RSG WR:")
        RSGembed.add_field(name= f"Player: {username}", value = f"\n\nRTA: {rthr}:{rtmin}:{rtsec}.{rtms}\nIGT: {igthr}:{igtmin}:{igtsec}.{igtms}\nDate: {date}\n\nVersion: {version}\nDifficulty: {difficulty}\nVersion Range: {vrange}\nF3: {f3}\nMods: {mods}\n\nVideo URI: <{uri}>\n\nComment: **`{comment}`**", inline=False)

        await ctx.send (embed=RSGembed)


@bot.command()
async def FSG(ctx, string):
    if string == "WR":
        fsgwr = requests.get("https://www.speedrun.com/api/v1/leaderboards/nd2e9erd/category/n2y9z41d", params={"top": "1"})
        userid = fsgwr.json()["data"]["runs"][0]["run"]["players"][0]["id"]
        rt = fsgwr.json()["data"]["runs"][0]["run"]["times"]["realtime_t"]
        igt = fsgwr.json()["data"]["runs"][0]["run"]["times"]["ingame_t"]

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

        date = fsgwr.json()["data"]["runs"][0]["run"]["date"]
        comment = fsgwr.json()["data"]["runs"][0]["run"]["comment"]

        try:
            uri = fsgwr.json()["data"]["runs"][0]["run"]["videos"]["links"][0]["uri"]

        except KeyError:
            uri = fsgwr.json()["data"]["runs"][0]["run"]["videos"]["text"]

        difficulty = diffidict[fsgwr.json()["data"]["runs"][0]["run"]["values"]["0nwkeorn"]]
        f3 = f3dict[fsgwr.json()["data"]["runs"][0]["run"]["values"]["ylqkjo3l"]]
        mods = modsdict[fsgwr.json()["data"]["runs"][0]["run"]["values"]["jlzwkmql"]]

        FSGembed = discord.Embed(color = 0xFFFD58,title= "FSG WR:")
        FSGembed.add_field(name= f"Player: {username}", value = f"\r\n\r\nRTA: {rthr}:{rtmin}:{rtsec}.{rtms}\nIGT: {igthr}:{igtmin}:{igtsec}.{igtms}\nDate: {date}\n\nVersion: 1.16.1\nDifficulty: {difficulty}\nF3: {f3}\nMods: {mods}\n\nVideo URI: <{uri}>\n\nComment: **`{comment}`**", inline=False)

        await ctx.send(embed=FSGembed)


@bot.command()
async def PB(ctx, string, str2):
    ssgpb = requests.get(f"https://www.speedrun.com/api/v1/users/{string}/personal-bests", params={"game": "j1npme6p"})
    if ssgpb.status_code == 200:
            range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            for i in range:
                seedtype = stdict[ssgpb.json()["data"][i]["run"]["values"]["r8rg67rn"]]
                if str2 == "SSG":
                    if seedtype == "SSG":
                        run = i
                        break
                if str2 == "RSG":
                    if seedtype == "RSG":
                        run = i
                        break

            rt = ssgpb.json()["data"][run]["run"]["times"]["realtime_t"]
            igt = ssgpb.json()["data"][run]["run"]["times"]["ingame_t"]

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



            date = ssgpb.json()["data"][run]["run"]["date"]
            comment = ssgpb.json()["data"][run]["run"]["comment"]


            version = vdict[ssgpb.json()["data"][run]["run"]["values"]["jlzkwql2"]]
            difficulty = diffidict[ssgpb.json()["data"][run]["run"]["values"]["9l737pn1"]]
            vrange = rangedict[ssgpb.json()["data"][run]["run"]["values"]["wl33kewl"]]
            f3 = f3dict[ssgpb.json()["data"][run]["run"]["values"]["ql6g2ow8"]]
            mods = modsdict[ssgpb.json()["data"][run]["run"]["values"]["dloymqd8"]]
            
            place = ssgpb.json()["data"][run]["place"]

            if seedtype == "SSG":
                colorvar = 0x73E089
            elif seedtype == "RSG":
                colorvar = 0x3598FB

        
            try:
                uri = ssgpb.json()["data"][run]["run"]["videos"]["links"][0]["uri"]
            except KeyError:
                uri = ssgpb.json()["data"][run]["run"]["videos"]["text"]
                
            SSGPBembed = discord.Embed(color = colorvar, title=f"{seedtype} PB:")
            SSGPBembed.add_field(name = f"Player: {string}", value = f"\n\nRTA: {rthr}:{rtmin}:{rtsec}.{rtms}\nIGT: {igthr}:{igtmin}:{igtsec}.{igtms}\nPlace: {place}\nDate: {date}\n\nVersion: {version}\nDifficulty: {difficulty}\nVersion Range: {vrange}\nF3: {f3}\nMods: {mods}\n\nVideo URI: <{uri}>\n\nComment: **`{comment}`**", inline=False)
            await ctx.send(embed=SSGPBembed)
    elif ssgpb.status_code == 404 or ssgpb.status_code == 420:
        await ctx.send("Unknown user name.")

@bot.command(name="?")
async def help(ctx):
    await ctx.send("```\nSSG WR\nRSG WR\nFSG WR\nPB [src-name]```")

bot.run(token)

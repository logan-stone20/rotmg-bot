from bs4 import BeautifulSoup
import requests


async def player_search(message):

    player_name = message.content.replace("?playersearch ", "")

    page_link = 'https://www.realmeye.com/player/' + player_name.strip()
    headers = {'User-Agent':'Mozilla/5.0'}

    print(page_link)
    print()

    page_response = requests.get(page_link, headers=headers)

    page_content = BeautifulSoup(page_response.text, "html.parser")

    if page_content is not None:
        stat_table = page_content.find("table", {"class": "summary"})
        if stat_table is not None:
            rows = stat_table.findAll("tr") 
            first_message = ""
            for row in rows:
                cols = row.findAll("td")
                first_message = first_message + (cols[0].text + ": " + cols[1].text) + "\n"

            await message.channel.send("```" + first_message + "```")
            characters_table = page_content.find("table", {"id": "e"})
            
            if characters_table is not None:
                tbody = characters_table.find("tbody")
                rows = tbody.findAll("tr")
                charCount = 0
                for row in rows:
                    charCount += 1
                    cols = row.findAll("td")
                    character = cols[2].text
                    level = cols[3].text
                    cqc = cols[4].text
                    fame = cols[5].text
                    exp = cols[6].text
                    place = cols[7].text
                    print()
                    print("Class: " + character +
                          "\nLevel: " + level +
                          "\nClass Quests Completed: " + cqc +
                          "\nFame: " + fame +
                          "\nExperience: " + exp +
                          "\nPlace: " + place)
        else:
            await message.channel.send("User not found.")

async def item_search(message):

    item_name = message.content[12:]
    item_name = item_name.replace(" ", "-")

    page_link = "https://www.realmeye.com/wiki/" + item_name.strip()
    headers = {'User-Agent':'Mozilla/5.0'}

    print(page_link)

    page_response = requests.get(page_link, headers = headers)

    page_content = BeautifulSoup(page_response.text, "html.parser")

    if page_content is not None:
        tables = page_content.findAll("div",{"class": "table-responsive"}).tr.td
        response = ""
        print(tables[0].text)
        #await message.channel.send("```" + response + "```")
        #await message.channel.send("For more info, visit " + page_link)

            

async def guild_search(message):

    guild_name = message.content.replace("?guildsearch ", "")
    guild_name = guild_name.replace(" ", "-")
    guild_name = guild_name.replace("'", "-")

    page_link = "https://www.realmeye.com/guild/" + guild_name
    headers = {'User-Agent':'Mozilla/5.0'}

    print(page_link)

    page_response = requests.get(page_link, headers = headers)

    page_content = BeautifulSoup(page_response.text, "html.parser")

    if page_content is not None:
        summary = page_content.find("table", {"class": "summary"})

        if summary is not None:

            rows = summary.findAll("tr")
            response = ""
            for row in rows:

                cols = row.findAll("td")
                response = response + cols[0].text + ": " + cols[1].text + "\n"

            await message.channel.send("```" + response + "```")

        else:
            await message.channel.send("Could not find page. Search is case sensitive.") 
            
        
    
    

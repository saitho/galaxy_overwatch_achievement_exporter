import json
import re
import requests

from lxml import etree

async def _get_achievements_html(username: str):
    url = f"https://playoverwatch.com/en-us/career/pc/{username.replace('#', '-')}"
    r = requests.get(url, {})
    return r.text


def _get_achievement_key(name: str):
    return re.sub('\W+', '', name.lower())


async def get_user_achievements(username: str):
    selector_achievements_all = "//*[contains(concat(' ', normalize-space(@class), ' '),' achievement-card-container ')]"

    player_data = await _get_achievements_html(username)
    root = etree.HTML(player_data)

    achievements = []
    selector_achievement_title = "//*[contains(concat(' ',normalize-space(@class),' '),' tooltip-tip ')]/h6/text()"
    selector_achievement_desc = "//*[contains(concat(' ',normalize-space(@class),' '),' tooltip-tip ')]/p/text()"
    selector_achievement_unlocked = "//*[contains(concat(' ',normalize-space(@class),' '),' media-card ')][not(contains(concat(' ',normalize-space(@class),' '),' m-disabled '))]"
    selector_achievement_img = "//img/@src"

    for achievement_tile in root.xpath(selector_achievements_all):
        achievement_dom = etree.HTML( etree.tostring(achievement_tile) )
        achievement_is_unlocked = len(achievement_dom.xpath(selector_achievement_unlocked)) > 0
        achievement_name = achievement_dom.xpath(selector_achievement_title)[0]
        achievement_description = achievement_dom.xpath(selector_achievement_desc)[0]
        achievement_image = achievement_dom.xpath(selector_achievement_img)[0]
        achievements.append({
            "name": achievement_name,
            "description": achievement_description,
            "api_key": _get_achievement_key(achievement_name),
            "image_url": achievement_image,
            "unlocked": achievement_is_unlocked
        })
    return achievements
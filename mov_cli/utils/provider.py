from fzf import fzf_prompt
from getpass import getuser

english = [
    "actvid",
    "sflix",
    "solar",
    "dopebox",
    "openloadmov",
]

german = [
    "kinox"
]

indian = [
    "streamblasters",
    "tamilyogi",
    "einthusan",
]

asian = [
    "viewasian",
    "watchasian",
]

anime = [
    "gogoanime",
    "animefox"
]

nsfw = [
    "hentaimama",
    "javct",
    "xxxmax",
    "pornhub",
]

tv = [
    "eja"
]

cartoons = [
    "kimcartoon"
]

turkish = [
    "turkish123"
]

sports = [
    "scdn"
]

update = [
    "pip install mov-cli"
]

inter = [
    "wlext",
]

preselction = {
    "English Providers": [english],
    "German Providers": [german],
    "Indian Providers": [indian],
    "Asian Providers": [asian],
    "18+ Providers": [nsfw],
    "LIVE TV Providers": [tv],
    "Cartoons Providers": [cartoons],
    "Turkish Providers": [turkish],
    "Anime Providers": [anime],
    "Sports Providers": [sports],
    "International Providers": [inter],
    "": [], f"Hi, {getuser()}" : [],
}

def ask():
    init = fzf_prompt(preselction)
    get = preselction.get(init)[0]
    choice = fzf_prompt(get)
    return choice



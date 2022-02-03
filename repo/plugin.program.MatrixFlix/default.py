# Module: default
# Author: MatrixFlix
# Created on: 03.02.2022
import sys
import xbmcplugin
import xbmcvfs
from urllib.parse import quote_plus, unquote_plus
import xbmcgui
import xbmc

artworkPath = xbmcvfs.translatePath
('special://home/addons/plugin.program.MatrixFlix/resources/media/')
fanart = artworkPath + "fanart.jpg"

def add_dir(name, url, mode, thumb):
    u = sys.argv[0] + "?url=" + quote_plus(url) + "&mode=" + str(mode) + "&name=" + quote_plus(name)
    liz = xbmcgui.ListItem(name)
    liz.setArt({'icon': thumb})
    liz.setProperty("fanart_image", fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok

def main_menu():
	add_dir("[COLOR cyan]Mise A Jour de MatrixFlix [/COLOR]", 'addon_maj', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR greenyellow]1 = -CHOISIR PACKS SKIN : ([COLOR orange]Sélectionner le pack souhaité[/COLOR])", 'light_light', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]LIGHT ([COLOR orange]le + leger[/COLOR])", 'light_light', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]FULL[/COLOR]", 'full_full', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]Rayflix[/COLOR]", ([COLOR orange]le skin de Rayflix[/COLOR])", 'full_perso', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]KIDS(LIGHT)[/COLOR]", 'light_kids', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]KIDS[/COLOR]", 'full_kids', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]SERIES[/COLOR] ([COLOR orange](LIGHT a venir)[/COLOR]", 'light_series', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]SERIES[/COLOR]", 'full_series', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]FILMS[/COLOR] ([COLOR orange](LIGHT a venir)[/COLOR]", 'light_films', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]FILMS[/COLOR] ([COLOR orange](a venir)[/COLOR]", 'full_films', 'call_save', artworkPath + 'icone.png')
	add_dir("[greenyellow]2: SAUVEGARDE ET RESTAURATION SKIN: [/COLOR]", 'skin_save1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR lime]Emplacement 1[/COLOR]", 'skin_save1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR lime]Emplacement 2[/COLOR]", 'skin_save2', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR lime]Emplacement 3[/COLOR]", 'skin_save3', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR springgreen]RESTAURER SKIN: [/COLOR]", 'skin_restor1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR springgreen]Emplacement 1[/COLOR]", 'skin_restor1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR springgreen]Emplacement 2[/COLOR]", 'skin_restor2', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR springgreen]Emplacement 3[/COLOR]", 'skin_restor3', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR greenyellow]3: Sélectionner les past souhaité[/COLOR] ([COLOR cyan](PREMIUM INTEGRE OU VIERGE:)[/COLOR]) ([COLOR orange]	Pensez a ajouter votre compte !			[/COLOR])", 'past_ray', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR gold]ALL Compte Integre 1[/COLOR]", 'cpt_all1', 'call_save', artworkPath + 'icone.png')	
	add_dir("[COLOR gold]ALL Compte Integre 2[/COLOR]", 'cpt_all2', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR gold]ALL VIERGE[/COLOR] ([COLOR orange]pensez a ajouter votre compte[/COLOR])", 'past_all', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR darkviolet]MASTER COMPTE PREMIUM Integre 1[/COLOR]", 'cpt_mst1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR darkviolet]MASTER COMPTE PREMIUM Integre 2[/COLOR]", 'cpt_mst2', 'call_save', artworkPath + 'icone.png')	
	add_dir("[COLOR darkviolet]MASTER VIERGE[/COLOR] ([COLOR orange]Ajouter votre compte[/COLOR])", 'past_master', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]CHOISIR PAST: [/COLOR]", 'past_ray', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]CHOISIR COMPTE PREMIUM: [/COLOR]", 'cpt_ray0', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 1[/COLOR]", 'cpt_ray1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 2[/COLOR]", 'cpt_ray2', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 3[/COLOR]", 'cpt_ray3', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 4[/COLOR]", 'cpt_ray4', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 5[/COLOR]", 'cpt_ray5', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 6[/COLOR]", 'cpt_ray6', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 7[/COLOR]", 'cpt_ray7', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 8[/COLOR]", 'cpt_ray8', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 9[/COLOR]", 'cpt_ray9', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 10[/COLOR]", 'cpt_ray10', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 11[/COLOR]", 'cpt_ray11', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 12[/COLOR]", 'cpt_ray12', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 13[/COLOR]", 'cpt_ray13', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 14[/COLOR]", 'cpt_ray14', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre 15[/COLOR]", 'cpt_ray15', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR red]NETTOYER KODI: -Vide le cache -les thumbnails et -les packages[/COLOR])", 'vider_cache', 'call_save', artworkPath + 'icone.png')
	
def callSave(url):
    plugins = __import__('resources.lib.' + url)
    function = getattr(plugins, "load")
    function()

def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params_l = sys.argv[2]
        cleanedparams = params_l.replace('?', '')
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    return param

params = get_params()

try:
    mode = unquote_plus(params["mode"])
except:
    mode = None

try:
    url = unquote_plus(params["url"])
except:
    pass

if mode is None:
    main_menu()

elif mode == 'call_save':
    callSave(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
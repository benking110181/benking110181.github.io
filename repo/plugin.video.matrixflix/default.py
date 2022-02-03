# Module: default
# Author: Arias800, Osmoze06, Rayflix
# Created on: 25.10.2021
import sys
import xbmcplugin
import xbmcvfs
from urllib.parse import quote_plus, unquote_plus
import xbmcgui
import xbmc

artworkPath = xbmcvfs.translatePath('special://home/addons/plugin.video.matrixflix/resources/media/')
fanart = artworkPath + "fanart.jpg"

def add_dir(name, url, mode, thumb):
    u = sys.argv[0] + "?url=" + quote_plus(url) + "&mode=" + str(mode) + "&name=" + quote_plus(name)
    liz = xbmcgui.ListItem(name)
    liz.setArt({'icon': thumb})
    liz.setProperty("fanart_image", fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok

def main_menu():
	add_dir("[COLOR magenta]Mise A Jour de MatrixFlix [/COLOR]", 'addon_maj', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR Transparent]1= Menu        [/COLOR] ([COLOR orange]Sélectionner le pack souhaité[/COLOR])", 'light_light', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]Light[/COLOR] ([COLOR orange]le + leger[/COLOR])", 'light_light', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]Full[/COLOR]", 'full_full', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]Rayflix[/COLOR] ([COLOR orange]le skin de Rayflix[/COLOR])", 'full_perso', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]Kids(LIGHT)[/COLOR]", 'light_kids', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]Kids[/COLOR]", 'full_kids', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]Séries[/COLOR] ([COLOR orange](Light a venir)[/COLOR]", 'light_series', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]Séries [/COLOR]", 'full_series', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]Films[/COLOR] ([COLOR orange](Light a venir)[/COLOR]", 'light_films', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]Films(Full)[/COLOR] ([COLOR orange](a venir)[/COLOR]", 'full_films', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR lime]2= Menu:		Sauvegarde & Restauration SKIN:	 [/COLOR]", 'skin_save1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR lime]Sauvegarde: 1[/COLOR]", 'skin_save1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR lime]Sauvegarde: 2[/COLOR]", 'skin_save2', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR lime]Sauvegarde: 3[/COLOR]", 'skin_save3', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR springgreen]RESTAURER SKIN:         [/COLOR]", 'skin_restor1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR springgreen]Restauration: 1[/COLOR]", 'skin_restor1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR springgreen]Restauration: 2[/COLOR]", 'skin_restor2', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR springgreen]Restauration: 3[/COLOR]", 'skin_restor3', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR Transparent]3= Menu: 	   [/COLOR]([COLOR cyan](Compte Premium intégré/:)[/COLOR]):", 'past_ray', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR gold](ALL) Compte Intégré: 1[/COLOR]", 'cpt_all1', 'call_save', artworkPath + 'icone.png')	
	add_dir("[COLOR gold](ALL) Compte Integre: 2[/COLOR]", 'cpt_all2', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR gold](ALL) Vierge[/COLOR] ([COLOR orange]pensez a ajouter votre compte[/COLOR])", 'past_all', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR darkviolet](MASTER) Compte PREMIUM Intégré: 1[/COLOR]", 'cpt_mst1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR darkviolet](MASTER) Compte PREMIUM Intégré: 2[/COLOR]", 'cpt_mst2', 'call_save', artworkPath + 'icone.png')	
	add_dir("[COLOR darkviolet](MASTER) Vierge[/COLOR] ([COLOR orange]Ajouter votre compte[/COLOR])", 'past_master', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR Transparent]Choisir Past Sauvegarder:(past_ray)[/COLOR]", 'past_ray', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]Choisir Compte PREMIUM: 0[/COLOR]", 'cpt_ray0', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 1[/COLOR]", 'cpt_ray1', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 2[/COLOR]", 'cpt_ray2', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 3[/COLOR]", 'cpt_ray3', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 4[/COLOR]", 'cpt_ray4', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 5[/COLOR]", 'cpt_ray5', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 6[/COLOR]", 'cpt_ray6', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 7[/COLOR]", 'cpt_ray7', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 8[/COLOR]", 'cpt_ray8', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 9[/COLOR]", 'cpt_ray9', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 10[/COLOR]", 'cpt_ray10', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 11[/COLOR]", 'cpt_ray11', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 12[/COLOR]", 'cpt_ray12', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 13[/COLOR]", 'cpt_ray13', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 14[/COLOR]", 'cpt_ray14', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR blueviolet]COMPTE PREMIUM Integre: 15[/COLOR]", 'cpt_ray15', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR Transparent]NETTOYER KODI:¤¤¤¤¤¤-Vide Le cache: -Les Thumbnails et -Les Packages !!!¤¤¤¤¤¤[/COLOR])", 'vider_cache', 'call_save', artworkPath + 'icone.png')
	
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
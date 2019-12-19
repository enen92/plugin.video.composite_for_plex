# -*- coding: utf-8 -*-
"""

    Copyright (C) 2018-2019 Composite (plugin.video.composite_for_plex)

    This file is part of Composite (plugin.video.composite_for_plex)

    SPDX-License-Identifier: GPL-2.0-or-later
    See LICENSES/GPL-2.0-or-later.txt for more information.
"""

from six import PY3

from kodi_six import xbmc  # pylint: disable=import-error

from .constants import CONFIG
from .logger import Logger

__LOG = Logger()

STRINGS = {
    # core
    'Delete': 117,
    'Refresh': 184,
    'Subtitles': 287,
    'Audio': 292,
    'Update library': 653,
    'Mark as watched': 16103,
    'Mark as unwatched': 16104,
    # add-on
    'Confirm file delete?': 30000,
    'Delete this item? This action will delete media and associated data files.': 30001,
    'Plex Online': 30002,
    'About to install': 30003,
    'This plugin is already installed': 30004,
    'Switch Failed': 30005,
    'Sign Out': 30006,
    'To sign out you must be logged in as an admin user. Switch user and try again': 30007,
    'myPlex': 30008,
    'You are currently signed into myPlex. Are you sure you want to sign out?': 30009,
    'You are not currently logged into myPlex. Continue to sign in, or cancel to return': 30011,
    'To access these screens you must be logged in as an admin user. '
    'Switch user and try again': 30012,
    'All': 30013,
    'Unwatched': 30014,
    'Recently Aired': 30015,
    'Recently Added': 30016,
    'Recently Viewed Episodes': 30017,
    'Recently Viewed Shows': 30018,
    'On Deck': 30019,
    'By Collection': 30020,
    'By First Letter': 30021,
    'By Genre': 30022,
    'By Year': 30023,
    'By Content Rating': 30024,
    'By Folder': 30025,
    'Search Shows...': 30026,
    'Search Episodes...': 30027,
    'By Album': 30029,
    'Search Artists...': 30035,
    'Search Albums...': 30036,
    'Search Tracks...': 30037,
    'Recently Released': 30040,
    'Recently Viewed': 30042,
    'By Decade': 30047,
    'By Director': 30048,
    'By Starring Actor': 30049,
    'By Country': 30050,
    'By Rating': 30052,
    'By Resolution': 30053,
    'Search...': 30056,
    'Camera Make': 30060,
    'Camera Model': 30061,
    'Aperture': 30062,
    'Shutter Speed': 30063,
    'ISO': 30064,
    'Lens': 30065,
    'Library refresh started': 30068,
    'myPlex not configured': 30069,
    'Select media to play': 30071,
    'Select subtitle': 30072,
    'Select audio': 30073,
    'Select master server': 30074,
    'Known server list': 30075,
    'Switch User': 30076,
    'Enter PIN': 30077,
    'myPlex Queue': 30080,
    'Sign In': 30081,
    'Display Servers': 30082,
    'Refresh Data': 30083,
    'Channels': 30084,
    'Playlists': 30085,
    'Play Transcoded': 30086,
    'All episodes': 30087,
    'Season': 30088,
    'Search for': 30089,
    'Unplayed': 30090,
    'Kids': 30589,
    'Teens': 30590,
    'Adults': 30591,
    'Manage myPlex': 30605,
    'Refresh library section': 30616,
    'Username:': 30617,
    'Password:': 30618,
    'Cancel': 30619,
    'Submit': 30620,
    'Manual': 30621,
    'Use PIN': 30622,
    'Done': 30623,
    'Unable to sign in': 30624,
    'From your computer, go to %s and enter the code below': 30625,
    'Successfully signed in': 30626,
    'Sign in not successful': 30627,
    'Email:': 30628,
    'Plex Pass:': 30629,
    'Joined:': 30630,
    'Exit': 30631,
    'Enter your myPlex details below': 30634,
    'Unknown': 30636,
    'myPlex Login': 30637,
    'Enter search term': 30638,
    'Enter value': 30639,
    'Transcode Profiles': 30641,
    'Offline': 30642,
    'Remote': 30643,
    'Nearby': 30644,
    'SSL': 30645,
    'Not Secure': 30646,
    'Message': 30648,
    'blank': 30649,
    'Server Discovery': 30650,
    'Please wait...': 30651,
    'myPlex discovery...': 30652,
    'GDM discovery...': 30653,
    'User provided...': 30654,
    'Caching results...': 30655,
    'Finished': 30656,
    'Found servers:': 30657,
    'No servers found': 30658,
    'installed': 30664,
    'Movies': 30665,
    'Music': 30666,
    'TV Shows': 30667,
    'Photos': 30668,
    'Go to': 30672,
    'Delete from the playlist?': 30673,
    'Confirm playlist item delete?': 30674,
    'Delete from playlist': 30675,
    'Select playlist': 30676,
    'Add to playlist': 30677,
    'Added to the playlist': 30678,
    'Failed to add to the playlist': 30679,
    'is already in the playlist': 30680,
    'has been removed the playlist': 30681,
    'Unable to remove from the playlist': 30682,
    'From your computer, go to [B]%s[/B] and enter the following code: [B]%s[/B]': 30690,
    'Widgets': 30692,
    'Clear Caches': 30694,
    'Movies on Deck': 30697,
    'TV Shows on Deck': 30698,
    'Recently Released Movies': 30699,
    'Recently Aired TV Shows': 30700,
    'Recently Added Movies': 30701,
    'Recently Added TV Shows': 30702,
    'Companion receiver is unable to start due to a port conflict': 30704,
    'Companion receiver has started': 30705,
    'Companion receiver has been stopped': 30706,
    'Create a playlist': 30722,
    'Enter a playlist title': 30723,
}


def decode_utf8(string):
    try:
        return string.decode('utf-8')
    except AttributeError:
        return string


def encode_utf8(string, py2_only=True):
    if py2_only and PY3:
        return string
    return string.encode('utf-8')


def i18n(string_id):
    mapped_string_id = STRINGS.get(string_id)
    if mapped_string_id:
        string_id = mapped_string_id

    try:
        core = int(string_id) < 30000
    except ValueError:
        __LOG.debug('Failed to map translation, returning id ...')
        return string_id

    if core:
        return encode_utf8(xbmc.getLocalizedString(string_id))

    return encode_utf8(CONFIG['addon'].getLocalizedString(string_id))


def directory_item_translate(title, thumb):  # pylint: disable=too-many-statements, too-many-branches
    translated_title = title

    if thumb.endswith('show.png'):
        if title == 'All Shows':
            translated_title = i18n('All')
        elif title == 'Unplayed':
            translated_title = i18n('Unplayed')
        elif title == 'Unwatched':
            translated_title = i18n('Unwatched')
        elif title == 'Recently Aired':
            translated_title = i18n('Recently Aired')
        elif title == 'Recently Added':
            translated_title = i18n('Recently Added')
        elif title == 'Recently Viewed Episodes':
            translated_title = i18n('Recently Viewed Episodes')
        elif title == 'Recently Viewed Shows':
            translated_title = i18n('Recently Viewed Shows')
        elif title == 'On Deck':
            translated_title = i18n('On Deck')
        elif title == 'By Collection':
            translated_title = i18n('By Collection')
        elif title == 'By First Letter':
            translated_title = i18n('By First Letter')
        elif title == 'By Genre':
            translated_title = i18n('By Genre')
        elif title == 'By Year':
            translated_title = i18n('By Year')
        elif title == 'By Content Rating':
            translated_title = i18n('By Content Rating')
        elif title == 'By Folder':
            translated_title = i18n('By Folder')
        elif title == 'Search Shows...':
            translated_title = i18n('Search Shows...')
        elif title == 'Search Episodes...':
            translated_title = i18n('Search Episodes...')

    if thumb.endswith('artist.png'):
        if title == 'All Artists':
            translated_title = i18n('All')
        elif title == 'By Album':
            translated_title = i18n('By Album')
        elif title == 'By Genre':
            translated_title = i18n('By Genre')
        elif title == 'By Year':
            translated_title = i18n('By Year')
        elif title == 'By Collection':
            translated_title = i18n('By Collection')
        elif title == 'Recently Added':
            translated_title = i18n('Recently Added')
        elif title == 'By Folder':
            translated_title = i18n('By Folder')
        elif title == 'Search Artists...':
            translated_title = i18n('Search Artists...')
        elif title == 'Search Albums...':
            translated_title = i18n('Search Albums...')
        elif title == 'Search Tracks...':
            translated_title = i18n('Search Tracks...')

    if thumb.endswith('movie.png') or thumb.endswith('video.png'):
        if title.startswith('All '):
            translated_title = i18n('All')
        elif title == 'Unplayed':
            translated_title = i18n('Unplayed')
        elif title == 'Unwatched':
            translated_title = i18n('Unwatched')
        elif title == 'Recently Released':
            translated_title = i18n('Recently Released')
        elif title == 'Recently Added':
            translated_title = i18n('Recently Added')
        elif title == 'Recently Viewed':
            translated_title = i18n('Recently Viewed')
        elif title == 'On Deck':
            translated_title = i18n('On Deck')
        elif title == 'By Collection':
            translated_title = i18n('By Collection')
        elif title == 'By Genre':
            translated_title = i18n('By Genre')
        elif title == 'By Year':
            translated_title = i18n('By Year')
        elif title == 'By Decade':
            translated_title = i18n('By Decade')
        elif title == 'By Director':
            translated_title = i18n('By Director')
        elif title == 'By Starring Actor':
            translated_title = i18n('By Starring Actor')
        elif title == 'By Country':
            translated_title = i18n('By Country')
        elif title == 'By Content Rating':
            translated_title = i18n('By Content Rating')
        elif title == 'By Rating':
            translated_title = i18n('By Rating')
        elif title == 'By Resolution':
            translated_title = i18n('By Resolution')
        elif title == 'By First Letter':
            translated_title = i18n('By First Letter')
        elif title == 'By Folder':
            translated_title = i18n('By Folder')
        elif title == 'Search...':
            translated_title = i18n('Search...')

    if thumb.endswith('photo.png'):
        if title == 'All Photos':
            translated_title = i18n('All')
        elif title == 'By Year':
            translated_title = i18n('By Year')
        elif title == 'Recently Added':
            translated_title = i18n('Recently Added')
        elif title == 'Camera Make':
            translated_title = i18n('Camera Make')
        elif title == 'Camera Model':
            translated_title = i18n('Camera Model')
        elif title == 'Aperture':
            translated_title = i18n('Aperture')
        elif title == 'Shutter Speed':
            translated_title = i18n('Shutter Speed')
        elif title == 'ISO':
            translated_title = i18n('ISO')
        elif title == 'Lens':
            translated_title = i18n('Lens')

    return translated_title


def item_translate(title, source, folder):
    translated_title = title

    if folder and source in ['tvshows', 'tvseasons']:
        if title == 'All episodes':
            translated_title = i18n('All episodes')
        elif title.startswith('Season '):
            translated_title = i18n('Season') + title[6:]

    return translated_title

# -*- coding: utf-8 -*-
"""

    Copyright (C) 2020 Composite (plugin.video.composite_for_plex)

    This file is part of Composite (plugin.video.composite_for_plex)

    SPDX-License-Identifier: GPL-2.0-or-later
    See LICENSES/GPL-2.0-or-later.txt for more information.
"""

import json
import re
import sys

from kodi_six import xbmc  # pylint: disable=import-error
from six.moves.urllib_parse import parse_qs

try:
    KODI_VERSION = int(xbmc.getInfoLabel('System.BuildVersion').split()[0].split('.')[0])
except:  # pylint: disable=bare-except
    KODI_VERSION = 0


def jsonrpc_request(query):
    response = xbmc.executeJSONRPC(json.dumps(query))
    payload = json.loads(response)
    return payload


def mark_movie_watched(movie_id):
    query = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "VideoLibrary.SetMovieDetails",
        "params": {
            "movieid": movie_id,
            "playcount": 1,
            "resume": {
                "position": 0.0
            }
        }
    }

    if KODI_VERSION < 18:
        del query['params']['resume']

    return jsonrpc_request(query)


def mark_episode_watched(episode_id):
    query = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "VideoLibrary.SetEpisodeDetails",
        "params": {
            "episodeid": episode_id,
            "playcount": 1,
            "resume": {
                "position": 0.0
            }
        }
    }

    if KODI_VERSION < 18:
        del query['params']['resume']

    return jsonrpc_request(query)


def mark_tvshow_watched(tvshow_id):
    query = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "VideoLibrary.SetTVShowDetails",
        "params": {
            "tvshowid": tvshow_id,
            "playcount": 1,
            "resume": {
                "position": 0.0
            }
        }
    }

    if KODI_VERSION < 18:
        del query['params']['resume']

    return jsonrpc_request(query)


if __name__ == '__main__':
    info_tag = sys.listitem.getVideoInfoTag()  # pylint: disable=no-member

    try:
        plugin_url = info_tag.getFilenameAndPath()
    except AttributeError:
        plugin_url = xbmc.getInfoLabel('ListItem.FileNameAndPath')

    params = parse_qs(plugin_url.split('?')[-1])
    plex_url = params.get('url', [''])[0]

    metadata_match = re.search('/metadata/(?P<metadata_id>[0-9]+)', plex_url)
    if metadata_match:
        metadata_id = metadata_match.group('metadata_id')
    else:
        metadata_id = [int(part) for part in plex_url.split('/') if part.isdigit()][-1]

    xbmc.executebuiltin('RunScript(plugin.video.composite_for_plex, watch, %s, %s, watch)' %
                        (plex_url, metadata_id))

    database_id = info_tag.getDbId()
    media_type = info_tag.getMediaType()

    if database_id and media_type:
        if media_type == 'movie':
            mark_movie_watched(database_id)
        elif media_type == 'tvshow':
            mark_tvshow_watched(database_id)
        elif media_type == 'episode':
            mark_episode_watched(database_id)

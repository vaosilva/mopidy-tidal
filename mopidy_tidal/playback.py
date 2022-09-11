from __future__ import unicode_literals

import logging

from mopidy import backend

logger = logging.getLogger(__name__)


class TidalPlaybackProvider(backend.PlaybackProvider):
    def translate_uri(self, uri):
        logger.info("TIDAL uri: %s", uri)
        parts = uri.split(":")
        track_id = int(parts[4])
        session = self.backend._session

        if hasattr(session, "get_media_url"):
            # tidalapi < 0.7.0
            newurl = session.get_media_url(track_id)
        else:
            # tidalapi >= 0.7.0
            newurl = session.track(track_id).get_url()

        logger.info("transformed into %s", newurl)
        return newurl

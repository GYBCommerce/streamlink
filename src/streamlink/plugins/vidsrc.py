import re
import streamlink.plugin
import streamlink.stream
from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.dash import DASHStream
from streamlink.stream.hls import HLSStream
import requests
from bs4 import BeautifulSoup

# https://vidsrc.me/embed/tt0396269/

@pluginmatcher(
    name="default",
    pattern=re.compile(r"https?://(?:www\.)?vidsrc\.me/embed/(?P<video_id>[^/]+)/?"),
)
class VidSrc(Plugin):
    url_re = re.compile(r"https?://(?:www\.)?vidsrc\.me/embed/(?P<video_id>[^/]+)/?$")

    @classmethod
    def can_handle_url(cls, url):
        return cls.url_re.match(url) is not None

    def _get_streams(self):
        response = requests.get(self.url)
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        iframe = soup.find("iframe")

        hls_url = f"https:{iframe.get('src')}"

        #return self.session.streams(self.url)
        return {"live": HLSStream(self.session, hls_url)}
        #return HLSStream.parse_variant_playlist(self.session, hls_url, headers={"Referer": self.url})


# Register the plugin
#streamlink.plugin.register_plugin(VidsrcPlugin)
__plugin__ = VidSrc

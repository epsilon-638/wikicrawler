from bs4 import BeautifulSoup
from dataclasses import dataclass
import requests as req
from request_headers import firefox_headers
import json
from typing import List


MEDIA_EXTS = [
    "jpg",
    "jpeg",
    "png",
    "pdf",
    "gif",
    "webp",
    "psd",
    "tiff",
    "svg",
    "hief",
    "indd",
    "raw",
]


@dataclass
class WikiContent:

    internal_links: List[str]
    external_links: List[str]
    internal_media: List[str]
    external_media: List[str]
    citations: List[str]


is_media = (lambda url:
    url.split(".")[-1].lower() in MEDIA_EXTS)


#is_internal_link = (lambda url:
#    True if
#        url.startswith('/') 
#        & (not url.startswith('//'))
#     else False)

is_internal = (lambda url:
    True if
        url.startswith('/')
        & (not url.startswith('//')) 
    else False)

is_external = (lambda url:
    True if
        url.startswith('http')
        | url.startswith('//')
    else False)

is_internal_link = (lambda url:
    True if
        is_internal(url)
        & (not is_media(url))
     else False)

is_external_link = (lambda url:
    True if
        is_external(url)
        & (not is_media(url))
     else False)

is_internal_media = (lambda url:
    True if
        is_internal(url) 
        & is_media(url)
     else False)

is_external_media = (lambda url:
    True if
        is_external(url) 
        & is_media(url)
     else False)

is_not_none = (lambda url:
    url != 'None')

is_citation = (lambda url:
    url.startswith('#'))

get_soup = (lambda response:
    BeautifulSoup(response, 'html.parser'))

get_body = (lambda soup:
    soup.find('div', class_="mw-content-ltr"))

process_response = (lambda response:
    get_body(get_soup(response)))

get_href = (lambda anchor:
    str(anchor.get('href')))

page_urls = (lambda content: 
    filter(is_not_none,
        map(get_href,
            content.find_all('a'))))

internal_links = (lambda urls:
    filter(is_internal_link, urls))

external_links = (lambda urls:
    filter(is_external_link, urls))

internal_media = (lambda urls:
    filter(is_internal_media, urls))

external_media = (lambda urls:
    filter(is_external_media, urls))

citations = (lambda urls: 
    filter(is_citation, urls))

get_wiki_content = (lambda soup: WikiContent(
    list(internal_links(page_urls(soup))),
    list(external_links(page_urls(soup))),
    list(internal_media(page_urls(soup))),
    list(external_media(page_urls(soup))),
    list(citations(page_urls(soup)))))

scrape_wiki = (lambda content:
    get_wiki_content(process_response(content)))

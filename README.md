AzLyricsAPI (http://www.azlyrics.com)
===========

These are a simple API for AzLyrics written in Python. Other functions will be added in future.
I didn't use other API or other services, this is from scratch.

Features
===

- Print lyrics in Terminal.
- Save lyrics in a .txt file.
- Print lyrics with a connected printer (alpha)

Roadmap
---

I would like to add other feature:

- Paste lyrics in web with the help of services like Pastebin, Google Docs and more.


Usage
====

<pre><code='python'>import api.azapi #If API's script is in '/api/azapi.py'.
api.azapi.generating(artist, title, save)</code></pre>

- 'artist' variable must be a <b>char</b> value.
- 'title' variable must be a <b>char</b> value.
- 'save' variable must be a <b>boolean</b> value.



#!/usr/bin/env python3
import urllib.request
import json


class GitHubRepoRelease:

    def __init__(self, repo):
        self.repo = repo
        url = f"https://api.github.com/repos/{repo}/releases/latest"
        self._resp_http = urllib.request.urlopen(url)
        self.release = json.load(self._resp_http)

    def download_urls(self, func=None):
        urls = [asset["browser_download_url"] for asset in self.release["assets"]]
        if func:
            urls = [url for url in urls if func(url)]
        return urls


if __name__ == '__main__':
    release = GitHubRepoRelease("cdr/code-server")
    url = release.download_urls(lambda url: "linux-x86_64" in url)[0]
    urllib.request.urlretrieve(url, "/tmp/code.tar.gz")

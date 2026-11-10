---
title: Navigate Chrome Browser Like a Pro Using Vimium
created: '2014-12-18T15:05:35-08:00'
date: '2026-11-09T20:23:37-08:00'
authors:
  - bendu
label: navigate-chrome-browser-like-a-pro-using-vimium
license: CC-BY-4.0
tags:
  - software
  - Chrome
  - Vimium
  - Vim
  - plugin
  - add-on
  - addon
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```{note}
There are apps for navigate any GUI applications (instead of just for browser).
See
[Navigate GUI Applications Without Mouse in Linux](navigate-gui-applications-without-mouse-in-linux)
for more discussions.
```

## Customize Key Mappings

1. Open Vimium Options.

1. Paste your customized key mappings into "Custom key mappings".
   Below is an example of my customized key mapping configuration.

   ```sh
   map d removeTab
   map u restoreTab
   unmap x
   unmap X
   map <c-d> scrollPageDown
   map <c-u> scrollPageUp
   map <c-f> scrollFullPageDown
   map <c-b> scrollFullPageUp
   ```

1. Click the "Save changes" button at the bottom-left corn.

## Save Failures with Large Settings

[GitLab issue #4986](https://gitlab.com/dclong/tasks/-/work_items/4986)
reports that adding an exclusion pattern may fail to save through either Vimium Options
("Save changes" or `Command+Enter` on macOS) or the toolbar popup.
The discussion identifies a likely cause: oversized settings exceeding Chrome's sync storage quota.
[Chrome's storage documentation](https://developer.chrome.com/docs/extensions/reference/api/storage#storage_areas)
lists limits of approximately 8 KB per item and 100 KB in total.

The issue's analysis says both interfaces use `Settings.setSettings()`,
which writes all non-default settings to `chrome.storage.sync`.
Too many exclusion patterns, or large custom key mappings, search-engine definitions,
or link-hint CSS, can therefore block saving even an unrelated change.
The failure may appear silent because the UI does not surface the storage error.

To investigate, open DevTools on the Vimium Options page
(`Command+Option+I` on macOS) and check the Console for storage errors such as
`QUOTA_BYTES_PER_ITEM`.
You can inspect current storage usage with:

```javascript
const settings = await chrome.storage.sync.get(null);
console.table(Object.entries(settings).map(([key, value]) => ({
  key,
  bytes: new Blob([key + JSON.stringify(value)]).size,
})));
console.log("Total bytes:", await chrome.storage.sync.getBytesInUse(null));
```

These values describe already stored settings; unsaved additions may exceed the quota.
If a quota error is confirmed, remove unnecessary exclusion rules or simplify the oversized
setting, save again, and reload Options to verify persistence.
If only the Options page fails, also look for validation errors in other fields,
which may be off-screen and prevent saving.

## Alternatives

- [Navigate GUI Applications Without Mouse in Linux](navigate-gui-applications-without-mouse-in-linux)

- [Anything better than SurfingKeys?](https://www.reddit.com/r/vim/comments/qbo35r/anything_better_than_surfingkeys/)

- [Surfingkeys @ GitHub](https://github.com/brookhong/Surfingkeys)

- [Tridactyl and Surfingkeys are Vimium on Steroids](https://devctrl.blog/posts/tridactyl-surfingkeys-vimium-on-steroids/)

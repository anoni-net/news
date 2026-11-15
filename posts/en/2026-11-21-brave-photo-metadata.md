---
title: The FBMD Identifier in Facebook Photos and Its Removal in Brave's Desktop Browser
description: From version 1.98, Brave's desktop browser automatically strips the FBMD identifier that Meta adds to Facebook photos whenever an image is saved or uploaded. Location, device and capture time are not removed, and as of 15 November the Android and iOS versions do not have the feature.
date: 2026-11-21T00:00:00+08:00
slug: brave-photo-metadata
categories: [tracking]
sources:
  - title: Brave removes tracking metadata from Instagram and Facebook photos
    url: https://brave.com/privacy-updates/40-remove-tracking-metadata/
    publisher: Brave
    date: 2026-11-12
  - title: Release Channel 1.98.60
    url: https://community.brave.app/t/release-channel-1-98-60/660299
    publisher: Brave
    date: 2026-10-27
  - title: Strip metadata from images on download/upload
    url: https://github.com/brave/brave-browser/issues/5238
    publisher: GitHub
    date: 2019-07-14
  - title: "IPTC investigates: what does Facebook do with your photo metadata?"
    url: https://iptc.org/news/what-does-facebook-do-with-your-photo-metadata/
    publisher: IPTC
    date: 2019-07-22
  - title: Social Media Sites Photo Metadata Test Results 2019
    url: https://iptc.org/standards/photo-metadata/social-media-sites-photo-metadata-test-results-2019/
    publisher: IPTC
  - title: Automatically delete personal EXIF data from images when uploading
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=743152
    publisher: Mozilla
    date: 2012-04-06
  - title: Is https://brave.com blocked in mainland China?
    url: https://en.greatfire.org/https/brave.com
    publisher: GreatFire
  - title: Is https://laptop-updates.brave.com blocked in mainland China?
    url: https://en.greatfire.org/https/laptop-updates.brave.com
    publisher: GreatFire
  - title: iTunes lookup API (cn)
    url: https://itunes.apple.com/lookup?id=1052879175&country=cn
    publisher: Apple
  - title: iTunes lookup API (tw)
    url: https://itunes.apple.com/lookup?id=1052879175&country=tw
    publisher: Apple
authors:
  - anoni-net
---

Brave announced on 12 November that, from version 1.98, its desktop browser automatically removes the `FBMD` identifier that Meta adds to Facebook photos whenever an image is saved or uploaded. People using Brave on desktop get the protection once they update. As of 15 November the Android and iOS versions do not have it, and the announcement describes them only as planned. A photo's location, device model and capture time are outside the scope of this change.

According to Brave's announcement, Meta stores the identifier in photo metadata (data attached to the file that is not normally visible) defined by the International Press Telecommunications Council (IPTC). The IPTC sets standards for the news industry, and photographers and publishers use its formats to embed captions, author names and copyright information in images.

When the IPTC tested how Facebook handles uploaded photos, it found that Facebook deleted most of the existing metadata and added a long string beginning with `FBMD` to the "Special Instructions" field. When someone else downloaded the same photo and uploaded it again, the value stayed the same. Brave repeated the test in July and found the identifier still there.

The announcement describes a hypothetical person who runs an Instagram account under a different name, kept apart from the real-name Facebook account that family and colleagues know. They use a separate email alias for each account, and maybe a VPN to hide their IP address. If they download an image a friend posted on Facebook urging people to vote and share it on their Instagram, the identifier travels with the file, and Meta could use it to link the Instagram account to the friend's post and the real-name network around it. Once that link exists, Meta might suggest the Instagram account to people who know them on Facebook, and the link could also leak or be handed over in response to a legal request.

Brave's announcement notes that Meta has not disclosed what the identifier is for or why it is placed in image metadata. The announcement also acknowledges that Meta may not use it for tracking, and states that without public information Brave weighs every possibility and its privacy implications. As of 15 November we could find no explanation from Meta about the identifier or about Brave's announcement, and no retest other than Brave's since the IPTC's 2019 round.

When an image is saved, Brave removes the identifier before the download finishes, so it does not come along if the file is later uploaded through another browser or app. When an image is uploaded to a website, Brave sends a stripped copy and leaves the original file on the computer unchanged. The feature appears in the release notes for version 1.98.60 on 27 October, and the corresponding request was opened on Brave's GitHub in 2019.

The title and first paragraph of Brave's announcement mention Instagram alongside Facebook, but the tests and demonstration steps in it all use Facebook photos. As of 15 November we found no independent test showing that Instagram photos also carry `FBMD`. In the IPTC's 2019 table of social media sites, the Instagram row records only that the site offers no way to save or download images and that no embedded metadata was displayed.

## Perspective {#perspective}

In both its 2016 and 2019 tests, the IPTC found two fields whose values differed from what was uploaded, and assumed Facebook had filled them in. The Job Id field got a new value with every upload, while the `FBMD` value in "Special Instructions" stayed the same when someone else uploaded the photo again. The IPTC states that it makes no assumptions about what these values are for, and in 2019 it could find no specification or statement from Facebook. Brave's announcement deals only with `FBMD` and does not mention Job Id, and the effect it describes is making it harder for Meta to link the same photo across accounts and sites, not preventing it altogether.

Other photo metadata has legitimate uses, such as photo apps sorting pictures by date and place. Brave lists removing location, device and date and time as features it would like to add later, and says users will decide when to remove them.

Brave uses Chrome as the comparison case without this protection. In 2012 someone filed a request in Firefox's bug tracker to delete EXIF data (the shooting details a camera writes into a photo) automatically on upload, and as of 15 November its status is WONTFIX. That request concerns EXIF, which is a different format from the IPTC field that holds `FBMD`.

People using Brave on desktop only need to update to 1.98 or later, and the announcement mentions no setting to turn on. The announcement includes steps to check. Save a photo from `facebook.com` in a browser such as Chrome, then open it in an image metadata viewer that runs in the browser, and the "Special Instructions" field shows a value beginning with `FBMD`. Open the same metadata viewer in Brave and choose the same file, and the value is gone.

When we checked on 20 October, GreatFire's last test in mainland China, on 18 October, had found `brave.com` 100% blocked, with interference recorded since 13 May 2017, and its most recent valid test of `laptop-updates.brave.com`, used for downloads and updates, was also blocked. On the same day, Apple's iTunes lookup API returned no Brave listing in the mainland China App Store (a lookup result, not an announcement of removal by Brave or Apple), while the Taiwan, Hong Kong, Japan, South Korea and Singapore stores listed Brave 1.96 (6 October). In none of those places does the App Store version bring this protection, since as of 15 November Brave has only announced plans for mobile.

Inferring from the two points at which the identifier is removed, saving and uploading, files that were neither downloaded nor uploaded through Brave on desktop are not protected, and neither are photos saved and shared through apps on a phone.

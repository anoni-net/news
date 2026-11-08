---
title: Unencrypted SD card inside a Lenovo fingerprint USB drive, and how to assess encryption claims
description: According to a researcher's slides, the Lenovo ThinkPlus FU100 fingerprint drive was marketed with hardware encryption and AES-256 but held an unencrypted SD card. Lenovo's statement says these products were sold by Lenovo only in mainland China and that affected customers can arrange a replacement. The statement does not address whether the AES-256 claim was accurate (checked on 8 November). For encrypted drives from other brands, the test is whether the key depends on the password.
date: 2026-11-15T00:00:00+08:00
slug: lenovo-fingerprint-usb
categories:
  - encryption
sources:
  - title: Breaking Encrypted USB Drives with Time-Travel Debugging
    url: https://github.com/xusheng6/breaking_encrypted_USB_drives_with_TTD/blob/main/Breaking_Encrypted_USB_Drives_v2.pdf
    publisher: RE//verse 2026
  - title: NVD-CVE-2025-13453
    url: https://nvd.nist.gov/vuln/detail/CVE-2025-13453
    publisher: NVD
    date: 2026-01-14
  - title: "Lenovo's 'encrypted' fingerprint USB drive is just an unencrypted SD card in a fancy case — AI-assisted follow-up finds a backdoor and hardcoded keys in other ‘secure’ USB products (updated)"
    url: https://www.tomshardware.com/tech-industry/cyber-security/lenovo-fingerprint-usb-stick-sold-as-aes-256-encrypted-had-a-plain-sd-card-inside-ai-assisted-follow-up-finds-a-backdoor-and-hardcoded-keys-in-other-secure-usb-products
    publisher: Tom's Hardware
    date: 2026-11-01
  - title: Lenovo ThinkPlus Fingerprint USB Drive Sold as Encrypted Was a Plain SD Card Inside
    url: https://hackingpassion.com/lenovo-thinkplus-encrypted-usb-sd-card/
    publisher: HackingPassion
    date: 2026-10-29
  - title: FIPS 140-2 Cerified Flash Drives Have Security Flaw
    url: https://spectrum.ieee.org/fips-1402-cerified-flash-drives-have-security-flaw
    publisher: IEEE Spectrum
    date: 2010-01-12
  - title: Cryptographic Module Validation Program
    url: https://csrc.nist.gov/projects/cryptographic-module-validation-program
    publisher: NIST
  - title: Header Key Derivation, Salt, and Iteration Count
    url: https://veracrypt.io/en/Header%20Key%20Derivation.html
    publisher: VeraCrypt
  - title: VeraCrypt Downloads
    url: https://veracrypt.io/en/Downloads.html
    publisher: VeraCrypt
  - title: BitLocker overview
    url: https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/
    publisher: Microsoft
  - title: BitLocker FAQ
    url: https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/faq
    publisher: Microsoft
  - title: Volume encryption with FileVault in macOS
    url: https://support.apple.com/guide/security/volume-encryption-with-filevault-sec4c6dc1b6e/web
    publisher: Apple
  - title: Encrypt and protect a storage device with a password in Disk Utility on Mac
    url: https://support.apple.com/guide/disk-utility/encrypt-protect-a-storage-device-password-dskutl35612/mac
    publisher: Apple
  - title: Frequently Asked Questions Cryptsetup/LUKS
    url: https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/FAQ.md
    publisher: cryptsetup
  - title: Personal Data Protection Act 2012
    url: https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=P16A-
    publisher: Singapore Statutes Online
authors:
  - anoni-net
---

A USB drive marketed as encrypted or fingerprint-locked does not necessarily hold encrypted files. In slides from the RE//verse reverse engineering conference in March 2026, a researcher took apart the Lenovo ThinkPlus FU100 fingerprint drive and concluded that the case held only an SD card and that the data had no encryption at all. According to a Lenovo statement carried by Tom's Hardware, these ThinkPlus storage products were designed for the China market and are only available from Lenovo in mainland China. The slides also list other affected devices, and the checks below apply equally to products from other brands that are advertised as encrypted.

The teardown and its conclusion both come from the slides, and what follows relies on their text and on accounts by Tom's Hardware and the security blog HackingPassion. One slide reads "It's just an SD card in a fancy case", and the fingerprint reader controls only the USB connection. As HackingPassion describes it, the fingerprint decides whether the drive connects to the computer, and the files on the card do not depend on it.

The "hardware encrypted" and AES-256 (a widely used encryption algorithm) claims appear on the FU100 introduction slide, with the image credited to Alibaba.com. As of 8 November we could not find an FU100 product page on Lenovo's website, so we cannot confirm whether Lenovo's own channels used the same wording.

According to the slides and HackingPassion, the researcher reported the problem to Lenovo on 2 August 2025. A temporary fix on 27 August 2025 added a layer of epoxy over the SD card, and a proper fix was scheduled for December 2025. Lenovo's statement says it worked with the researcher through coordinated disclosure after receiving the report, remediated the issues through hardware and software upgrades, and published a security advisory and three CVEs (public vulnerability identifiers) in January 2026.

The original page of Lenovo advisory `LEN-210545` returned Access Denied when we checked on 8 November, so we know its contents only through secondary sources and the US National Vulnerability Database (NVD). In the NVD record submitted by Lenovo, someone with physical access may be able to read data stored on the drive, and the affected products are the first generation of the ThinkPlus FU100, FU200, TU800 and TSD303.

According to HackingPassion and Tom's Hardware, the TSD303 external SSD covered in the same talk does encrypt its data, and its problem lay in password verification. The drive sent the correct password in plain text over USB to a program on the computer, which compared it with what the user typed. A first fix encrypted the password before sending it, but the key could be derived by the program, and a second fix in December 2025 moved the comparison onto the drive itself. In HackingPassion's summary of the slides, of ten devices built on the same software kit (vendor names blacked out on the slide), two stored data unencrypted on a micro SD card and eight had problems with how the password was sent.

Lenovo's statement does not address whether the AES-256 and hardware encryption claims were accurate, and it neither confirms nor denies that the SD card was unencrypted. According to HackingPassion, neither Lenovo nor the researcher mentions any attack on owners, and as of 8 November we had found no reported victims.

## Perspective {#perspective}

Fingerprint readers and password screens may control nothing more than the connection, and whether the data is protected depends on where the decryption key comes from. HackingPassion's summary gives two reliable designs: a key derived from the password through a deliberately slow function such as PBKDF2 or Argon2, so that each guess costs time, or verification carried out entirely inside the drive's own chip, with neither password nor key leaving it. According to the slides, the FU100's data is not encrypted, so it uses neither design (our inference).

In the versions the researcher tested, the software encryption tool from storage vendor Netac used a fixed AES-256 key written into the program, unrelated to the user's password (per Tom's Hardware and HackingPassion). Tom's Hardware also reports that Netac had not patched this by the time of the researcher's March 2026 talk. Software encryption is a different kind of case from the FU100's complete lack of encryption, but in both, an AES-256 label does not reveal where the key comes from (our generalization).

FIPS 140 (the US government standard for cryptographic modules) is administered through the Cryptographic Module Validation Program (CMVP) of the US National Institute of Standards and Technology (NIST), and modules are tested by independent laboratories. Certificates can be looked up on NIST's list, and according to NIST's page, FIPS 140-2 certificates move to the Historical List after 21 September 2026. IEEE Spectrum reported that the German security firm SySS published a way in December 2009 to bypass several FIPS 140-2 certified USB drives, recovering data within seconds regardless of the password. Citing GCN, IEEE Spectrum wrote that the preliminary analysis in a NIST press release at the time traced the problem to "the software authorizing decryption" rather than the certified cryptographic module, and that NIST was investigating whether the certification process needed changes.

As of 8 November we could not find any record of the FU100 passing FIPS 140 or China's commercial cryptography certification (the country's certification system for commercial cryptography products). HackingPassion advises treating a fingerprint reader or password screen on a drive as a lock on access, unless the maker shows that the key depends on it. Because NIST's preliminary analysis pointed to software, we infer that even after a certificate turns up, buyers still need the vendor to explain how keys are generated and where the password is verified.

People with any of the four first-generation devices listed in NVD can contact Lenovo Support to arrange a replacement, according to Lenovo's statement. HackingPassion reports that the free upgrade goes through a service line in China, with the device either sent back for replacement or given a firmware upgrade on site. Also according to HackingPassion, Lenovo advises backing up the data first and then wiping or formatting the device.

Lenovo's statement does not say whether units resold outside mainland China can be replaced. As of 8 November we could not find a record of the FU100 being sold through official channels in Hong Kong, Singapore or Taiwan, or rules in those places specific to labeling storage devices as encrypted. We could not confirm whether ordinary encrypted USB drives or SSDs fall within mainland China's commercial cryptography certification catalog.

Whether the data on a lost drive is actually encrypted can have legal consequences in Singapore. For organizations covered by the Personal Data Protection Act 2012, Part 6A treats the loss of a storage medium as a data breach where unauthorized access or similar handling of the personal data on it is likely, and under section 26D(5) an organization need not notify affected individuals of a notifiable breach if it had a technological measure in place beforehand that makes significant harm to them unlikely. We infer that encryption is the obvious candidate for such a measure, and that an organization relying on a drive like the FU100 could not count on the exception on the strength of the product's marketing.

Anyone storing sensitive files on a drive from another brand can encrypt them before copying them over, so that the key comes from a password they set (one of the options HackingPassion lists). VeraCrypt (open-source disk encryption software) lists Windows, macOS and Linux versions on its download page, and supports two key derivation methods, PBKDF2 and Argon2id, for non-system volumes and file containers. The cost is that every computer used to open the files must be able to run VeraCrypt.

Microsoft's documentation lists Windows Pro, Enterprise, Education and similar editions as able to enable BitLocker, and Home is not in the table. According to the BitLocker FAQ, BitLocker To Go covers USB flash drives and SD cards, and encrypted drives can be opened on another computer with a password. We could not find official documentation on whether Home can unlock an already encrypted drive.

Apple's security guide states that FileVault protects internal and removable storage devices, and Disk Utility can also encrypt an external device with a password when formatting it, which requires erasing the device first. LUKS (a disk encryption format common on Linux) processes passwords with PBKDF2 or Argon2, according to the cryptsetup FAQ, which also recommends backing up the LUKS header, since a damaged header can make the data impossible to decrypt. We could not find official documentation on whether macOS-encrypted external drives or LUKS volumes can be opened on other operating systems, so anyone who needs to move between computers should test this first.

Encrypting files yourself addresses a drive that is lost or taken by someone else, but it does not help if the computer itself is compromised, the password is too short, or the password is forgotten (our inference). A drive that holds only public material does not need this step, and anyone storing personal data or work documents can weigh it against the cost of needing the encryption software on every computer.

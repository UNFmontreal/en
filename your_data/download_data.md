---
title: "Download your MRI data"
date: 2020-10-18
description: >
  Retrieving your MRI data
---

## Requirements

To download your data you need __[an account](https://unf-montreal.ca/fr/documentation/welcome/account/)__ on the UNF servers.
You also need to know which group you belong to.

You have two different ways to retrieve your MRI data:
- Use a terminal (Linux, Mac)
- Use an SFTP client (Windows, Mac, Linux)

## Using the terminal (Mac, Linux, advanced Windows users)

Open a terminal and use the ssh command to retrieve your MRI data in a tar.gz archive. Replace the unf_login and path to your dicoms fields, as well as the destination tar.gz file.

- Download a folder and create a tar.gz archive

`ssh unf_login@elm.criugm.qc.ca tar czf - /path/to/your/dicom/ > destination_file_on_your_computer.tar.gz`

- Download a tar.gz archive

`rsync -azvL unf_login@elm.criugm.qc.ca:/unf/dicoms/by_groups_tar/path_to_your_dicoms destination_folder_on_your_computer`

## Using an SFTP client

### Installation

Filezilla is a software we recommend and it is available on all OS (Windows, Mac, Linux). You can download it by following this link __[Filezilla](https://filezilla-project.org/)__.

![Menu](/images/documentation/fr/download_mri/filezilla-menu.png)

### Configuration - first use

Start Filezilla and open the menu File -> Site Manager
You should see the following window:

![Configuration](/images/documentation/fr/download_mri/filezilla-config.png)

Create a new site that you can name __unf-dicom__ for example and fill in the different fields:

**Host**: elm.criugm.qc.ca

**Protocol**: SFTP-SSH File Transfer Protocol

**Login Type**: Interactive

**User**: this is the UNF username that was created for you when you made __[your account request](https://unf-montreal.ca/fr/documentation/welcome/account/)__.

Then click the *Connect* button.

You may see the following window appear:

![Certificate](/images/documentation/fr/download_mri/filezilla-trust.png)

Click on `Always trust` and click OK.

Finally Filezilla will ask for your UNF password as shown in the following window:

![password](/images/documentation/fr/download_mri/filezilla-password.png)

You are now connected to the UNF servers and you should see a similar window.

![Main window](/images/documentation/fr/download_mri/filezilla-main_window.png)

- Red: your file system on your computer.
- Blue: the file system on the server.
- Green: path used on the server

You can move files from right to left or vice versa to download and/or send data to the server.


## Access to your MRI data

Your MRI data can be located in 3 different places. Replace groupName with your group.

- `/unf/bids/groupName` if you requested/coordinated an automatic BIDS conversion
- `/unf/dicoms/by_groups_tar/groupName` if your data is relatively old (before 2016)
- `/unf/dicoms/by_groups/groupName` if your data was acquired more recently

If you would like help downloading your data, please do not hesitate to send an email to the following address: __[support.unf](mailto:support.unf@criugm.qc.ca?subject=Help-Download-MRI)__.
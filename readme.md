About
-----

A python http server for fast Unreal Tournament 2004 file uploads in LAN games.
Sets the LAN ip automatically.
Requires coping of all uploadable resources into same directory.


Requirements
------------

* UT2004
* Python 3


How to install
--------------

* cd ut2004
* mkdir shared && cd shared
* cp REPOFOLDER/*.py .
* copy all animation/map/etc files into shared folder
* change ut2004/system/ut2004.ini:
```
[IpDrv.HTTPDownload]
RedirectToURL=http://placeholder/
ProxyServerHost=
ProxyServerPort=80
UseCompression=False

[IpDrv.TcpNetDriver]
AllowDownloads=True
MaxDownloadSize=0
DownloadManagers=IpDrv.HTTPDownload
DownloadManagers=Engine.ChannelDownload
```

How to use
----------

* frist run fileserver.py
* then ut2004

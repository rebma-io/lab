# Octoprint

To manage and allow for web access to my [3D printer](prusa.md) I am
running [Octoprint](https://octoprint.org/) on a cheap Intel Celeron N5105-based
micro machine that picked up on
[AliExpress](https://www.aliexpress.us/item/3256802565230576.html) for less than
the going rate of a decent Raspberry Pi with a case and power supply.

## Running on Ubuntu

Since I don't run the Octoprint Raspberry Pi distribution, I had to get
everything set up myself. 

### Software Installation

I created an Octoprint user (`octoprint`) so that everything could run under a
non-privileged user. Their home is `/home/octoprint` and the software is
installed into a Python
[virtualenv](https://docs.python.org/3/library/venv.html). 

I have `systemd` managing Octoprint as a [service
unit](https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files)
in `/etc/systemd/system/octoprint.service`:

```ini
[Unit]
Description=Octoprint
After=network.target

[Service]
ExecStart=/home/octoprint/octoprint/bin/octoprint serve
WorkingDirectory=/home/octoprint/octoprint
StandardOutput=inherit
StandardError=inherit
Restart=always
User=octoprint
CPUSchedulingPolicy=rr
CPUSchedulingPriority=80

[Install]
WantedBy=multi-user.target
```

I set `CPUSchedulingPriority` to be relatively high to ensure that there's never
a blip in the gcode flow between it and the printer.

Once you put that in place, you can enable them:

```console
$ sudo systemctl enable octoprint
$ sudo systemctl start octoprint
$ systemctl status octoprint
● octoprint.service - Octoprint
     Loaded: loaded (/etc/systemd/system/octoprint.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2023-06-09 21:56:00 PDT; 2 days ago
   Main PID: 883 (octoprint)
      Tasks: 37 (limit: 9138)
     Memory: 1.5G
        CPU: 57min 19.305s
     CGroup: /system.slice/octoprint.service
             └─883 /home/octoprint/octoprint/bin/python3 /home/octoprint/octoprint/bin/octoprint serve
```

### Webcam

DANGER: Do not leave your 3D printer unattended and leave your house. 

One of the great things about Octoprint is being able to integrate a webcam into
your workflow. This can give you both real-time view of what's going on, but
also, using [Octolapse](https://plugins.octoprint.org/plugins/octolapse/),
generate timelapses of the print and save them for review. 

To get it running on the Ubuntu distribution, I unfortunately had to use a Snap
distribution for the [mjpg-streamer](https://snapcraft.io/mjpg-streamer) tool
that is used. I'm sure I could have gotten it running otherwise, but after a few
false starts, I just called "done" and kept moving.

Like Octoprint itself, I have systemd managing the software. I used the
following unit file in `/etc/systemd/system/mjpg-streamer.service`.

```ini
[Unit]
Description=Motion JPEG Streamer
After=network.target

[Service]
ExecStart=/snap/bin/mjpg-streamer -i "input_uvc.so -r 1920x1080 -f 30" -o "output_http.so -w /var/snap/mjpg-streamer/current/www/"
WorkingDirectory=/tmp
StandardOutput=inherit
StandardError=inherit
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

Finally, like with Octoprint, you can enable and start it:

```console
$ sudo systemctl enable mjpg-streamer
$ sudo systemctl start mjpg-streamer
$ systemctl status mjpg-streamer
● mjpg-streamer.service - Motion JPEG Streamer
     Loaded: loaded (/etc/systemd/system/mjpg-streamer.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2023-06-09 21:56:00 PDT; 2 days ago
   Main PID: 882 (mjpg-streamer.s)
      Tasks: 0 (limit: 9138)
     Memory: 12.9M
        CPU: 913ms
     CGroup: /system.slice/mjpg-streamer.service
             ‣ 882 /bin/sh /snap/mjpg-streamer/42/bin/mjpg-streamer.sh -i "input_uvc.so -r 1920x1080 -f 30" -o "output_>
```

### Plugins

I have found these plugins to Octoprint, among the many hundreds, to be
especially useful.

* [Bed Visualizer](https://plugins.octoprint.org/plugins/bedlevelvisualizer/)
* [Cost Estimation](https://plugins.octoprint.org/plugins/costestimation/)
* [Display Layer Progress](https://plugins.octoprint.org/plugins/DisplayLayerProgress/)
* [Exclude Region](https://plugins.octoprint.org/plugins/excluderegion/)
* [Heater Timeout](https://plugins.octoprint.org/plugins/HeaterTimeout/)
* [Octolapse](https://plugins.octoprint.org/plugins/octolapse/)
* [OctoPod](https://plugins.octoprint.org/plugins/octopod/). Integrates with the
  iOS app
  [OctoPod](https://apps.apple.com/us/app/octopod-for-octoprint/id1412557625)
  that gives you real-time access to your printer over your iOS device. It can
  even work on AppleTV.
* [Print Job History](https://plugins.octoprint.org/plugins/PrintJobHistory/)
* [PrintTimeGenius](https://plugins.octoprint.org/plugins/PrintTimeGenius/)
* [Simple Emergency Stop](https://plugins.octoprint.org/plugins/simpleemergencystop/)
* [Spool Manager](https://plugins.octoprint.org/plugins/SpoolManager/)

## Access Anywhere via Tailscale

TODO: Discuss how to use Tailscale to access Octoprint from anywhere.
Maybe this belongs in a whole new section for "Linuxy things"?
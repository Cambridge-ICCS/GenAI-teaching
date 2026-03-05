magick images/Cambridge_uni_logo.png -resize x500 /tmp/cam.png
magick images/Full_logo.png -resize x500 /tmp/iccs.png
magick /tmp/cam.png /tmp/iccs.png +append -background none images/combined_logo.png

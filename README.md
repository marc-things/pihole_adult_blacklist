# pihole_adult_blacklist

The purpose of this script is to automate adding domains to the pi-hole blacklist.

The script goes through the following steps:

1. downloads the adult blacklist tar.gz file from http://dsi.ut-capitole.fr/blacklists/index_en.php
2. extracts the contents of the tar.gz
3. runs the pihole -b shell command on each line from the domains file that was extracted

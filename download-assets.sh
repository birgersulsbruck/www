#!/usr/bin/env bash
# download-assets.sh
# Downloader alle billeder fra det gamle birgersulsbruck.com til ./assets/
# og omskriver *.dc.html til at bruge de lokale filer (klar til et GitHub-repo).
#
# Brug:        ./download-assets.sh
# Med lydzip:  ./download-assets.sh --with-zip   (henter ogsaa LPCD_2014new.zip, 133 MB)
#
# Koer scriptet fra mappen med .dc.html-filerne. Kraever: curl, perl.
set -euo pipefail

BASE="http://www.birgersulsbruck.com"
PATHS=(
  "Books_CDs_files/C_T_LOGO_LOW.jpg"
  "Books_CDs_files/Conga_bog.jpg"
  "Books_CDs_files/LatPerc_bog.jpg"
  "Books_CDs_files/PALfoto.jpg"
  "Books_CDs_files/PALtitel%20kopi.gif"
  "Books_CDs_files/SalsaSesWeb.jpg"
  "Books_CDs_files/The_Little_Frontpage_LOW.jpg"
  "Books_CDs_files/VideoFoto.jpg"
  "Books_CDs_files/mwmac.png"
  "Books_CDs_files/shapeimage_1.jpg"
  "Download_files/mwmac.png"
  "Download_files/shapeimage_1.jpg"
  "Info_files/BS-med-No_LOW.jpg"
  "Info_files/BS_1977-80_LOW.jpg"
  "Info_files/BS_1984_Jamboree_LOW.jpg"
  "Info_files/BS_Naestv_1_LOW.jpg"
  "Info_files/BS_PJ25_1_LOW.jpg"
  "Info_files/BS_Simone_12_LOW.jpg"
  "Info_files/BobbyWatson_Advance.jpg"
  "Info_files/Cox-Montmartre_LOW.jpg"
  "Info_files/DRSO_2010_1_LOW.jpg"
  "Info_files/K%26C%20paa%20Viften_12jpg%20kopi.jpg"
  "Info_files/K%26C_booklet_LOW.jpg"
  "Info_files/SNM_CDweb.jpg"
  "Info_files/mwmac.png"
  "Info_files/shapeimage_1.jpg"
  "News_files/2002_cubateam_LOW.jpg"
  "News_files/2013_Guerilla1_LOW.jpg"
  "News_files/2013_TivoliBB_Bobo_LOW.jpg"
  "News_files/BS_2013_PJ-clinic_LOW.jpg"
  "News_files/BS_Naestv_2_MLow.jpg"
  "News_files/BS_Simone_12_LOW.jpg"
  "News_files/Coco_PJ30_5_LOW.jpg"
  "News_files/DRBB_AmBio1_Low.jpg"
  "News_files/DRSO_2010_1_LOW.jpg"
  "News_files/DaveH_12_2_Low.jpg"
  "News_files/DoP1_13_1A_KLow.jpg"
  "News_files/DoP1_13_1_LOW.jpg"
  "News_files/K%26C_Horsh_1.jpg"
  "News_files/MoryK_Istanbul_08_LOW.jpg"
  "News_files/SNM_Odense_2.jpg"
  "News_files/The_Little_Frontpage_LOW.jpg"
  "News_files/mwmac.png"
  "News_files/shapeimage_1.jpg"
  "Photos_files/mwmac.png"
  "Photos_files/shapeimage_1.jpg"
  "Reviews_files/5Hour_1985.jpg"
  "Reviews_files/5Hours_1987_LOW.jpg"
  "Reviews_files/Congress_96_LOW-filtered.jpg"
  "Reviews_files/IntJazzWork_84_LOW.jpg"
  "Reviews_files/JazzGrooves_LOW.jpg"
  "Reviews_files/JazzWorks85_LOW.jpg"
  "Reviews_files/Leverkus_93_LOW-filtered.jpg"
  "Reviews_files/MONT_feb86_LOW-filtered.jpg"
  "Reviews_files/Muff%20annonce.jpg"
  "Reviews_files/SNM_Koeln_posterWeb%20kopi.jpg"
  "Reviews_files/SNM_VanVan_LOW.jpg"
  "Reviews_files/TrondheimFest02_LOW.jpg"
  "Reviews_files/VadsoePoster_95_low-filtered.jpg"
  "Reviews_files/Voss_Frikk_1982_LOW.jpg"
  "Reviews_files/Voss_front_82_LOW.jpg"
  "Reviews_files/W_W_festival86.jpg"
  "Reviews_files/W_W_festival86_LOW.jpg"
  "Reviews_files/mwmac.png"
  "Reviews_files/shapeimage_1.jpg"
  "Seminars_files/mwmac.png"
  "Seminars_files/shapeimage_1.jpg"
  "Welcome_files/BSLogo2%20kopi.gif"
  "Welcome_files/Forside_engl.png"
  "Welcome_files/mwmac.png"
  "Welcome_files/shapeimage_1.jpg"
)

echo "Henter ${#PATHS[@]} billeder..."
for p in "${PATHS[@]}"; do
  out="assets/$p"
  mkdir -p "$(dirname "$out")"
  if [ ! -s "$out" ]; then
    echo "  $p"
    curl -fsSL "$BASE/$p" -o "$out" || echo "  !! FEJL: $p (spring over)"
  fi
done

if [ "${1:-}" = "--with-zip" ]; then
  echo "Henter LPCD_2014new.zip (133 MB)..."
  mkdir -p assets/Download_files
  curl -fSL "$BASE/Download_files/LPCD_2014new.zip" -o assets/Download_files/LPCD_2014new.zip
fi

echo "Omskriver HTML-filer til lokale stier..."
for p in "${PATHS[@]}"; do
  proxied="https://images.weserv.nl/?url=www.birgersulsbruck.com/${p//%/%25}"
  perl -pi -e "s{\\Q$proxied\\E}{assets/$p}g" *.dc.html
done
# Zip-linket peger paa lokal fil, hvis den er hentet
if [ -s assets/Download_files/LPCD_2014new.zip ]; then
  perl -pi -e 's{http://www\.birgersulsbruck\.com/Download_files/LPCD_2014new\.zip}{assets/Download_files/LPCD_2014new.zip}g' *.dc.html
fi

echo "Faerdig. Billederne ligger i ./assets/ og siderne peger nu paa dem."
echo "Konsolider i git med: git add assets *.dc.html support.js && git commit -m 'Konsolider billeder lokalt'"

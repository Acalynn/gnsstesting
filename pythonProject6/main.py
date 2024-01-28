# python 2.7
# pip install git+https://github.com/GNSSpy-Project/gnsspy
# pip install pyunpack

import gnsspy as gp
station = gp.read_obsFile("rinex/THCM021o45.obs")
readNav = gp.read_navFile("rinex/THCM021o45_gps.nav")

print(station)
print("------------------------")
print(station.observation)
print("------------------------")
print(station.epoch)
print("------------------------")
print(station.version)

print(">>>>>>>>>>> NAV <<<<<<<<<")
print(readNav.navigation)
print(readNav.epoch)

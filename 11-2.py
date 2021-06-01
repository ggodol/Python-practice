"""
11-2 패키지
https://youtu.be/kWiCuklohdY?t=19450

예제를 위해 travel 폴더 생성
"""
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to2 = vietnam.VietnamPackage()
trip_to2.detail()
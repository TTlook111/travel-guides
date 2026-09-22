import urllib.request
import os
import ssl

# 忽略SSL证书验证
ssl._create_default_https_context = ssl._create_unverified_context

assets_dir = r"E:\projects\景色\jiuzhaigou-guide\assets"

images = {
    # Hero - 五花海秋季全景
    "hero_wuhuahai_autumn.jpg": "https://aka.doubaocdn.com/s/xQUW2OjEff",
    # 五花海
    "wuhuahai_spring.jpg": "https://aka.doubaocdn.com/s/RcXHHGiCTh",
    "wuhuahai_underwater.jpg": "https://aka.doubaocdn.com/s/IjkQ9x1RJm",
    "wuhuahai_summer.jpg": "https://aka.doubaocdn.com/s/pihh2Xy8GF",
    "wuhuahai_autumn2.jpg": "https://aka.doubaocdn.com/s/GInJ3pl1PL",
    "wuhuahai_autumn3.jpg": "https://aka.doubaocdn.com/s/5FeWdQHOrH",
    # 秋季彩林
    "autumn_forest_lake1.jpg": "https://aka.doubaocdn.com/s/X0iSddDkmS",
    "autumn_forest_lake2.jpg": "https://aka.doubaocdn.com/s/XNeMf7yT48",
    "autumn_jinlinghai1.jpg": "https://aka.doubaocdn.com/s/hpHAP36Yxn",
    "autumn_jinlinghai2.jpg": "https://aka.doubaocdn.com/s/HhthUehmIT",
    "autumn_reflection.jpg": "https://aka.doubaocdn.com/s/6hCiys5rMo",
    "autumn_aerial.jpg": "https://aka.doubaocdn.com/s/rUQnHrwJZC",
    # 冬季雪景
    "winter_forest1.jpg": "https://aka.doubaocdn.com/s/8vHiM4atV6",
    "winter_valley.jpg": "https://aka.doubaocdn.com/s/xBsDFBdaFo",
    "winter_snow_lake.jpg": "https://aka.doubaocdn.com/s/l1pXFHDEoJ",
    "winter_blue_lake.jpg": "https://aka.doubaocdn.com/s/qdOJ9BnbX5",
    "winter_snow_mountain.jpg": "https://aka.doubaocdn.com/s/j0RZ5nVWWw",
    "winter_lake_mist.jpg": "https://aka.doubaocdn.com/s/jgynW3vhVU",
    # 诺日朗瀑布
    "nuorilang_waterfall1.jpg": "https://aka.doubaocdn.com/s/ILRMy0EeR8",
    "nuorilang_waterfall2.jpg": "https://aka.doubaocdn.com/s/OjBWARwcg1",
    "nuorilang_autumn.jpg": "https://aka.doubaocdn.com/s/d8jsQEEAOh",
    "nuorilang_summer.jpg": "https://aka.doubaocdn.com/s/SDk2NxfsEc",
    # 五彩池
    "wucaichi_summer.jpg": "https://aka.doubaocdn.com/s/zt4MXDGaY0",
    "wucaichi_winter.jpg": "https://aka.doubaocdn.com/s/6rg2QKMM4z",
    "wucaichi_portrait.jpg": "https://aka.doubaocdn.com/s/svhkoB5Mia",
    "wucaichi_panorama.jpg": "https://aka.doubaocdn.com/s/TunVbJebLt",
    # 珍珠滩瀑布
    "zhenzhutan1.jpg": "https://aka.doubaocdn.com/s/UHJFwXDxUC",
    "zhenzhutan2.jpg": "https://aka.doubaocdn.com/s/Vywd2zVl1d",
    "zhenzhutan3.jpg": "https://aka.doubaocdn.com/s/qqMHVUmkjP",
    "zhenzhutan4.jpg": "https://aka.doubaocdn.com/s/7Hsmq0sZCA",
    # 春季
    "spring_peach_lake.jpg": "https://aka.doubaocdn.com/s/3bb9CrwvgM",
    "spring_peach_snow.jpg": "https://aka.doubaocdn.com/s/2ztUOV23aj",
    "spring_wild_peach.jpg": "https://aka.doubaocdn.com/s/Rlg0Lch11U",
    "spring_peach_branch.jpg": "https://aka.doubaocdn.com/s/qewHVrcKXk",
    # 夏季
    "summer_cuihai.jpg": "https://aka.doubaocdn.com/s/NbWSTFuxYV",
    "summer_reflection.jpg": "https://aka.doubaocdn.com/s/ZuJOkmxnJj",
    "summer_valley.jpg": "https://aka.doubaocdn.com/s/UN3XDueqZn",
    "summer_mirror_lake.jpg": "https://aka.doubaocdn.com/s/oXLBZDl9OU",
}

success = 0
failed = 0
for filename, url in images.items():
    filepath = os.path.join(assets_dir, filename)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        with open(filepath, "wb") as f:
            f.write(data)
        size_kb = len(data) / 1024
        print(f"OK: {filename} ({size_kb:.0f} KB)")
        success += 1
    except Exception as e:
        print(f"FAIL: {filename} - {e}")
        failed += 1

print(f"\nDone: {success} success, {failed} failed")

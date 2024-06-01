import aiohttp
import asyncio
from utils.tools import (
    search_github, search_twitter, search_instagram, search_facebook, search_linkedin,
    search_reddit, search_tiktok, search_snapchat, search_pinterest, search_whatsapp,
    search_telegram, search_youtube, search_messenger, search_wechat, search_qq,
    search_sina_weibo, search_qzone, search_douyin, search_kuaishou
)

async def fetch_status(session, url):
    async with session.get(url) as response:
        return response.status

async def search_platform(session, username, platform_url):
    url = platform_url.format(username=username)
    status = await fetch_status(session, url)
    if status == 200:
        return url
    else:
        return None

async def search_username(username):
    print("Searching...")

    async with aiohttp.ClientSession() as session:
        tasks = {
            'GitHub': search_github(session, username),
            'Twitter': search_twitter(session, username),
            'Instagram': search_instagram(session, username),
            'Facebook': search_facebook(session, username),
            'LinkedIn': search_linkedin(session, username),
            'Reddit': search_reddit(session, username),
            'TikTok': search_tiktok(session, username),
            'Snapchat': search_snapchat(session, username),
            'Pinterest': search_pinterest(session, username),
            'WhatsApp': search_whatsapp(session, username),
            'Telegram': search_telegram(session, username),
            'YouTube': search_youtube(session, username),
            'Messenger': search_messenger(session, username),
            'WeChat / Weixin': search_wechat(session, username),
            'QQ': search_qq(session, username),
            'Sina Weibo': search_sina_weibo(session, username),
            'Qzone': search_qzone(session, username),
            'Douyin': search_douyin(session, username),
            'Kuaishou': search_kuaishou(session, username)
        }

        results = await asyncio.gather(*tasks.values())
        result_dict = dict(zip(tasks.keys(), results))

        print("\nRésulats de recherche:")
        for platform, url in result_dict.items():
            if url:
                print(f" - {platform}: {url}")
            else:
                print(f" - {platform}: Profil non trouvé")

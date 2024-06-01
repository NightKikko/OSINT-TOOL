import aiohttp
import asyncio

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

async def search_github(session, username):
    return await search_platform(session, username, "https://github.com/{username}")

async def search_twitter(session, username):
    return await search_platform(session, username, "https://twitter.com/{username}")

async def search_instagram(session, username):
    return await search_platform(session, username, "https://www.instagram.com/{username}")

async def search_facebook(session, username):
    return await search_platform(session, username, "https://www.facebook.com/{username}")

async def search_linkedin(session, username):
    return await search_platform(session, username, "https://www.linkedin.com/in/{username}")

async def search_reddit(session, username):
    return await search_platform(session, username, "https://www.reddit.com/user/{username}")

async def search_tiktok(session, username):
    return await search_platform(session, username, "https://www.tiktok.com/@{username}")

async def search_snapchat(session, username):
    return await search_platform(session, username, "https://www.snapchat.com/add/{username}")

async def search_pinterest(session, username):
    return await search_platform(session, username, "https://www.pinterest.com/{username}")

async def search_whatsapp(session, username):
    return await search_platform(session, username, "https://wa.me/{username}")

async def search_telegram(session, username):
    return await search_platform(session, username, "https://t.me/{username}")

async def search_youtube(session, username):
    return await search_platform(session, username, "https://www.youtube.com/{username}")

async def search_messenger(session, username):
    return await search_platform(session, username, "https://www.messenger.com/{username}")

async def search_wechat(session, username):
    return await search_platform(session, username, "https://www.wechat.com/{username}")

async def search_qq(session, username):
    return await search_platform(session, username, "https://www.qq.com/{username}")

async def search_sina_weibo(session, username):
    return await search_platform(session, username, "https://www.weibo.com/{username}")

async def search_qzone(session, username):
    return await search_platform(session, username, "https://www.qzone.com/{username}")

async def search_douyin(session, username):
    return await search_platform(session, username, "https://www.douyin.com/{username}")

async def search_kuaishou(session, username):
    return await search_platform(session, username, "https://www.kuaishou.com/{username}")

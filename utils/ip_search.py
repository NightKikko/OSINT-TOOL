import aiohttp
import asyncio
from colorama import Fore, Style

async def search_ip():
    ip_address = input("$ Enter IP Address: ")
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://ip-api.com/json/{ip_address}') as response:
            if response.status == 200:
                data = await response.json()
                print(Fore.GREEN + "    IP Address Information:")
                print(Fore.GREEN + f"    IP Address: {data['query']}")
                print(Fore.GREEN + f"    Country: {data['country']}")
                print(Fore.GREEN + f"    City: {data['city']}")
                print(Fore.GREEN + f"    Region: {data['regionName']}")
                print(Fore.GREEN + f"    Zip Code: {data['zip']}")
                print(Fore.GREEN + f"    Latitude: {data['lat']}")
                print(Fore.GREEN + f"    Longitude: {data['lon']}")
                print(Fore.GREEN + f"    Timezone: {data['timezone']}")
                print(Fore.GREEN + f"    Internet Service Provider: {data['isp']}")
                print(Fore.GREEN + f"    Organization: {data['org']}")
                print(Fore.GREEN + f"    AS (Autonomous System): {data['as']}")
                if 'asname' in data:
                    print(Fore.GREEN + f"    AS Name: {data['asname']}")
                else:
                    print(Fore.GREEN + " AS Name: Not available")

                print(Style.RESET_ALL)
            else:
                print(Fore.RED + f"[!] Failed to retrieve information for IP: {ip_address}")
                print(Style.RESET_ALL)

if __name__ == "__main__":
    asyncio.run(search_ip())

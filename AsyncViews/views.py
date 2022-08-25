import asyncio
import httpx
import time
from django.http import HttpResponse, JsonResponse


async def http_call_async():
  for i in range(6):
    await asyncio.sleep(1)
    print(i)
  
  async with httpx.AsyncClient() as client:
    res = await client.get('https://ebaconline.com.br')
    print(res)


async def async_view(request):
  loop = asyncio.get_event_loop()
  loop.create_task(http_call_async())
  return JsonResponse({'message': 'Hello, world, from async!'})
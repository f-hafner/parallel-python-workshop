import asyncio 


async def counter(name):
  for i in range(5):
    print(f"{name:<10} {i:03}")
    await asyncio.sleep(0.2) # the task here is to sleep


async def main():
    await asyncio.gather(counter("Earth"), counter("Moon"))


if __name__ == "__main__":
    asyncio.run(main())
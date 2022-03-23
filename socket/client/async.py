import random
import asyncio


def random_value():
    """Return an integer value

    Returns a random integer between 15 and 30 (inclusive)
    """
    value = random.randint(15, 30)  # could be a temperature reading?
    return value


async def main(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    addr = writer.get_extra_info("peername")
    print(f"Connected to {addr}")

    for _ in range(10):
        value = random_value()

        print(f"Sending {value}")
        message = str(value).encode()  # int as string, to bytes
        writer.write(message)
        await writer.drain()

        data = await reader.read(100)
        response = data.decode()  # from bytes to string
        print("Received", response)

        await asyncio.sleep(1)

    writer.close()


if __name__ == "__main__":
    asyncio.run(main("127.0.0.1", 65432))

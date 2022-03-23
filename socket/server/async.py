import asyncio


async def handle_request(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f"Connection from {addr}")

    while data := await reader.read(100):
        message = data.decode()
        print(f"Received {message}")

        writer.write(data)
        await writer.drain()

    print("Closing connection")
    writer.close()


async def main(host, port):
    server = await asyncio.start_server(handle_request, host, port)

    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main("127.0.0.1", 65432))

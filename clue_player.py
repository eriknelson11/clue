import asyncio
import websockets
import draw_board_terminal
import json

ASSIGNED_SUSPECT = ""
#ASSIGNED_CARDS

async def connect():
    uri = "ws://localhost:8180"
    initial_connect = True

    async with websockets.connect(uri) as websocket:
        while True:
            try:
                # Wait for a message from the server
                message_json = await websocket.recv()
                message = json.loads(message_json)
                ASSIGNED_SUSPECT = message["assigned_suspect"]
                player_locations = message["player_locations"]
                draw_board_terminal.draw_board(player_locations)

                if initial_connect:
                    print(f"Welcome! Your assigned suspect is {ASSIGNED_SUSPECT}")
            except Exception as e:
                print(f"An error occurred: {e}")
                break

# Run the client
asyncio.get_event_loop().run_until_complete(connect())
import players
import asyncio
import websockets
import json

# Keep track of player connections (assigned player -> connection)
connected_players = {}

PLAYER_LOCATIONS = {'Study':"", 'H1':"", 'Hall':"", 'H2':"MS", 'Lounge':"",
                    'H3':"PP", 'H4':"", 'H5':"CM", 
                    'Library':"", 'H6':"", 'Billiard Room':"", 'H7':"",'Dining Room':"",
                    'H8':"MP", 'H9':"", 'H10':"", 
                    'Conservatory':"", 'H11':"MG", 'Ballroom':"", 'H12':"MW",'Kitchen':"",
                    '':''}

# abbreviated suspect list
SUSPECTS = ['CM', 'MS', 'PP', 'MG', 'MW', 'MP']

# handles all web socket connections
async def handler(websocket):
    # max number of connections reached
    if len(SUSPECTS) == 0:
        return
    # Make each a player a random suspect (can let the player choose what suspect they want to be later)
    suspect = SUSPECTS.pop()
    connected_players[suspect] = websocket

    print(f"New player connected: {suspect}")

    try:
        # TODO
        message = {"assigned_suspect": suspect, "player_locations": PLAYER_LOCATIONS, "assigned_cards": "TODO"}
        await websocket.send(json.dumps(message))

        # Handle incoming messages from this client
        while True:
            message = await websocket.recv()
            
            # TODO
            # ingest message and perform action based on message type
            
    
    except websockets.ConnectionClosed:
        print(f"Connection closed from {websocket.remote_address}")
    
    finally:
        # Disconnect
        del connected_players[suspect]

async def public_message(message):
    for player in connected_players.values():
        try:
            await player.send(message)
        except websockets.ConnectionClosed:
            pass

async def private_message(message, player):
    try:
        await connected_players[player].send(message)
    except websockets.ConnectionClosed:
        pass 

async def start_server():
    server = await websockets.serve(handler, "localhost", 8180)
    print("Server started on ws://localhost:8180")
    await server.wait_closed()

asyncio.get_event_loop().run_until_complete(start_server())

import asyncio
from typing import Any, Dict, Optional, Tuple

class RobloxHandler:
    """Handles Roblox game-related operations."""
    
    def __init__(self, game_id: int) -> None:
        """Initialize handler with game ID."""
        self.game_id = game_id
        self.data: Optional[Dict[str, Any]] = None

    async def fetch_game_data(self) -> None:
        """Asynchronously fetch the game data."""
        self.data = await self._simulate_fetch(self.game_id)

    async def _simulate_fetch(self, game_id: int) -> Dict[str, Any]:
        """Simulate fetching game data from an API."""
        await asyncio.sleep(1)
        return {'id': game_id, 'name': f'Game {game_id}', 'players': 42}

    def get_game_info(self) -> Optional[Tuple[int, str, int]]:
        """Return game information such as ID, name, and player count."""
        if self.data:
            return self.data['id'], self.data['name'], self.data['players']
        return None

# Example usage
# async def main():
#     handler = RobloxHandler(1234)
#     await handler.fetch_game_data()
#     info = handler.get_game_info()
#     print(info)

# asyncio.run(main())
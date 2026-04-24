from typing import Any, Dict, Optional

class RobloxHandler:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = 'https://api.roblox.com'

    def get_user_info(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Fetch user information by user ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Optional[Dict[str, Any]]: User information if found, otherwise None.
        """
        import requests
        response = requests.get(f'{self.base_url}/users/{user_id}')
        if response.status_code == 200:
            return response.json()
        return None

    def get_game_info(self, game_id: int) -> Optional[Dict[str, Any]]:
        """Fetch game information by game ID.

        Args:
            game_id (int): The ID of the game.

        Returns:
            Optional[Dict[str, Any]]: Game information if found, otherwise None.
        """
        import requests
        response = requests.get(f'{self.base_url}/games/{game_id}')
        if response.status_code == 200:
            return response.json()
        return None

    def create_game(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Create a new game with given data.

        Args:
            data (Dict[str, Any]): Data for the new game.

        Returns:
            Optional[Dict[str, Any]]: Created game information if successful, otherwise None.
        """
        import requests
        response = requests.post(f'{self.base_url}/games', json=data, headers={'Authorization': f'Bearer {self.api_key}'})
        if response.status_code == 201:
            return response.json()
        return None

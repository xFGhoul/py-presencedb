import aiohttp

from .models import User, Activity
from .errors import (UserNotFound, ActivityNotFound, UnexpectedRequestError)

class Client():
    def __init__(self):
        super().__init__()

    async def _make_request(self, target: str, params: dict) -> dict:
        BASE_URL = "https://api.presencedb.com"
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50", "content-type": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BASE_URL}/{target}", params=params, headers=headers) as response:
                json = await response.json()
                return json
    
    async def get_user(self, user_id: int) -> User:
        """Get A Users Profile
        
        
        Args:
            user_id (int): Discord ID of User
        
        Raises:
            UserNotFound: User not in DB
        
        Returns:
            User: Object of JSON response from API
        
        """
        user_params = {"id": user_id}
        user_info = await self._make_request("user", user_params)
        if user_info:
            return User(user_info)
        else:
            raise UserNotFound("User Couldn't Be Found")

    async def get_activity(self, activity_id: int) -> Activity:
        """Get Info About an Activity

        Parameters
        ----------
        activity_id : int
            ID of Activity

        Returns
        -------
        Activity
            [description]
        """
        activity_params = {"id": activity_id}
        activity_info = await self._make_request("activity", activity_params)
        if activity_info:
            return Activity(activity_info)
        else:
            raise ActivityNotFound("Activity Couldn't Be Found")


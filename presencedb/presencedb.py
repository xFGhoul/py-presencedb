import aiohttp

from typing import List

from ._constants import API
from .models import User, Activity, TopActivity, TrendingActivity
from .errors import UserNotFound, ActivityNotFound, UnexpectedRequestError


class Client:
    def __init__(self):
        super().__init__()

    async def _make_request(self, target: str) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{API.BASE_URL}/{target}", headers=API.HEADERS
            ) as response:
                json = await response.json()
                return json

    async def get_user(self, user_id: int, should_format: bool) -> User:
        """Get A Users Profile


        Args:
            user_id (int): Discord ID of User

        Raises:
            UserNotFound: User not in DB

        Returns:
            User: Object of JSON response

        """
        user_info = await self._make_request(f"user/{user_id}")
        user_stats = await self._make_request(f"user/{user_id}/stats")
        if user_info and user_stats is not None:
            return User(user_info, user_stats, should_format)
        else:
            raise UserNotFound("User Couldn't Be Found")

    async def get_activity(self, activity_id: int, should_format: bool) -> Activity:
        """Get An Activity

        Args:
            activity_id (int): ID Of The Activity
            should_format (bool): If The Values Should Be Formatted

        Raises:
            ActivityNotFound: Activity Not Found In DB

        Returns:
            Activity: Object Of JSON Response
        """
        activity_info = await self._make_request(f"activity/{activity_id}")
        activity_stats = await self._make_request(f"activity/{activity_id}/stats")
        if activity_info and activity_stats is not None:
            return Activity(activity_info, activity_stats, should_format)
        else:
            raise ActivityNotFound("Activity Couldn't Be Found")

    async def get_top_activities(self) -> List[TopActivity]:
        """Returns The Top Activities

        Raises:
            UnexpectedRequestError: HTTP Request Was Unable To Be Processed

        Returns:
            List[TopActivity]: List Of Top Activities
        """
        top_activity_info = await self._make_request("activities/top")
        if top_activity_info:
            top_activities = [TopActivity(**activity) for activity in top_activity_info]
            return top_activities
        else:
            raise UnexpectedRequestError("Could Not Fetch The Top Activities")

    async def get_trending_activities(self) -> List[TrendingActivity]:
        """Returns The Trending Activities

        Raises:
            UnexpectedRequestError: HTTP Request Was Unable To Be Processed

        Returns:
            List[TrendingActivity]: List Of Trending Activities
        """
        trending_activity_info = await self._make_request("activities/trending")
        if trending_activity_info:
            trending_activities = [
                TrendingActivity(**activity) for activity in trending_activity_info
            ]
            return trending_activities
        else:
            raise UnexpectedRequestError("Could Not Fetch The Trending Activities")

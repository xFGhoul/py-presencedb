import logging

from typing import List, Optional, Tuple, Union, Dict, Self, Any
from aiohttp import ClientSession

from .abc import TopActivity, TrendingActivity
from .activity import Activity
from .enums import ActivityID
from .user import User
from .http import Route, HTTP

__all__: Tuple[str, ...] = ("Client",)

logger = logging.getLogger(__name__)


class Client:
    """Client Interface For Interacting With PresenceDB API

    Args:
        session (Optional[aiohttp.ClientSession]): Client session used for HTTP requests.
    """

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        self._http: HTTP = HTTP(session=session)

    async def __aenter__(self) -> Self:
        if self._http.session is None:
            await self._http.create_client_session()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.cleanup()

    async def cleanup(self) -> None:
        """Closes The Current Client Session

        Raises:
            RuntimeError: If The Session Was Already Closed
        """
        if self._http.session.closed:
            raise RuntimeError("Client Session Already Closed.")
        logger.debug("Closing Session")
        await self._http.session.close()
        logger.debug("Session Closed")

    async def get_user(self, user_id: int, format: Optional[bool] = False) -> User:
        """Get A User's Profile

        Args:
            user_id (int): Discord ID of user
            format (bool, optional): If to format user data. Defaults to False

        Returns:
            User: PresenceDB User

        Raises:
            UserNotFound: If the user was not found
        """
        data: Dict = await self._http.request(
            Route("GET", "user/{user_id}", user_id=user_id)
        )
        stats: Dict = await self._http.request(
            Route("GET", "user/{user_id}/stats", user_id=user_id)
        )
        trending: Dict = await self._http.request(
            Route("GET", "user/{user_id}/trending-activities", user_id=user_id)
        )
        top: Dict = await self._http.request(
            Route("GET", "user/{user_id}/top-activities", user_id=user_id)
        )
        return User(
            data.get("data"),
            stats.get("data"),
            trending.get("data"),
            top.get("data"),
            format,
        )

    async def get_users(
        self, user_ids: List[int], format: Optional[bool] = False
    ) -> List[User]:
        """Get Multiple User Profiles

        Args:
            user_ids (List[int]): Discord IDs of users
            format (bool, optional): If to format user data. Defaults to False

        Returns:
            List[User]: List of users.

        Raises:
            PresenceDBError: If the users were not found.
        """
        users: List = []
        for user_id in user_ids:
            data: Dict = await self._http.request(
                Route("GET", "user/{user_id}", user_id=user_id)
            )
            stats: Dict = await self._http.request(
                Route("GET", "user/{user_id}/stats", user_id=user_id)
            )
            trending: Dict = await self._http.request(
                Route("GET", "user/{user_id}/trending-activities", user_id=user_id)
            )
            top: Dict = await self._http.request(
                Route("GET", "user/{user_id}/top-activities", user_id=user_id)
            )
            users.append(
                User(
                    data.get("data"),
                    stats.get("data"),
                    trending.get("data"),
                    top.get("data"),
                    format,
                )
            )
        return users

    async def get_activity(
        self, activity_id: Union[int, str, ActivityID], format: Optional[bool] = False
    ) -> Activity:
        """Get An Activity

        Args:
            activity_id (Union[int, str, ActivityID]): ID of activity
            format (bool, optional): If duration values should be formatted. Defaults to False

        Returns:
            Activity: PresenceDB Activity

        Raises:
            PresenceDBError: If the activity could not be found
        """
        data: Dict = await self._http.request(
            Route("GET", "activity/{activity_id}", activity_id=activity_id)
        )
        stats: Dict = await self._http.request(
            Route("GET", "activity/{activity_id}/stats", activity_id=activity_id)
        )
        return Activity(data.get("data"), stats.get("data"), format)

    async def get_activities(
        self,
        activity_ids: Union[List[int], List[str], List[ActivityID]],
        format: Optional[bool] = False,
    ) -> List[Activity]:
        """Get Multiple Activities

        Args:
            activity_ids (List[Union[int, str, ActivityID]]): ID of activities
            format (bool, optional): If duration values should be formatted. Defaults to False.

        Returns:
            List[Activity]: List of found activities

        Raises:
            PresenceDBError: If the activity could not be found
        """
        activities: List = []
        for activity_id in activity_ids:
            data: Dict = await self._http.request(
                Route("GET", "activity/{activity_id}", activity_id=activity_id)
            )
            stats: Dict = await self._http.request(
                Route("GET", "activity/{activity_id}/stats", activity_id=activity_id)
            )
            activities.append(Activity(data.get("data"), stats.get("data"), format))
        return activities

    async def get_top_activities(self) -> List[TopActivity]:
        """Returns Top Activities

        Returns:
            List[TopActivity]: List of Top Activities

        Raises:
            PresenceDBError: If Top Activities could not be fetched.
        """
        data: Dict = await self._http.request(Route("GET", "activities/top"))
        return [TopActivity(**activity) for activity in data.get("data")]

    async def get_trending_activities(self) -> List[TrendingActivity]:
        """Returns Current Trending Activities

        Returns:
            List[TrendingActivity]: List of trending activities

        Raises:
            PresenceDBError: Trending activities could not be fetched
        """
        data: Dict = await self._http.request(Route("GET", "activities/trending"))
        return [TrendingActivity(**activity) for activity in data.get("data")]

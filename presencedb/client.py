import logging

from typing import List, Optional, Tuple, Union, Self, Any
from aiohttp import ClientSession

from .abc import TopActivity, TrendingActivity
from .activity import Activity
from .session import Session
from .enums import ActivityID
from .user import User
from .http import Route, HTTP

__all__: Tuple[str, ...] = ("Client",)

logger = logging.getLogger(__name__)


class Client:
    """Client Interface For Interacting With PresenceDB API

    Parameters
    -----------
    session: Optional[aiohttp.ClientSession]
        Client Session Used For HTTP Requests
    """

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        self._http = HTTP(session=session)

    async def __aenter__(self) -> Self:
        if self._http.session is None:
            await self._http.create_client_session()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.cleanup()

    async def cleanup(self) -> None:
        """Closes The Current Client Session

        Raises
        ------
        RuntimeError
            If The Session Was Already Closed
        """
        if self._http.session.closed:
            raise RuntimeError("Client Session Already Closed.")
        logger.debug("Closing Session")
        await self._http.session.close()
        logger.debug("Session Closed")

    async def get_session(self) -> Session:
        """
        Get Current Logged In User's Session


        Returns
        -------
        Session
            Class Representing Session
        """
        data = await self._http.request(Route("GET", "auth/session"))
        return Session(data)

    async def get_user(self, user_id: int, format: Optional[bool] = False) -> User:
        """Get A User's Profile

        Parameters
        ----------
        user_id : :class:`int`
            Discord ID of User
        format : Optional[:class:`bool`]
            If To Format User Data, by default False

        Returns
        -------
        User
            Object Response Of User

        Raises
        ------
        UserNotFound
            If The User Was Not Found
        """
        data = await self._http.request(Route("GET", "user/{user_id}", user_id=user_id))
        stats = await self._http.request(
            Route("GET", "user/{user_id}/stats", user_id=user_id)
        )
        trending = await self._http.request(
            Route("GET", "user/{user_id}/trending-activities", user_id=user_id)
        )
        top = await self._http.request(
            Route("GET", "user/{user_id}/top-activities", user_id=user_id)
        )
        return User(data, stats, trending, top, format)

    async def get_users(
        self, user_ids: List[int], format: Optional[bool] = False
    ) -> List[User]:
        """Get Multiple User Profiles

        Parameters
        ----------
        user_id : List[:class:`int`]
            Discord ID's of Users
        format : Optional[:class:`bool`]
            If To Format User Data, by default False

        Returns
        -------
        List[User]
            List of Users

        Raises
        ------
        UserNotFound
            If The Users Were Not Found
        """
        users = []
        for user_id in user_ids:
            data = await self._http.request(
                Route("GET", "user/{user_id}", user_id=user_id)
            )
            stats = await self._http.request(
                Route("GET", "user/{user_id}/stats", user_id=user_id)
            )
            trending = await self._http.request(
                Route("GET", "user/{user_id}/trending-activities", user_id=user_id)
            )
            top = await self._http.request(
                Route("GET", "user/{user_id}/top-activities", user_id=user_id)
            )
            users.append(User(data, stats, trending, top, format))
        return users

    async def get_activity(
        self, activity_id: Union[int, str, ActivityID], format: Optional[bool] = False
    ) -> Activity:
        """Get An Activity

        Parameters
        ----------
        activity_id : Union[:class:`int`, class:`str`, ActivityID]
            ID of Activity
        format : Optional[:class:`bool`]
            If Duration Values Should Be Formatted, by default False

        Returns
        -------
        Activity
            Object Of JSON Response

        Raises
        ------
        ActivityNotFound
            If The Activity Could Not Be Found
        """
        data = await self._http.request(
            Route("GET", "activity/{activity_id}", activity_id=activity_id)
        )
        stats = await self._http.request(
            Route("GET", "activity/{activity_id}/stats", activity_id=activity_id)
        )
        return Activity(data, stats, format)

    async def get_activities(
        self,
        activity_ids: Union[List[int], List[str], List[ActivityID]],
        format: Optional[bool] = False,
    ) -> List[Activity]:
        """Get Multiple Activities

        Parameters
        ----------
        activity_ids: List[:class:`int`], List[:class:`str`], List[ActivityID]
            ID of Activities
        format : Optional[:class:`bool`]
            If Duration Values Should Be Formatted, by default False

        Returns
        -------
        List[Activity]
            List of Found Activities

        Raises
        ------
        ActivityNotFound
            If The Activity Could Not Be Found
        """
        activities = []
        for activity_id in activity_ids:
            data = await self._http.request(
                Route("GET", "activity/{activity_id}", activity_id=activity_id)
            )
            stats = await self._http.request(
                Route("GET", "activity/{activity_id}/stats", activity_id=activity_id)
            )
            activities.append(Activity(data, stats, format))
        return activities

    async def get_top_activities(self) -> List[TopActivity]:
        """Returns Top Activities

        Returns
        -------
        List[TopActivity]
            List Of Top Activities

        Raises
        ------
        ActivitiesNotFound
            Top Activities Could Not Be Fetched
        """
        data = await self._http.request(Route("GET", "activities/top"))
        return [TopActivity(**activity) for activity in data]

    async def get_trending_activities(self) -> List[TrendingActivity]:
        """Returns Current Trending Activities

        Returns
        -------
        List[TrendingActivity]
            List Of Trending Activities
        Raises
        ------
        ActivitiesNotFound
            Trending Activities Could Not Be Fetched
        """
        data = await self._http.request(Route("GET", "activities/trending"))
        return [TrendingActivity(**activity) for activity in data]

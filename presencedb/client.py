import logging
from typing import Dict, List, Optional, Tuple, Union

import aiohttp
from aiohttp import ClientSession

from .abc import TopActivity, TrendingActivity
from .activity import Activity
from .constants import API
from .enums import ActivityID
from .errors import ActivitiesNotFound, ActivityNotFound, UserNotFound
from .user import User

__all__: Tuple[str, ...] = ("Client",)


class Client:
    """Client Interface For Interacting With PresenceDB API

    Parameters
    -----------
    session: Optional[aiohttp.ClientSession]
        Client Session Used For HTTP Requests
    """

    __slots__ = (
        "session",
        "logger",
    )

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        self.logger = logging.getLogger(__name__)
        if session is None:
            self.session = aiohttp.ClientSession(headers=API.HEADERS)
        else:
            self.session = session

    async def _make_request(self, target: str) -> Dict:
        """

        Sends An HTTP /GET Request To PresenceDB API

        Parameters
        ----------
        target: :class:`str`
            API Endpoint

        Returns
        -------
        Dict
            JSON Response From API

        Raises
        ------
        HTTPError
            If The Request Failed
        """
        async with self.session.get(API.BASE_URL / target) as response:
            self.logger.debug(f"Sending HTTP /GET Request: {API.BASE_URL}/{target}")
            json = await response.json()
            return json

    async def cleanup(self) -> None:
        """Closes The Current Client Session

        Raises
        ------
        RuntimeError
            If The Session Was Already Closed
        """
        if self.session.closed:
            raise RuntimeError("Client Session Already Closed.")
        self.logger.debug("Closing Session")
        await self.session.close()
        self.logger.debug("Session Closed")

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
        data = await self._make_request(f"user/{user_id}")
        stats = await self._make_request(f"user/{user_id}/stats")
        if data and stats is not None:
            return User(data, stats, format)
        else:
            raise UserNotFound

    async def get_users(
        self, user_ids: List[int], format: Optional[bool] = False
    ) -> List[User]:
        """Get Multiple User Profiles

        Parameters
        ----------
        user_id : :class:`List[int]`
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
            data = await self._make_request(f"user/{user_id}")
            stats = await self._make_request(f"user/{user_id}/stats")
            if data and stats is not None:
                users.append(User(data, stats, format))
            else:
                raise UserNotFound
        return users

    async def get_activity(
        self, activity_id: Union[int, ActivityID], format: Optional[bool] = False
    ) -> Activity:
        """Get An Activity

        Parameters
        ----------
        activity_id : Union[:class:`int`, ActivityID]
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
        data = await self._make_request(f"activity/{activity_id}")
        stats = await self._make_request(f"activity/{activity_id}/stats")
        if data and stats is not None:
            return Activity(data, stats, format)
        else:
            raise ActivityNotFound

    async def get_activities(
        self,
        activity_ids: Union[List[int], List[ActivityID]],
        format: Optional[bool] = False,
    ) -> List[Activity]:
        """Get Multiple Activities

        Parameters
        ----------
        activity_ids: List[:class:`int`], List[ActivityID]
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
            data = await self._make_request(f"activity/{activity_id}")
            stats = await self._make_request(f"activity/{activity_id}/stats")
            if data and stats is not None:
                activities.append(Activity(data, stats, format))
            else:
                raise ActivityNotFound
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
        data = await self._make_request("activities/top")
        if data:
            top_activities = [TopActivity(**activity) for activity in data]
            return top_activities
        else:
            raise ActivitiesNotFound

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
        data = await self._make_request("activities/trending")
        if data:
            trending_activities = [TrendingActivity(**activity) for activity in data]
            return trending_activities
        else:
            raise ActivitiesNotFound

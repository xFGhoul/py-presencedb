.. currentmodule:: presencedb

API Reference
=============

Client
------

.. attributetable:: Client

.. autoclass:: Client
    :members:

Models
------

User
~~~~

.. attributetable:: User

.. autoclass:: presencedb.user.User()
    :members:

UserStats
~~~~~~~~~
.. attributetable:: UserStats

.. autoclass:: presencedb.user.UserStats()
    :members:

Activity
~~~~~~~~
.. attributetable:: Activity

.. autoclass:: presencedb.activity.Activity()
    :members:

ActivityStats
~~~~~~~~~~~~~
.. attributetable:: ActivityStats

.. autoclass:: presencedb.activity.ActivityStats()
    :members:


Objects
-------

TopUser
~~~~~~~
.. attributetable:: TopUser

.. autoclass:: presencedb.abc.TopUser()
    :members:

TopActivity
~~~~~~~~~~~
.. attributetable:: TopActivity

.. autoclass:: presencedb.abc.TopActivity()
    :members:

TrendingActivity
~~~~~~~~~~~~~~~~

.. attributetable:: TrendingActivity

.. autoclass:: presencedb.abc.TrendingActivity()
    :members:

CurrentActivity
~~~~~~~~~~~~~~~
.. attributetable:: presencedb.user.CurrentActivity

.. autoclass:: presencedb.user.CurrentActivity()
    :members:

PlaytimeDate
~~~~~~~~~~~~
.. attributetable:: presencedb.abc.PlaytimeDate

.. autoclass:: presencedb.abc.PlaytimeDate()
    :members:

AvatarHistory
~~~~~~~~~~~~~
.. attributetable:: presencedb.user.AvatarHistory

.. autoclass:: presencedb.user.AvatarHistory()
    :members:

Record
~~~~~~
.. attributetable:: presencedb.user.Record

.. autoclass:: presencedb.user.Record()
    :members:

ActivityRecord
~~~~~~~~~~~~~~
.. attributetable:: presencedb.user.ActivityRecord

.. autoclass:: presencedb.user.ActivityRecord()
    :members:

Avatar
~~~~~~
.. attributetable:: presencedb.abc.Avatar

.. autoclass:: presencedb.abc.Avatar()
    :members:

Enums
-----

ActivityID
~~~~~~~~~~

.. autoclass:: presencedb.enums.ActivityID

    .. attribute:: SPOTIFY

    .. attribute:: YOUTUBE

    .. attribute:: VALORANT

    .. attribute:: ROBLOX

    .. attribute:: VSCODE

    .. attribute:: OSU

    .. attribute:: NETFLIX

    .. attribute:: LUNAR_CLIENT

    .. attribute:: MINECRAFT

    .. attribute:: GENSHIN_IMPACT

    .. attribute:: TWITCH

    .. attribute:: REDDIT

    .. attribute:: MEDAL

    .. attribute:: LEAGUE_OF_LEGENDS

    .. attribute:: CSGO

    .. attribute:: CUSTOM_STATUS

    .. attribute:: GRAND_THEFT_AUTO_V

    .. attribute:: CRUNCHYROLL

    .. attribute:: CODE

    .. attribute:: YOUTUBE_MUSIC


.. _presencedb-api-utils:

Utility Functions
-----------------

.. autofunction:: presencedb.utils.humanize_duration
.. autofunction:: presencedb.utils.icon_to_bytes

Exceptions
----------

.. autoexception:: PresenceDBException()

.. autoexception:: HTTPException()

.. autoexception:: NotFound()

.. autoexception:: PresenceDBError()


Exception Hierarchy
~~~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`Exception`
        - :exc:`PresenceDBException`
           - :exc:`HTTPException`
            - :exc:`NotFound`
            - :exc:`PresenceDBError`

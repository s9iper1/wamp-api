import txaio

import constants
import sqlalchemy as db

from database import user_database

txaio.use_asyncio()
from os import environ
import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner



class Component(ApplicationSession):
    async def onJoin(self, details):
        # a remote procedure; see frontend.py for a Python front-end
        # that calls this. Any language with WAMP bindings can now call
        # this procedure if its connected to the same router and realm.

        def register(username, email):
            print(f"name : {username} and age is {email}")
            user_database.create_new_user(username, email)
            return username, email

        registration = self.register(register, constants.register)
        # print(f"registered 'com.myapp.add2' with id {registration.id}")

        # publish an event every second. The event payloads can be
        # anything JSON- and msgpack- serializable
        # while True:
        #     self.publish('com.myapp.hello', 'Hello, world!')
        #     await asyncio.sleep(1)
        #


if __name__ == '__main__':
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", "ws://localhost:8080/ws"),
        "realm1",
    )
    runner.run(Component)

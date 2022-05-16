from os import environ
import txaio

import constants
txaio.use_asyncio()
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

import constants


class Component(ApplicationSession):
    async def onJoin(self, details):
        # listening for the corresponding message from the "backend"
        # (any session that .publish()es to this topic).
        def onevent(msg):
            print("Got event: {}".format(msg))
        await self.subscribe(onevent, constants.register)
        user_name = input("username: \n")
        email = input("email: \n")
        # call a remote procedure.
        res = await self.call(constants.register, user_name, email)
        print("Got result: {}".format(res))


if __name__ == '__main__':
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", "ws://localhost:8080/ws"),
        "realm1",
    )
    runner.run(Component)

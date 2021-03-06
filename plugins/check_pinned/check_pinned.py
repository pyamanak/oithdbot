from __future__ import unicode_literals
# don't convert to ascii in py2.7 when creating string to return

crontable = []
outputs = []

# Catch all the events
def catch_all(data):
    # print(data)
    pass

# Only handles when a user becomes active
def process_presence_change(data):
    print("PRESENCE CHANGE")

    # While we can respond to presence change events,
    # we cannot actually send a message to a channel as
    # the data structure does not contain a channel ID
    if (data["presence"].startswith("active")):
        print("IS ACTIVE")
        outputs.append([data['user'], "Hello \"{}\"".format(
            data['user'])]
        )

    # Can we send a message to the Slackbot with the UserID
    # (which we have) and have the slackbot post to the user?


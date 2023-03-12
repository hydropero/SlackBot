import os
# Use the package we installed
from slack_bolt import App
from sqlalchemy.orm import sessionmaker
import db
import models
import datetime
import sqlalchemy
import time
from sqlalchemy import create_engine

#minor12
# Retrieves Slack credentials from non-git synced file
with open('dbinfo') as dbinfo:
  lines = dbinfo.readlines()
  token_value = lines[0].split('=')[1].strip()
  signing_secret_value = lines[1].split('=')[1].strip()


# Initializes your app with your bot token and signing secret
app = App(
    token=token_value,
    signing_secret=signing_secret_value
)

Standups = models.Standups

@app.command("/standup")
def open_modal(ack, client, body):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "standup",
            "title": {
                "type": "plain_text",
                "text": "Daily Standup Automator",
                "emoji": False
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
                "emoji": False
            },
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": False
            },
            "blocks": [
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Welcome to the Daily Standup Bot. Please make sure to answer all questions as accurately and completely as possible. All submissions will be saved and made retrievable by the user who created the submission."
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Note: responses are not being sanitized for safety currently, so please avoid special characters where possible."
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "input",
                    "block_id": "do_yesterday",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "What did you do yesterday?",
                        "emoji": False
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "input",
                    "block_id": "tech_do_yesterday",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "What did you do tech related yesterday?",
                        "emoji": False
                    }
                },
                {
                    "type": "input",
                    "block_id": "tech_type",
                    "element": {
                        "type": "multi_static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select options",
                            "emoji": False
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Virtualization",
                                    "emoji": False
                                },
                                "value": "value-0"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Networking",
                                    "emoji": False
                                },
                                "value": "value-1"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Cloud",
                                    "emoji": False
                                },
                                "value": "value-2"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Security",
                                    "emoji": False
                                },
                                "value": "value-3"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Linux",
                                    "emoji": False
                                },
                                "value": "value-4"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Scripting/Programming",
                                    "emoji": False
                                },
                                "value": "value-5"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "General Computing",
                                    "emoji": False
                                },
                                "value": "value-6"
                            }
                        ],
                        "action_id": "multi_static_select-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "What area of technology did you work within?",
                        "emoji": False
                    }
                },
                {
                    "type": "input",
                    "block_id": "challenge",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "What was the biggest challenge?",
                        "emoji": False
                    }
                },
                {
                    "type": "input",
                    "block_id": "do_today",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "What will you do today?",
                        "emoji": False
                    }
                },
                {
                    "type": "input",
                    "block_id": "blockers",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Are there any blockers?",
                        "emoji": False
                    }
                }
            ]
        },
    )


@app.view("standup")
def handle_submission(ack, body, client, view, logger):
    # Assume there's an input block with `input_c` as the block_id and `dreamy_input`
    user = body["user"]["id"]
    # Validate the inputs
    hopes_and_dreams = view["state"]["values"]
    # Acknowledge the
    #  view_submission request and close the modal


    # Do whatever you want with the input data - here we're saving it to a DB
    # then sending the user a verification of their submission
    current_date = datetime.datetime.now()
    current_time = datetime.datetime.time()
    do_yesterday = view["state"]["values"]["do_yesterday"]["plain_text_input-action"]
    tech_do_yesterday = view["state"]["values"]["tech_do_yesterday"]["plain_text_input-action"]
    tech_type = view["state"]["values"]["tech_type"]["multi_static_select-action"]
    challenge = view["state"]["values"]["challenge"]["plain_text_input-action"]
    do_today = view["state"]["values"]["do_today"]["plain_text_input-action"]
    blockers = view["state"]["values"]["blockers"]["plain_text_input-action"]

    standup_entry = Standups(
        username = "Myles",
        date = current_date,
        time = current_time,
        do_yesterday = do_yesterday,
        tech_do_yesterday = tech_do_yesterday,
        tech_type = tech_type,
        challenge = challenge,
        do_today = do_today,
        blockers = blockers
    )
    with db.session.begin() as session:
        session.add(standup_entry)


    view = {
        "type": "modal",
        "title": {
            "type": "plain_text",
            "text": "Completed!",
            "emoji": False
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Thank you for your submission. You may now click 'Close' to exit this form."
                }
            }
        ]
    }

    ack()
    ack(response_action="update", view=view)

    # Message to send user
    msg = ""
    try:
        # Save to DB
        msg = f"Your submission was successful"
    except Exception as e:
        # Handle error
        msg = "There was an error with your submission"

    # Message the user
    try:
        client.chat_postMessage(channel=user, text=msg)
    except e:
        logger.exception(f"Failed to post a message {e}")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))

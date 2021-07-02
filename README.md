# turnio-mark-as-read

An example Turn.io UI integration on Replit. This will automatically mark any message received from a user as read and will display a blue double check mark on the consumer client.

*This Replit assumes the following*:

1. You have gone through the [webhooks example](https://github.com/turnhub/turnio-webhooks-replit) and are comfortable with how to get an authentication for Turn and set it up as a secret in Repl.it

# How to run this Repl.it

[![Run on Repl.it](https://repl.it/badge/github/turnhub/turnio-mark-as-read-replit)](https://repl.it/github/turnhub/turnio-mark-as-read-replit)

1. Click the `Run on Repl.it` button above and install this example into your Repl.it workspace.
2. Get a Turn token and add it as a secret called `TOKEN` in Repl.it
3. Set up your webhook in the Turn UI using the replit.URL.
4. Send a message to your number and watch it being marked as read!

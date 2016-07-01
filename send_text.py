from twilio.rest import TwilioRestClient

account_sid = "AC0ca58c2cacff589c5395eaef6ba4bf53"
auth_token = "b1e17879c8440d0697930ba8aac116b3"

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "Hello, this is a trial text",
    to = "+447563200272",
    from_ = "+16502854887"
)
